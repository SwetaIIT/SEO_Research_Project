#Using Supadata API to extract transcript from youtube 
import os
from supadata import Supadata

API_KEY = os.getenv("SUPADATA_API_KEY")

supadata = Supadata(api_key=API_KEY)

VIDEO_URLS = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2"
]

OUTPUT_DIR = "research/youtube-transcripts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_transcript(video_url, index):
    try:
        result = supadata.transcript(url=video_url, lang="en")

        transcript_text = result.get("content", str(result))

        file_path = f"{OUTPUT_DIR}/video_{index}.txt"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"URL: {video_url}\n\n")
            f.write(transcript_text)

        print("Saved:", file_path)

    except Exception as e:
        print("Error:", e)

for i, url in enumerate(VIDEO_URLS, start=1):
    fetch_transcript(url, i)
