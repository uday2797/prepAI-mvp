from fastapi import APIRouter, HTTPException
from tinydb import TinyDB, Query, MemoryStorage

import uuid

router = APIRouter()

# In-memory DB
db = TinyDB(storage=MemoryStorage)

# Tables
students_table = db.table('students')
admins_table = db.table('admins')
modules_table = db.table('modules')
approvals_table = db.table('approvals')

# Preload students
students_table.insert_multiple([
    {"id":"s1","name":"Uday","email":"uday@student.com","password":"pass1","branch":"CSE","careerInterest":"IT","completedModules":[],"progress":0},
    {"id":"s2","name":"Raghu","email":"raghu@student.com","password":"pass2","branch":"ECE","careerInterest":"Core","completedModules":[],"progress":0},
    {"id":"s3","name":"Akash","email":"akash@student.com","password":"pass3","branch":"ME","careerInterest":"Core","completedModules":[],"progress":0},
    {"id":"s4","name":"Sasi","email":"sasi@student.com","password":"pass4","branch":"EEE","careerInterest":"IT","completedModules":[],"progress":0},
    {"id":"s5","name":"Ranjith","email":"Ranjith@student.com","password":"pass5","branch":"CSE","careerInterest":"IT","completedModules":[],"progress":0}
])

# Preload admin
admins_table.insert({"id":"a1","name":"Admin","email":"admin@college.edu","password":"admin123"})

# Preload modules
modules_table.insert_multiple([
    {"id":"m1","title":"Aptitude Basics","branch":["All"],"youtubeLink":"https://www.youtube.com/watch?v=L-EFQ5q6RvM","completedBy":[]},
    {"id":"m2","title":"Basic of Python","branch":["CSE","ECE"],"youtubeLink":"https://www.youtube.com/watch?v=QXeEoD0pB3E","completedBy":[]},
    {"id":"m3","title":"OS Basics","branch":["All"],"youtubeLink":"https://www.youtube.com/watch?v=vBURTt97EkA","completedBy":[]},
    {"id":"m4","title":"Communication Skills","branch":["All"],"youtubeLink":"https://www.youtube.com/watch?v=2xdUQadfmqg","completedBy":[]}
])

# Approvals table empty initially

@router.post("/login")
def login(email: str, password: str):
    students = db.table('students')
    admins = db.table('admins')
    user = students.get(Query().email == email) or admins.get(Query().email == email)
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": "admin" if user in admins.all() else "student"
    }

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
    return {"id": student_id, "name": name, "email": email, "role": "student"}
