import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://sofifa.com/'
browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

page= requests.get(url,headers=browser)
response=page.text

soup=BeautifulSoup(response,'html.parser')

list_player= []
cont=0

for line in soup.find_all('tr'):
    
    if cont > 1:
        
        dict_player= {}
        
        ref_player = line.find('td', class_='col-name')
        
        #ID JOGADOR
        dict_player['Id'] = ref_player.a.get('href').split('/')[2]

        #NOME JOGADOR
        dict_player['Nome'] = ref_player.a.text
        
        #POSIÇÃO JOGADOR
        player_positions=ref_player.find_all('span')
        positions=[]
        for position in range(len(player_positions)):
            if len(positions) <= len(player_positions):
                positions.append(player_positions[position].text)
                dict_player['Posições']= positions
            else: break
            
        #NACIONALIDADE (BANDEIRA)
        dict_player['Nacionalidade']=ref_player.find('img').get('data-src')
        
        #IDADE
        dict_player['Idade']=line.find('td',class_='col col-ae').text
        
        #OVER
        dict_player['Overral']=line.find('td',class_='col col-oa').text
        
        #POTENTIAL
        dict_player['Potential']=line.find('td',class_='col col-pt').text

        #TIME E CONTRATO
        team_contrat=line.find_all('td', class_='col-name')[1]
        
        dict_player['Time']=team_contrat.find('a').text
        dict_player['Time(Bandeira)']=line.find_all('td', class_='col-name')[1].find('img').get('data-src')
        
        dict_player['Tempo de Contrato']=team_contrat.find('div',class_='sub').text.split('\n')[1]
        
        #VALOR
        dict_player['Valor']=line.find('td', class_='col col-vl').text
        
        #SALARIO
        dict_player['Salário']=line.find('td',class_='col col-wg').text
        
        #STATUS TOTAIS
        dict_player['Status totais']=line.find('td','col col-tt').text
        
        list_player.append(dict_player)
        
        df = pd.DataFrame(list_player)
        df
    
    cont +=1
        


    
    
    


