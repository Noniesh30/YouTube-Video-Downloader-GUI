import tkinter as tk
from tkinter import messagebox
from directory import directory_select
from valid import is_valid_youtube_link
from mine import download_youtube_video


def download_link():
    global link
    link = entry.get()
    test_link=is_valid_youtube_link(link)
    if test_link:
        open_quality_window()
    else:
        messagebox.showwarning("Error", "Please enter a valid link")

def open_quality_window():

    def download_trans():
        selected_quality = video_quality.get()
        print(f"Selected Video Quality: {selected_quality}")
        global link
        downloading(link,selected_quality)
    
    quality_window = tk.Toplevel(window)
    quality_window.title("Select Video Quality")
    label = tk.Label(quality_window, text="Select Video Quality")
    label.pack(pady=10)
    video_quality = tk.StringVar()
    radio_360p = tk.Radiobutton(quality_window, text="360p", variable=video_quality, value='360p')
    radio_720p = tk.Radiobutton(quality_window, text="720p", variable=video_quality, value='720p')
    radio_1080p = tk.Radiobutton(quality_window, text="1080p", variable=video_quality, value='1080p')
    radio_2160p = tk.Radiobutton(quality_window, text="2160p", variable=video_quality, value='2160p')

    radio_360p.pack(pady=5)
    radio_720p.pack(pady=5)
    radio_1080p.pack(pady=5)
    radio_2160p.pack(pady=5)
    
    ok_button = tk.Button(quality_window, text="OK", command=download_trans)
    ok_button.pack(pady=10)

def downloading(link,quality):
    window.destroy() 
    path=directory_select()
    messagebox.showinfo("Download", f"Downloading from link: {link}\n Resolution:{quality}\n Path:{path}")
    download_youtube_video(link,path,quality)
    


window = tk.Tk()
window.title("Download Link GUI")
label = tk.Label(window, text="To download Youtube, paste the link below:")
label.pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(pady=10)
download_button = tk.Button(window, text="Download", command=download_link)
download_button.pack(pady=10)
window.mainloop()
