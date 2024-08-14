from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from chat import get_chat
from settings import init_ollama

load_dotenv()

app = FastAPI()
init_ollama()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str


async def response_streamer(response):
    for token in response:
        yield f"{token}"


@app.post("/chat/")
async def read_root(
        question: Question,
):
    chat = get_chat()
    response = chat.stream_chat(question.question)
    return StreamingResponse(response_streamer(response.response_gen))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
