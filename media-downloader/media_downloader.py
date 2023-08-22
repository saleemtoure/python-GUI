from asyncio import exceptions
import os
from re import S
from pytube import YouTube as yt
import pytube.exceptions as ptExceptions
import tkinter as tk
from tkinter import E, messagebox

desktop_path = os.path.normpath(os.path.expanduser("~/Desktop"))

# video = yt("https://www.youtube.com/watch?v=-qu-txgwsiA")

# print(video.streams.filter(file_extension="mp4", progressive=True))

# video.streams.get_by_itag(22).download(output_path=desktop_path)


class YoutubeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#a83434")
        self.label = tk.Label(self.root, text="YouTube Downloader", font=("Arial", 19))
        self.label.pack(padx=10, pady=10)

        self.url_box = tk.Entry(self.root, width=50, font=("Arial", 16))
        self.url_box.bind("<KeyPress>", self.shortcut)
        self.url_box.insert(0, "Paste your URL here")
        self.url_box.pack(padx=10, pady=10)
        self.video = ""
        self.video_title = self.video.title
        self.video_itag = 0

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
        # try:#!Catching error not working (trying to catch an exception if other text then url entered)
        #     url = self.url_box.get()
        # except ptExceptions.RegexMatchError:
        #     print("URL Error. Try again")

        try:
            video_url = self.url_box.get()
        except ptExceptions.PytubeError as PE:
            # if str(PE) == "{caller}: could not find match for {pattern}":
            #     print("LØØl")
            print(repr(PE))
        else:
            self.video = yt(video_url)
            print(self.video.title)
        # if len(self.url_box.get()) == 0 or self.url_box.get() == "Paste your URL here":
        #     print("No URL inserted. Try again")
        # else:
        #     self.video = yt(self.url_box.get())

        # if self.checkState.get() == "Video":
        #     print(f"Downloading video: '{self.video.title}'")
        # else:
        #     print(f"Downloading audio from video: '{self.video.title}'")

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.download()

    def onClosing(self):
        if messagebox.askyesno(title="Quit?", message="Vil du virkelig avslutte"):
            self.root.destroy()

    def clear(self):
        self.url_box.delete("1.0", tk.END)


YoutubeGUI()
