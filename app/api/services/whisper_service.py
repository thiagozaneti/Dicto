# app/api/services/openai_service.py
from faster_whisper import WhisperModel
import tempfile

class WhisperTranscription:  
    def __init__(self, model_size: str = "large-v3"):
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def transcribe(self, data: bytes, filename: str = "audio.m4a", language: str = "pt") -> dict:
        """
        Recebe bytes de áudio e retorna texto + segmentos com tempo.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=filename) as tmp:
            tmp.write(data)
            tmp.flush()
            path = tmp.name

        segments, info = self.model.transcribe(path, language=language)

        result = {
            "language": info.language,
            "duration": info.duration,
            "segments": []
        }

        for seg in segments:
            result["segments"].append({
                "id": seg.id,
                "start": seg.start,
                "end": seg.end,
                "text": seg.text.strip()
        })

        return result
