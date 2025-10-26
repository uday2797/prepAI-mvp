from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def ask_question(question: str):
    # Simple static responses for demo
    responses = {
        "hello": "Hi! How can I help you today?",
        "progress": "You can check your progress in your dashboard.",
        "modules": "All modules are listed in your dashboard.",
    }
    answer = responses.get(question.lower(), "Sorry, I don't understand yet.")
    return {"answer": answer}
