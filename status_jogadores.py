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
count=0
excessoes=0

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
    count+=1
    print(count)
    print('-----------')
    print(id)
    
    #NOME JOGADOR - VAI PEGAR O VALOR DA LINHA DO DF DA COLUNA NOME
    dict_stats['Nome'] = df[(df['Id']==id)]['Nome'].values[0]

    try:
        #Pé bom
        ul_class_pl = soup.find('ul', class_='pl').find_all('li')
        dict_stats['Pé bom']=ul_class_pl[0].text.split('foot')[1] 
        #gavi nonetype 
    except:
        dict_stats['Pé bom'] = None
        print('Excessão acionada')
        excessoes+=1 
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
    
    #PAC
    pac_stats= stats[0].find_all('li')
    for statu in pac_stats:
        separador = statu.text.split(' ')
        
        if len(separador) > 2:
            compost_stats = ' '.join(separador[-2:]).replace('\n','')
            dict_stats[compost_stats]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
   
    #Chute
    sho_stats = stats[1].find_all('li')
    for statu in sho_stats:
        separador = statu.text.split(' ')
        
        if len(separador) > 2:
            compost_stats = ' '.join(separador[-2:]).replace('\n','')
            dict_stats[compost_stats]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
     
    #LOGICA ANTIGA   
    # dict_stats['Finalização']=sho_stats[0].text.split(' ')[0]
    # dict_stats['Posicionamento']=sho_stats[1].text.split(' ')[0]
    # dict_stats['Força do Chute']=sho_stats[2].text.split(' ')[0]
    # dict_stats['Chute de Longe']=sho_stats[3].text.split(' ')[0]
    # dict_stats['Penaltis']=sho_stats[4].text.split(' ')[0]
    # dict_stats['Voleio']=sho_stats[4].text.split(' ')[0]
    
    #PASS
    pas_stats = stats[2].find_all('li')
    for statu in pas_stats:
        separador = statu.text.split(' ')

        #Lógica necessária caso seja um status composto
        if len(separador) > 2:
            compost_stats=" ".join(separador[-2:]).replace('\n','')
            dict_stats[compost_stats]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
        
    #DRIBLE
    dri_stats = stats[3].find_all('li')
    for statu in dri_stats:
        separador = statu.text.split(' ')
        
        #Lógica necessária caso seja um status composto
        if len(separador) > 2:
            compost_stat=" ".join(separador[-2:]).replace('\n','')
            dict_stats[compost_stat]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
            
    #DEFESA
    def_stats= stats[4].find_all('li')
    for statu in def_stats:
        separador = statu.text.split(' ')
        
        if len(separador) > 2:
            compost_stats= " ".join(separador[-2:]).replace('\n', '')
            dict_stats[compost_stat]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
                    
    #FISICO
    phy_stats=stats[5].find_all('li')
    for statu in phy_stats:
        separador = statu.text.split(' ')
        
        if len(separador) > 2:
            compost_stats= " ".join(separador[-2:]).replace('\n', '')
            dict_stats[compost_stat]=separador[0]
        else:
            dict_stats[separador[1].replace('\n','')]=separador[0]
        
    #PLAYSTYLES
    playstyles=[style.text for style in stats[7].find_all('li') if len(stats[7].find_all('li')) > 1]
    dict_stats['PlayStyles'] = playstyles
    
    list_player_status.append(dict_stats)
    

df_stats = pd.DataFrame(list_player_status)
df_stats.to_csv('stats_jogadores_eafc24.csv', index=False)
print(f'Número de excessões {excessoes}')
    
    
        
        
    
    
    
    
    
    
    
    
    
    








