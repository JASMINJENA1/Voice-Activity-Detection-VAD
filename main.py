from fastapi import FastAPI, File, UploadFile, HTTPException
import webrtcvad
from pydub import AudioSegment
import io

app = FastAPI()
vad = webrtcvad.Vad(3)  # Level of aggressiveness: 0-3

def perform_vad(audio_bytes):
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="wav")
    samples = audio.get_array_of_samples()
    sample_rate = audio.frame_rate

    raw_audio = samples.tobytes()
    frame_duration = 30  # ms
    frame_length = int(sample_rate * frame_duration / 1000 * audio.sample_width)
    
    is_speech = []
    for i in range(0, len(raw_audio), frame_length):
        frame = raw_audio[i:i+frame_length]
        if len(frame) == frame_length:
            is_speech.append(vad.is_speech(frame, sample_rate))
    
    return is_speech

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["audio/wav", "audio/x-wav"]:
        raise HTTPException(status_code=400, detail="Only WAV files are supported.")
    audio_bytes = await file.read()
    vad_results = perform_vad(audio_bytes)
    return {"vad_results": vad_results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




