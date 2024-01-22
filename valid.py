from pytube import YouTube

def is_valid_youtube_link(link):
    try:
        # Attempt to create a YouTube object
        yt = YouTube(link)
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False
