import os
from moviepy.editor import VideoFileClip
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


def transcribe_audio_from_video(video_path):
    audio_path = "temp_audio.wav"

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()  # 🔥 IMPORTANT

    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file
        )

    o
