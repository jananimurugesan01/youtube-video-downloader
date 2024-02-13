from pytube import YouTube
def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True,file_extension='mp4').first()
        video.download()
        print("video has been downloaded..!")
    except Exception as e:
        print("Error:",str(e))
def download_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        print("Audio has been downloaded..!")
    except Exception as e:
        print("Error:",str(e))
if __name__ == "__main__":
    video_url = "https://youtu.be/EvMS73TWIQA?si=DTB3gwVHkl_YfrE1" 
    audio_url = "https://youtu.be/EvMS73TWIQA?si=DTB3gwVHkl_YfrE1"  
    download_video(video_url)
    download_audio(audio_url)

