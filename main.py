import os
import requests
from bs4 import BeautifulSoup
from pydub import AudioSegment

# query를 변환하는 함수
def getQuery(query_raw):
    return query_raw.replace(' ', '%20')

# YouGlish에서 video src를 추출하는 함수
def getVideofrom(url, time_interval):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # video 태그에서 src 속성 추출
    video_src = soup.find('video', class_='video-stream')['src']
    
    # blob URL 처리 필요 시 yt-dlp나 ffmpeg 사용
    video_data = requests.get(video_src, stream=True)
    temp_file = "temp_video.mp4"
    
    with open(temp_file, 'wb') as f:
        for chunk in video_data.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    # 10초 오디오 추출
    audio = AudioSegment.from_file(temp_file)
    clip = audio[:time_interval * 1000]  # ms 단위

    os.remove(temp_file)  # 임시 파일 삭제
    return clip

# 오디오 저장 함수
def save(audio, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    audio.export(filepath, format="mp3")

# 실행 예시
query_raw = "hello world"
query = getQuery(query_raw)
print(query)
audio = getVideofrom(url=f"https://youglish.com/pronounce/{query}/english", time_interval=10)
save(audio, f'./audio/{query}.mp3')
