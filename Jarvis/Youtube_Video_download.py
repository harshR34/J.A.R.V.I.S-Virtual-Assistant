from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.first()  # Get the highest resolution stream
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example video URL
save_location = "/path/to/save/location"  # Example save location

download_video(video_url, save_location)
