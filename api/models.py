from pydantic import BaseModel
from typing import List, Optional

# ----------------------------
# Student Models
# ----------------------------
class Student(BaseModel):
    id: str
    name: str
    email: str
    password: str
    branch: str
    careerInterest: str
    completedModules: List[str] = []
    progress: int = 0

class StudentLogin(BaseModel):
    email: str
    password: str

class StudentRegister(BaseModel):
    name: str
    email: str
    password: str
    branch: str
    careerInterest: str

# ----------------------------
# Admin Models
# ----------------------------
class Admin(BaseModel):
    id: str
    name: str
    email: str
    password: str

# ----------------------------
# Module Models
# ----------------------------
class Module(BaseModel):
    id: str
    title: str
    branch: List[str]
    youtubeLink: str
    completedBy: List[str] = []

class ModuleCompleteRequest(BaseModel):
    studentId: str
    moduleId: str

# ----------------------------
# Approval Models
# ----------------------------
class ApprovalRequest(BaseModel):
    studentId: str
    moduleId: str

class HandleApprovalRequest(BaseModel):
    requestId: str
    approve: bool

# ----------------------------
# Chatbot Model
# ----------------------------
class QuestionRequest(BaseModel):
    question: str
