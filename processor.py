import os
import requests
from moviepy.editor import VideoFileClip

API_KEY = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path):
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    files = {"file": open(file_path, "rb")}
    data = {"model": "whisper-1"}
    response = requests.post(url, headers=headers, files=files, data=data)
    return response.json()["text"]

def process_video_pipeline(video_path):
    print("Transcribing audio...")
    transcript = transcribe_audio(video_path)

    print("Creating clips...")
    video = VideoFileClip(video_path)
    duration = video.duration

    segments = [
        (0, min(30, duration)),
        (30, min(60, duration))
    ]

    for i, (start, end) in enumerate(segments):
        clip = video.subclip(start, end)
        clip = clip.resize(height=1920).crop(width=1080, x_center=clip.w/2)
        clip.write_videofile(f"clip_{i}.mp4", codec="libx264")
