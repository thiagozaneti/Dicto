from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os


class OpenAITranscription:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise RuntimeError("API_KEY não encontrado no ambiente/.env")

        self.client = OpenAI(api_key=self.api_key)

    def transcribe(self, audio_path: str, language: str = "pt"):
        """
        Recebe o caminho para o arquivo de áudio e retorna o texto + segmentos.
        """
        path = Path(audio_path)
        if not path.exists():
            raise FileNotFoundError(f"Áudio não encontrado: {path}")

        with path.open("rb") as f:
            result = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                response_format="verbose_json",
                timestamp_granularities=["segment"],
                language=language,
            )

        return result
    
    
if __name__ == "__main__":
    api = OpenAITranscription()
    result = api.transcribe(r"C:\Users\Thiago\Documents\Projetos\Dicto\Dicto\apps\api\dicto_api\asr\gra4.m4a")

    print("\n=== TEXTO COMPLETO ===")
    print(result.text)

    print("\n=== SEGMENTOS ===")
    
word_amount = 0
letter_number = 0

for seg in result.segments:
    print(f"[{seg.start:.2f}s - {seg.end:.2f}s] {seg.text}")

    #contar palavras 
    words = seg.text.strip().split()
    word_amount += len(words)

    #contar letras 
    for char in seg.text:
        if char and not char.isspace():
            letter_number += 1

print(f"\nTotal de palavras: {word_amount}")
print(f"Total de letras: {letter_number}")
