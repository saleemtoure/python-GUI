import os
from pytube import YouTube
import pytube.exceptions as pte
from moviepy.editor import AudioFileClip, VideoFileClip, CompositeAudioClip
import tkinter as tk
from tkinter import NORMAL, ttk, messagebox, filedialog
import sv_ttk

desktop_path = os.path.normpath(os.path.expanduser("~/Desktop"))


class DownloaderGUI:
    def __init__(self):
        self.root = tk.Tk()
        sv_ttk.set_theme("dark")

        self.root.maxsize(800, 450)
        self.root.minsize(800, 250)

        self.root.title("YouTube Downloader - github.com/saleemtoure")
        self.label = ttk.Label(self.root, text="YouTube Downloader", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.theme_button = ttk.Button(
            self.root, text="Toggle Dark Mode", command=sv_ttk.toggle_theme
        )
        self.theme_button.pack(padx=10, pady=10)

        self.url_box = ttk.Entry(self.root, width=60, font=("Arial", 16))
        self.url_box.insert(0, "Paste your URL here")
        self.clicked = self.url_box.bind("<Button-1>", self.click)
        self.url_box.pack(padx=10, pady=10)

        self.checkState = tk.StringVar(self.root, "Download Video")
        self.checkState.set("Video")

        self.dropdown = ttk.Combobox(
            state="readOnly",
            values=[
                "Video (Highest Quality available)",
                "1080p",
                "720p",
                "Only Audio (Highest Quality available)",
            ],
            width=35,
        )
        self.dropdown.current(1)
        self.dropdown.pack(padx=10, pady=10)

        self.checkbox_state = tk.IntVar()
        self.checkbox = tk.Checkbutton(
            text="Choose where to save file (Default: Desktop)",
            variable=self.checkbox_state,
        )
        self.checkbox.pack(padx=10, pady=10)

        self.path_label = ttk.Label(self.root, text=f"Downloading to: Desktop")
        self.path_label.pack(padx=10, pady=10)

        self.download_button = ttk.Button(
            self.root,
            text="Download File",
            # font=("Arial", 18),
            command=lambda: self.download_media(
                self.url_box.get(),
                self.dropdown_select()[0],
                self.dropdown_select()[1],
            ),
        )
        self.download_button.pack(padx=10, pady=10)

        self.progress = tk.IntVar(value=0)
        self.progress_label = ttk.Label(self.root, text=f"{0}%")
        self.progress_label.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.mainloop()

    def dropdown_select(self):
        selection = self.dropdown.get()
        if selection == "Video (Highest Quality available)":
            return "Video", "Highest"
        elif selection == "1080p":
            return "Video", "1080p"
        elif selection == "720p":
            return "Video", "720p"
        else:
            return "Audio", None

    def download_media(self, video_url, media_type, video_quality):
        out_path = ""
        temp_path = ""
        if self.checkbox_state.get() == 0:
            out_path = desktop_path
        else:
            temp_path = filedialog.askdirectory()
            if temp_path != "":  # Empty string
                out_path = temp_path
                self.path_label.configure(text=f"Downloading to: {out_path}")
            else:
                out_path = desktop_path
                self.path_label.configure(
                    text=f"No custom path chosen \n Downloading to: Desktop"
                )
        try:
            yt = YouTube(video_url)
            video_title = yt.title

            if media_type == "Audio":
                yt = YouTube(video_url, on_progress_callback=self.on_progress)
                file = yt.streams.get_audio_only()
                file.download()

                audio_mp4_file = AudioFileClip(f"{file.title}.mp4")
                audio_mp4_file.write_audiofile(f"{out_path}/{file.title}.mp3")

                if os.path.exists(f"{file.title}.mp4"):
                    os.remove(f"{file.title}.mp4")
                    self.on_finish()
                else:
                    "Error when deleting converted files"

            elif video_quality == "720p":
                yt = YouTube(video_url, on_progress_callback=self.on_progress)
                file = yt.streams.filter(
                    res="720p", mime_type="video/mp4", progressive=True
                ).first()
                file.download(filename=f"{out_path}/{video_title}(720p).mp4")
                self.on_finish()

            else:
                yt.streams.get_audio_only().download(
                    filename="audio.mp3", skip_existing=False
                )
                audio = CompositeAudioClip([AudioFileClip("audio.mp3")])

                if video_quality == "Highest":
                    yt = YouTube(video_url, on_progress_callback=self.on_progress)
                    file = (
                        yt.streams.filter(adaptive=True)
                        .order_by("resolution")
                        .desc()
                        .first()
                    )
                    file.download(filename="video.mp4", skip_existing=False)

                    video = VideoFileClip("video.mp4")
                    video.audio = audio
                    video.write_videofile(
                        f"{out_path}/{video_title}({yt.streams.filter(adaptive=True).order_by('resolution').desc().first().resolution}).mp4"
                    )

                    if os.path.exists(f"video.mp4") and os.path.exists("audio.mp3"):
                        os.remove("video.mp4")
                        os.remove("audio.mp3")
                        self.on_finish()
                    else:
                        "Error when deleting merged files"

                elif video_quality == "1080p":
                    yt = YouTube(video_url, on_progress_callback=self.on_progress)
                    file = (
                        yt.streams.filter(
                            res="1080p", mime_type="video/mp4", adaptive=True
                        )
                        .order_by("resolution")
                        .desc()
                        .first()
                    )

                    file.download(filename="video.mp4", skip_existing=False)

                    video = VideoFileClip("video.mp4")
                    video.audio = audio
                    video.write_videofile(f"{out_path}/{video_title}(1080p).mp4")

                    if os.path.exists(f"video.mp4") and os.path.exists("audio.mp3"):
                        os.remove("video.mp4")
                        os.remove("audio.mp3")
                        self.on_finish()
                    else:
                        "Error when deleting merged files"

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

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size * 100
        per = str(int(percentage))
        self.progress_label.configure(text=f"{per}%")
        if bytes_remaining == 0:
            self.progress_label.configure(text="Completed. Now converting")
        self.progress_label.update()

    def on_finish(self):
        self.progress_label.configure(text="Finished downloading and converting!")

    def click(self, event):
        self.url_box.configure(state=NORMAL)
        self.url_box.delete(0, tk.END)
        self.url_box.unbind("<Button-1>", self.clicked)

    def onClosing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
            self.root.destroy()


DownloaderGUI()
