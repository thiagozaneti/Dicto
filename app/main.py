from fastapi import FastAPI
from app.api.routes.transcribe_route import transcribe_route

app = FastAPI()
app.include_router(transcribe_route, prefix="/api/v1")

