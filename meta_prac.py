import requests
from bs4 import BeautifulSoup

url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%83%89%EC%A1%B0%ED%99%94%EC%9E%A5%ED%92%88&pagingIndex=1&pagingSize=40&productSet=total&query=색조화장품&viewType=thumb'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.


title=soup.select_one('#\35 611904751 > a > dl > dd > div > div.name')





print(title)

