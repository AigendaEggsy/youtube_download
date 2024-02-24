import yt_dlp

class YouTubeDownloader:
    def __init__(self):
        self.download_path = '%(title)s.%(ext)s'

    def download_video(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': self.download_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return filename