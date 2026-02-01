import os
from moviepy.editor import VideoFileClip
from openai import OpenAI

import os
from moviepy.editor import VideoFileClip
from openai import OpenAI

client = OpenAI()   # ← CHANGE THIS LINE
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
