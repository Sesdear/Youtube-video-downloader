from pytube import YouTube, exceptions
import customtkinter
import os
target_directory = "C:/youtube_videos/"
if not os.path.exists(target_directory):
    os.mkdir(target_directory)
class EntryWid(customtkinter.CTkEntry):
    def __init__(self, master):
        super().__init__(master, placeholder_text="Input your url", width=90, height=32)
        self.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
    def get_url(self):
        entry_msg = str(self.get())
        return entry_msg
class App(customtkinter.CTk):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("300x90")
        self.title("YouTube Video Downloader by HLNikNiky")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.entry_get = EntryWid(self)
        self.entry_get.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.button = customtkinter.CTkButton(self, text="Start", command=self.click_button)
        self.button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    def click_button(self):
        user_message = self.entry_get.get_url()
        try:
            yt = YouTube(user_message)
            video_streams = yt.streams.filter(res="1080p", file_extension="mp4").all()
            if not video_streams:
                print("Error: No FHD stream available.")
                return
            video = video_streams[0]
            download_location = os.path.join(os.getcwd(), target_directory)
            video.download(download_location)
        except exceptions.VideoUnavailable:
            print("Error: The video is unavailable.")
        except exceptions.PytubeError as e:
            print(f"Error: {e}")
if __name__ == '__main__':
    app = App(None)
    app.mainloop()