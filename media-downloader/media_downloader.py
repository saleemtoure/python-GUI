import os
from pytube import YouTube
from pytube.exceptions import *
import tkinter as tk
from tkinter import messagebox

desktop_path = os.path.normpath(os.path.expanduser("~/Desktop"))


class DownloaderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#a83434")
        self.label = tk.Label(self.root, text="YouTube Downloader", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.url_box = tk.Entry(self.root, width=50, font=("Arial", 16))
        self.url_box.bind("<KeyPress>", self.shortcut)
        self.url_box.insert(0, "Paste your URL here")
        self.url_box.pack(padx=10, pady=10)

        self.checkState = tk.StringVar(self.root, "Download Video (720p)")
        self.checkState.set("Video")

        self.video_option = tk.Radiobutton(
            self.root,
            text="Download Video (720p)",
            value="Video",
            variable=self.checkState,
        ).pack()

        self.audio_option = tk.Radiobutton(
            self.root,
            text="Download Audio ONLY",
            value="Audio",
            variable=self.checkState,
        ).pack()

        self.download_button = tk.Button(
            self.root, text="Download File", font=("Arial", 18), command=self.download
        )
        self.download_button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.mainloop()

    def download(self):
        try:
            # video_url = self.url_box.get()
            video_url = (
                "https://www.youtube.com/watch?v=-qu-txgwsiA&ab_channel=ShowTimeNorge"
            )
            yt = YouTube(video_url)

            video_kvaliteter = list(yt.streams.filter(progressive=True))
            lyd_kvaliteter = list(yt.streams.filter(only_audio=True))
            print(video_kvaliteter)
            print(lyd_kvaliteter)
        except RegexMatchError:
            print("Regex match error. Invalid URL.")
        except VideoPrivate:
            print("Video is private.")
        except VideoRegionBlocked:
            print("Video is blocked in your region.")
        except VideoUnavailable:
            print("Video is unavailable.")
        except PytubeError as e:
            print(f"A Pytube error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.download()

    def onClosing(self):
        if messagebox.askyesno(title="Quit?", message="Vil du virkelig avslutte"):
            self.root.destroy()

    def clear(self):
        self.url_box.delete("1.0", tk.END)


DownloaderGUI()
