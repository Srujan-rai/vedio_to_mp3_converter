from pytube import YouTube
import moviepy.editor as mp
import os

def download_youtube_audio(video_url, output_path):
    try:

        if not os.path.exists(output_path):
            os.makedirs(output_path)


        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=output_path)

        video_file = mp.VideoFileClip(os.path.join(output_path, f"{yt.title}.mp4"))
        audio_file_path = os.path.join(output_path, f"{yt.title}.mp3")
        video_file.audio.write_audiofile(audio_file_path)

        os.remove(os.path.join(output_path, f"{yt.title}.mp4"))

        return audio_file_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
video_url = input("enter the vedio url : ")
output_directory = 'mp3/'

audio_file = download_youtube_audio(video_url, output_directory)
if audio_file:
    print(f"Audio file downloaded: {audio_file}")
else:
    print("Failed")
