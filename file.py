import json
import requests 
from bs4 import BeautifulSoup
import lxml

urlLivros='https://www.bibliaonline.com.br/acf/sl/113'
reqLivros = requests.get(urlLivros)
soupLivros = BeautifulSoup(reqLivros.content,'html.parser')
linkLivros = soupLivros.find('article').find_all('p')
#-----------Apenas teste ... Pegar do array pronto-------------
urlTitulo='https://www.bibliaonline.com.br/acf/lc'
reqTitulo= requests.get(urlTitulo)
soupTitulo = BeautifulSoup(reqTitulo.content,'html.parser')
#-------------------------------------------------------------------
titulo = soupTitulo.find('h1',{ "class":"MuiTypography-root MuiTypography-h1"})

sl = open('salmos.json','a+',encoding='utf8')
sl.write('{ \n "'+ titulo.get_text() +'": [')
numVer=1
numCap = 50
numTeste =1
while numTeste < numCap:
     sl.write('{ \n        "v":[ \n')
     while (numVer < len(soupLivros.find_all('sup'))):
          for s in soupLivros.find_all('sup'):
               s.clear()
          for versiculo in linkLivros:
               if (numVer == len(soupLivros.find_all('sup'))):
                    completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text() + '" }\n'
                    sl.write(completo)
               else:
                    completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text() + '" },\n'
                    sl.write(completo)
                    numVer += 1
     numTeste += 1
     sl.write(']}, \n ')
sl.write('\n ]}')
sl.close()
    



