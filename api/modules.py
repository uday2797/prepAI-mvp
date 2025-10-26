from fastapi import APIRouter, HTTPException
from tinydb import TinyDB, Query

router = APIRouter()
db = TinyDB('db.json')

@router.get("/")
def get_modules():
    modules_table = db.table('modules')
    return modules_table.all()

@router.post("/complete")
def complete_module(studentId: str, moduleId: str):
    students_table = db.table('students')
    modules_table = db.table('modules')
    
    student = students_table.get(Query().id == studentId)
    module = modules_table.get(Query().id == moduleId)
    if not student or not module:
        raise HTTPException(status_code=404, detail="Student or Module not found")
    
    if moduleId not in student["completedModules"]:
        student["completedModules"].append(moduleId)
        student["progress"] = int(len(student["completedModules"]) / len(modules_table.all()) * 100)
        students_table.update(student, Query().id == studentId)
    
    if studentId not in module["completedBy"]:
        module["completedBy"].append(studentId)
        modules_table.update(module, Query().id == moduleId)
    
    return {"progress": student["progress"]}
