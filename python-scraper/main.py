import requests
from bs4 import BeautifulSoup

URL = "https://truyenchu.com.vn/"  # Cập nhật trang web mới

def fetch_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.text.strip()
            print(f"Trang chủ: {title}")
        else:
            print(f"Lỗi HTTP {response.status_code} khi truy cập {URL}")
    
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    fetch_data()
