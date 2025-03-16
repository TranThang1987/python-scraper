import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_URL = "https://truyenchu.com.vn/tim-kiem"

def get_story_chapters(story_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    params = {"q": story_name}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return {"error": f"Lỗi HTTP {response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Kiểm tra danh sách truyện trả về
    results = soup.select(".list-truyen .item-truyen a")
    
    if not results:
    return {"error": "Không tìm thấy truyện!"}

