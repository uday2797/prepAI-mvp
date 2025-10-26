from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Relative imports for Vercel serverless
from .auth import router as auth_router
from .modules import router as modules_router
from .students import router as students_router
from .chatbot import router as chatbot_router

app = FastAPI()

# Enable CORS so frontend can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo, allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth")
app.include_router(modules_router, prefix="/modules")
app.include_router(students_router, prefix="/students")
app.include_router(chatbot_router, prefix="/chatbot")
