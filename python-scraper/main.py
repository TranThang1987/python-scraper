import requests
from bs4 import BeautifulSoup

URL = "https://www.tangthuvien.net/"

def fetch_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.text.strip()
        print(f"Trang chủ: {title}")
    else:
        print("Lỗi khi lấy dữ liệu!")

if __name__ == "__main__":
    fetch_data()
