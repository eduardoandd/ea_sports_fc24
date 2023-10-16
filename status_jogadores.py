import pandas as pd
from requests import get
from bs4 import BeautifulSoup


url='https://sofifa.com/player/'
browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

df=pd.read_csv('jogadores_eafc24.csv')
list_id=[]
list_id=df['Id'].tolist()
list_url=[]
list_player_status= []

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
    
    

    try:
        ul_class_pl = soup.find('ul', class_='pl').find_all('li')
        #Pé bom
        dict_stats['Pé bom']=ul_class_pl[0].text.split('foot')[1] 
    except:
        dict_stats['Pé bom'] = None
        print('Excessão acionada')
        continue
    
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
    
    stats = soup.find_all('div', class_='col col-12')[1].find_all('div', class_='block-quarter')
    
    
    for i in range(len(stats)):
        
        status_select = stats[i].find_all('li')
        
        if i == 7:
            list_playstyles=[]
            if not list_playstyles:
                dict_stats['playstyles']='Não possui'
            else:
                [list_playstyles.append(statu.text) for statu in status_select]
                dict_stats['playstyles']=list_playstyles
                
        else:
  
            for statu in status_select:
                
                separador = statu.text.split(' ')
            
                if len(separador) > 2:
                    compost_stats = ' '.join(separador[-2:]).replace('\n','')
                    dict_stats[compost_stats]=separador[0]
                else:
                    dict_stats[separador[1].replace('\n','')]=separador[0]

    list_player_status.append(dict_stats)
    
df_stats = pd.DataFrame(list_player_status)
df_stats.to_csv('stats_jogadores_eafc24.csv', index=False)

    
    
        
        
    
    
    
    
    
    
    
    
    
    








