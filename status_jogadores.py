import pandas as pd
from requests import get
from bs4 import BeautifulSoup


url='https://sofifa.com/player/'
browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

df=pd.read_csv('jogadores_eafc24.csv')

list_id=df['Id'].head(10).tolist()
list_url=[]


for id in list_id:
    url_with_id= f'{url}{id}/?attr=fut'
    list_url.append(url_with_id)

    for url_id in list_url:
        page = get(url_id,headers=browser)
        response= page.text
        soup=BeautifulSoup(response, 'html.parser')
        
    dict_stats= {}
    
    #ID JOGADOR
    dict_stats['Id_player']= id
    
    #NOME JOGADOR - VAI PEGAR O VALOR DA LINHA DO DF DA COLUNA NOME
    dict_stats['Nome'] = df[(df['Id']==id)]['Nome'].values[0]

    #Pé bom
    ul_class_pl = soup.find('ul', class_='pl').find_all('li')
    dict_stats['Pé bom']=ul_class_pl[0].text.split('foot')[1]
    
    #Skill Moves
    dict_stats['Estrela Skils']=ul_class_pl[1].text.split(' ')[0]
    
    #Perna ruim
    dict_stats['Estrela Perna ruim']=ul_class_pl[2].text.split(' ')[0]
    
    #Reputação internacional
    dict_stats['Reputação']=ul_class_pl[3].text.split(' ')[0]
    
    #Dedicação
    dict_stats['Dedicação']=ul_class_pl[4].text.split('rate')[1]
    
    #Tipo físico
    dict_stats['Body Type']= ul_class_pl[5].text.split('type')[1]
    
    
    #PAC
    stats = soup.find_all('div', class_='col col-12')[1].find_all('div', class_='block-quarter')
    dict_stats['Velocidade Final']=stats[0].li.text.split(' ')[0]
    dict_stats['Aceleração']=stats[1].li.text.split(' ')[0]
    
    #Chute
    sho_stats = stats[1].find_all('li')
    dict_stats['Finalização']=sho_stats[0].text.split(' ')[0]
    dict_stats['Posicionamento']=sho_stats[1].text.split(' ')[0]
    dict_stats['Força do Chute']=sho_stats[2].text.split(' ')[0]
    dict_stats['Chute de Longe']=sho_stats[3].text.split(' ')[0]
    dict_stats['Penaltis']=sho_stats[4].text.split(' ')[0]
    dict_stats['Voleio']=sho_stats[4].text.split(' ')[0]
    
    #PASS
    pas_stats = stats[2].find_all('li')
    
    for i in range(len(pas_stats)):
        split=pas_stats[i].text.split(' ')
        dict_stats[split[1].replace('\n','')]=split[0]
    
    
    
    
    
    
    
    
    
    








