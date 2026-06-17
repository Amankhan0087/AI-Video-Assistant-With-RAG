import yt_dlp
import imageio_ffmpeg
import subprocess
import os

DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True,
        "nopart": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        if info.get("requested_downloads"):
            downloaded = info["requested_downloads"][0]["filepath"]
        else:
            downloaded = ydl.prepare_filename(info)

    wav_path = os.path.splitext(downloaded)[0] + ".wav"
    subprocess.run(
        [FFMPEG_EXE, "-y", "-i", downloaded, "-ar", "16000", "-ac", "1", wav_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )

    if downloaded != wav_path and os.path.exists(downloaded):
        os.remove(downloaded)

    return wav_path


print(download_youtube_audio("https://youtu.be/BedAaB1RKgE?si=tWHnkr-YTzOZM9R1"))
