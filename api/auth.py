from fastapi import APIRouter, HTTPException
from tinydb import TinyDB, Query
import uuid

router = APIRouter()
db = TinyDB('db.json')

@router.post("/login")
def login(email: str, password: str):
    students = db.table('students')
    admins = db.table('admins')
    user = students.get(Query().email == email) or admins.get(Query().email == email)
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return user

@router.post("/register")
def register(name: str, email: str, password: str, branch: str, careerInterest: str):
    students = db.table('students')
    existing = students.get(Query().email == email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    student_id = str(uuid.uuid4())
    students.insert({
        "id": student_id,
        "name": name,
        "email": email,
        "password": password,
        "branch": branch,
        "careerInterest": careerInterest,
        "completedModules": [],
        "progress": 0
    })
    return {"id": student_id}
