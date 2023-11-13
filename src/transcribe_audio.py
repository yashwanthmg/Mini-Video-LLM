from google.cloud import speech_v1p1beta1 as speech
from moviepy.video.io.VideoFileClip import VideoFileClip


def transcribe_video(video_path):
    client = speech.SpeechClient()

    # Extract audio from video
    video = VideoFileClip(video_path)
    video.audio.write_audiofile("temp_audio.wav")

    # Transcribe the audio
    with open("temp_audio.wav", "rb") as audio_file:
        content = audio_file.read()

    audio_config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=44100,
        language_code="en-US",
        audio_channel_count = 2,
    )

    response = client.recognize(
        audio=speech.RecognitionAudio(content=content),
        config=audio_config,
    )

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript + " "

    return text.strip()

# Example usage
video_path = "C:/Users/Home/Videos/SQLshort.mp4"  # Update with your video path
transcribed_text = transcribe_video(video_path)
print("Transcribed Text:", transcribed_text)