import whisper
whisper_model = whisper.load_model("small")

response = whisper_model.transcribe("apps/api/dicto_api/asr/grav1.m4a",)
print(response)

