import requests
from bs4 import BeautifulSoup
import pickle

def crawl_phishtank_urls(start_id, end_id):
    base_url = "https://phishtank.org/target_search.php?target_id={id}&valid=y&active=y&Search=Search"
    total_phishing_urls = []

    for id in range(start_id, end_id + 1):
        url = base_url.format(id=id)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tất cả các hàng trong bảng
        rows = soup.find_all('tr')

        phishing_urls = []
        for row in rows[1:]:  # bỏ qua hàng tiêu đề
            columns = row.find_all('td')
            if len(columns) > 0:  # Kiểm tra có đủ cột không
                id_detail = columns[0].text.strip()  # Lấy ID

                # try catch

                base_url_detail = "https://phishtank.org/phish_detail.php?phish_id=" + id_detail
                response_detail = requests.get(base_url_detail)


                soup_detail = BeautifulSoup(response_detail.content, 'html.parser')

                phishing_url = soup_detail.find('div', class_='padded').find('span', style="word-wrap:break-word;").b.text


                phishing_urls.append(phishing_url)
        total_phishing_urls.append(phishing_urls)
    return total_phishing_urls

total_phishing_urls = crawl_phishtank_urls(0, 300)

with open("urls.data", "wb") as file:
    pickle.dump(total_phishing_urls, file)