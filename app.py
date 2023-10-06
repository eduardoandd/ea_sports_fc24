import requests
from bs4 import BeautifulSoup

url = 'https://sofifa.com/'
browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

page= requests.get(url,headers=browser)
response=page.text

soup=BeautifulSoup(response,'html.parser')


names_players=soup.find('td', class_= 'col-name').div.get_text()


