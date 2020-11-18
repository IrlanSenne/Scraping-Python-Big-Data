import json
import requests 
from bs4 import BeautifulSoup
import lxml

urlLivros='https://www.bibliaonline.com.br/acf/sl/113'
reqLivros = requests.get(urlLivros)
soupLivros = BeautifulSoup(reqLivros.content,'html.parser')
linkLivros = soupLivros.find('article').find_all('p')
sl = open('salmos.json','a+',encoding='utf8')
sl.write('{ \n "c1": { \n')
numVer=1
while (numVer < len(soupLivros.find_all('sup'))):
     for s in soupLivros.find_all('sup'):
          s.clear()
     for versiculo in linkLivros:
          completo = '"' + str(numVer) + '" : "' + versiculo.get_text() + '",\n'
          sl.write(completo)
          numVer += 1
sl.write('} \n }')     
               

     #versiculo_json = json.dumps(versiculo.get_text(),ensure_ascii=False).encode('utf-8')
     #completo = '{ '+ '"'+str(1)+'" : "' + versiculo.get_text() + '"},\n'
     #sl.write(completo)

sl.close()
    



