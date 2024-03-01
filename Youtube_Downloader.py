import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist

def download_single_video():
    url = single_video_entry.get()
    output_path = single_output_path.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def download_playlist():
    url = playlist_entry.get()
    output_path = playlist_output_path.get()
    try:
        playlist = Playlist(url)
        for video in playlist.video_urls:
            yt = YouTube(video)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path)
        messagebox.showinfo("Success", "Playlist download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_output_path():
    path = filedialog.askdirectory()
    single_output_path.set(path)
    playlist_output_path.set(path + "/Playlist")

# Create main window
root = tk.Tk()
root.title("YouTube Downloader")

# Single Video Download Section
single_frame = tk.LabelFrame(root, text="Single Video Download")
single_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

single_video_label = tk.Label(single_frame, text="Video URL:")
single_video_label.grid(row=0, column=0, padx=5, pady=5)

single_video_entry = tk.Entry(single_frame, width=50)
single_video_entry.grid(row=0, column=1, padx=5, pady=5)

single_output_label = tk.Label(single_frame, text="Output Path:")
single_output_label.grid(row=1, column=0, padx=5, pady=5)

single_output_path = tk.StringVar()
single_output_entry = tk.Entry(single_frame, width=40, textvariable=single_output_path)
single_output_entry.grid(row=1, column=1, padx=5, pady=5)

single_output_button = tk.Button(single_frame, text="Browse", command=browse_output_path)
single_output_button.grid(row=1, column=2, padx=5, pady=5)

single_download_button = tk.Button(single_frame, text="Download", command=download_single_video)
single_download_button.grid(row=2, column=1, padx=5, pady=5)

# Playlist Download Section
playlist_frame = tk.LabelFrame(root, text="Playlist Download")
playlist_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

playlist_label = tk.Label(playlist_frame, text="Playlist URL:")
playlist_label.grid(row=0, column=0, padx=5, pady=5)

playlist_entry = tk.Entry(playlist_frame, width=50)
playlist_entry.grid(row=0, column=1, padx=5, pady=5)

playlist_output_label = tk.Label(playlist_frame, text="Output Path:")
playlist_output_label.grid(row=1, column=0, padx=5, pady=5)

playlist_output_path = tk.StringVar()
playlist_output_entry = tk.Entry(playlist_frame, width=40, textvariable=playlist_output_path)
playlist_output_entry.grid(row=1, column=1, padx=5, pady=5)

playlist_output_button = tk.Button(playlist_frame, text="Browse", command=browse_output_path)
playlist_output_button.grid(row=1, column=2, padx=5, pady=5)

playlist_download_button = tk.Button(playlist_frame, text="Download", command=download_playlist)
playlist_download_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
