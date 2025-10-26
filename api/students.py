from fastapi import APIRouter, HTTPException
from tinydb import TinyDB, Query

router = APIRouter()
db = TinyDB('db.json')

# Request approval for a module or learning path
@router.post("/request-approval")
def request_approval(studentId: str, moduleId: str):
    students_table = db.table('students')
    approvals_table = db.table('approvals')
    student = students_table.get(Query().id == studentId)
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    existing = approvals_table.get((Query().studentId == studentId) & (Query().moduleId == moduleId))
    if existing:
        raise HTTPException(status_code=400, detail="Approval request already sent")
    
    approvals_table.insert({
        "id": f"apr_{studentId}_{moduleId}",
        "studentId": studentId,
        "studentName": student["name"],
        "moduleId": moduleId,
        "status": "Pending"
    })
    return {"message": "Approval request sent successfully"}

# Admin: view pending approvals
@router.get("/pending-approvals")
def pending_approvals():
    approvals_table = db.table('approvals')
    pending = approvals_table.search(Query().status == "Pending")
    return pending

# Admin: approve/reject a request
@router.post("/handle-approval")
def handle_approval(requestId: str, approve: bool):
    approvals_table = db.table('approvals')
    students_table = db.table('students')
    modules_table = db.table('modules')
    
    req = approvals_table.get(Query().id == requestId)
    if not req:
        raise HTTPException(status_code=404, detail="Approval request not found")
    
    if approve:
        req["status"] = "Approved"
        student = students_table.get(Query().id == req["studentId"])
        module = modules_table.get(Query().id == req["moduleId"])
        if req["moduleId"] not in student["completedModules"]:
            student["completedModules"].append(req["moduleId"])
            student["progress"] = int(len(student["completedModules"]) / len(modules_table.all()) * 100)
            students_table.update(student, Query().id == student["id"])
        if req["studentId"] not in module["completedBy"]:
            module["completedBy"].append(req["studentId"])
            modules_table.update(module, Query().id == module["id"])
    else:
        req["status"] = "Rejected"
    
    approvals_table.update(req, Query().id == requestId)
    return {"message": f"Request {'approved' if approve else 'rejected'}"}

# Admin: get all students
@router.get("/all")
def get_all_students():
    students_table = db.table('students')
    return students_table.all()
