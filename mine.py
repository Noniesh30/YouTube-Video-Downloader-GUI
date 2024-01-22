from pytube import YouTube
import os
from tkinter import messagebox

def download_youtube_video(url, output_path, resolution):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4', resolution=resolution).first()
        if video:
            output_file = os.path.join(output_path, video.default_filename)
            video.download(output_path)
            messagebox.showinfo(f"Download successful! Saved to: {output_file}")
        else:
            messagebox.showinfo("No video available with the specified resolution.")
    except Exception as e:
        messagebox.showinfo(f"Download failed: {str(e)}")

