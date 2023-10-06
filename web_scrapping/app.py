#APRENDENDO A EXTRAIR DADOS DO SOFIFA.COM
from bs4 import BeautifulSoup

with open('teste.html', 'r') as file:
    conteudo = file.read()
    
ex = BeautifulSoup(conteudo, 'lxml')

tags=ex.find_all(class_='h')

for tag in tags:
    print(tag.text)

