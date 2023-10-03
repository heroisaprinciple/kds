import moviepy.editor

def read_audio_from_video(video, audio_output):
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    audio.write_audiofile(audio_output)

read_audio_from_video("lab1vid.mp4", "audio.mp3")
