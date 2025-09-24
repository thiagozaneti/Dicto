from fastapi import APIRouter, UploadFile, File, HTTPException
from app.api.services.whisper_service import WhisperTranscription

transcribe_route = APIRouter()
whisper_client = WhisperTranscription(model_size="base")

@transcribe_route.post("/transcribes")
async def transcribes(file: UploadFile = File(...)):
    try:
        data = await file.read()
        result = whisper_client.transcribe(data, filename=file.filename or "audio.m4a")
        return {"ok": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
