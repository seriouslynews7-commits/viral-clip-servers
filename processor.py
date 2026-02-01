import os
from moviepy.editor import VideoFileClip
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

def transcribe_audio_from_video(video_path):
    audio_path = "temp_audio.wav"

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file
        )

    os.remove(audio_path)
    return transcript.text


def process_video_pipeline(video_path):
    print("Transcribing audio...")
    transcript = transcribe_audio_from_video(video_path)
    print("Transcript:", transcript)

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

    print("Done.")
