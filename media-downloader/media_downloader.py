from fileinput import filename
import os
import ffmpeg
from pytube import YouTube
import pytube.exceptions as pte
import tkinter as tk
from tkinter import messagebox

desktop_path = os.path.normpath(os.path.expanduser("~/Desktop"))

#! YT PART START


def get_media(video_url, media_type, video_quality):
    try:
        yt = YouTube(video_url)
        video_title = yt.title

        if media_type == "Audio":
            print(yt.streams.filter(only_audio=True))
            yt.streams.get_audio_only().download()
        elif video_quality == "720p":
            yt.streams.filter(
                res="720p", mime_type="video/mp4", progressive=True
            ).first().download()
        else:
            yt.streams.get_audio_only().download(filename="audio.mp3")
            audio = ffmpeg.input("audio.mp3")
            if video_quality == "Highest":
                yt.streams.filter(adaptive=True).order_by(
                    "resolution"
                ).desc().first().download(filename="video.mp4")

                video = ffmpeg.input("video.mp4")
                ffmpeg.concat(video, audio, v=1, a=1).output(
                    f"{video_title}({yt.streams.filter(adaptive=True).order_by('resolution').desc().first().resolution}).mp4"
                ).run(overwrite_output=True)

                if os.path.exists("video.mp4") and os.path.exists("audio.mp3"):
                    os.remove("video.mp4")
                    os.remove("audio.mp3")
                else:
                    "Error with deleting merged files"

            elif video_quality == "1080p":
                yt.streams.filter(
                    res="1080p", mime_type="video/mp4", adaptive=True
                ).first().download(filename="video.mp4")

                video = ffmpeg.input("video.mp4")
                ffmpeg.concat(video, audio, v=1, a=1).output(
                    f"{video_title}(1080p).mp4"
                ).run(overwrite_output=True)

                if os.path.exists("video.mp4") and os.path.exists("audio.mp3"):
                    os.remove("video.mp4")
                    os.remove("audio.mp3")
                else:
                    "Error with deleting merged files"

            elif video_quality == "720p":
                yt.streams.filter(
                    res="720p", mime_type="video/mp4", progressive=True
                ).first().download()

    except pte.RegexMatchError:
        print("Regex match error. Invalid URL.")
    except pte.VideoPrivate:
        print("Video is private.")
    except pte.VideoRegionBlocked:
        print("Video is blocked in your region.")
    except pte.VideoUnavailable:
        print("Video is unavailable.")
    except pte.PytubeError as e:
        print(f"A Pytube error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


get_media(
    "https://www.youtube.com/watch?v=w2IhccXakkE&ab_channel=PoloGVEVO",
    "Video",
    "1080p",
)
#! YT PART END

# class DownloaderGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.configure(bg="#a83434")
#         self.label = tk.Label(self.root, text="YouTube Downloader", font=("Arial", 19))
#         self.label.pack(padx=10, pady=10)

#         self.url_box = tk.Entry(self.root, width=50, font=("Arial", 16))
#         self.url_box.bind("<KeyPress>", self.shortcut)
#         self.url_box.insert(0, "Paste your URL here")
#         self.url_box.pack(padx=10, pady=10)

#         self.checkState = tk.StringVar(self.root, "Download Video (720p)")
#         self.checkState.set("Video")

#         self.video_option = tk.Radiobutton(
#             self.root,
#             text="Download Video (720p)",
#             value="Video",
#             variable=self.checkState,
#         ).pack()

#         self.audio_option = tk.Radiobutton(
#             self.root,
#             text="Download Audio ONLY",
#             value="Audio",
#             variable=self.checkState,
#         ).pack()

#         self.download_button = tk.Button(
#             self.root, text="Download File", font=("Arial", 18), command=self.download
#         )
#         self.download_button.pack(padx=10, pady=10)

#         self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
#         self.root.mainloop()

#     def download(self):
#         pass

#     def shortcut(self, event):
#         if event.state == 4 and event.keysym == "Return":
#             self.download()

#     def onClosing(self):
#         if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
#             self.root.destroy()

#     def clear(self):
#         self.url_box.delete("1.0", tk.END)


# DownloaderGUI()
