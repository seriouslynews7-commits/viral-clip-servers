import whisper
from moviepy.editor import VideoFileClip

def process_video_pipeline(video_path):

    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    transcript = result["segments"]

    video = VideoFileClip(video_path)

    for i, seg in enumerate(transcript[:5]):
        start, end = seg["start"], seg["end"]
        clip = video.subclip(start, end)
        clip = clip.resize(height=1920).crop(width=1080, x_center=clip.w/2)
        clip.write_videofile(f"clip_{i}.mp4", codec="libx264")
