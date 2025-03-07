import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def download_video(url, output_path, format_choice):
    """Download a single video with the chosen format."""
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': format_choice if format_choice != 'best' else 'best',
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def choose_directory():
    """Open a dialog for selecting the output directory."""
    folder_selected = filedialog.askdirectory()
    return folder_selected if folder_selected else os.getcwd()

def start_download():
    """Start the download process based on user's selection."""
    url = simpledialog.askstring("Enter URL", "Enter the YouTube URL:")
    if not url:
        messagebox.showwarning("Input Error", "URL cannot be empty.")
        return
    
    output_path = choose_directory()
    
    download_type = simpledialog.askstring(
        "Download Type", "Enter 'video' for a single video, 'playlist' for a playlist, 'channel' for all videos, or 'audio' for audio-only:")
    if not download_type:
        return
    
    format_choice = 'best'
    if download_type == 'video':
        format_choice = simpledialog.askstring(
            "Choose Format", "Enter quality (best, 1080p, 720p, audio only):", initialvalue="best"
        )
        if format_choice == 'audio only':
            download_type = 'audio'
    
    if download_type == 'video':
        download_video(url, output_path, format_choice)
    elif download_type == 'playlist':
        download_video(url, output_path, 'best')  # Can be extended for playlist
    elif download_type == 'channel':
        download_video(url, output_path, 'best')  # Can be extended for channel
    elif download_type == 'audio':
        download_video(url, output_path, 'bestaudio')
    else:
        messagebox.showwarning("Invalid Input", "Invalid download type selected.")

# Set up the GUI
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")

start_button = tk.Button(root, text="Start Download", command=start_download, width=20, height=2)
start_button.pack(pady=40)

root.mainloop()
