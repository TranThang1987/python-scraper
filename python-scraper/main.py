import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_URL = "https://truyenchu.com.vn/tim-kiem"

def get_story_chapters(story_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    # Gửi yêu cầu tìm kiếm truyện
    params = {"q": story_name}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return {"error": f"Lỗi HTTP {response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Lấy danh sách truyện kết quả
    results = soup.select(".list-truyen .item-truyen a")
    
    if not results:
        return {"error": "Không tìm thấy truyện!"}

    # Lấy URL của truyện đầu tiên
    first_story_url = "https://truyenchu.com.vn" + results[0]["href"]

    # Gửi yêu cầu lấy chi tiết truyện
    response = requests.get(first_story_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        chapter_count = soup.select_one(".truyen-detail .so-chuong").text.strip()
    except AttributeError:
        chapter_count = "Không rõ số chương"

    return {
        "story_name": story_name,
        "chapter_count": chapter_count,
        "story_url": first_story_url
    }

@app.route("/search", methods=["GET"])
def search_story():
    story_name = request.args.get("name")
    
    if not story_name:
        return jsonify({"error": "Vui lòng nhập tên truyện!"}), 400
    
    data = get_story_chapters(story_name)
    return jsonify(data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Lấy PORT từ biến môi trường Railway
    print(f"🚀 Đang chạy trên cổng: {port}")  # Kiểm tra PORT đang nhận
    app.run(host="0.0.0.0", port=port, debug=True)


