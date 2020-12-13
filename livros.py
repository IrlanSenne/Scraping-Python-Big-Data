import requests 
from bs4 import BeautifulSoup

sl = open('biblia-kjv.json','a+',encoding='utf8')
sl.write('{')
livros= ['https://www.bibliaonline.com.br/kjv/gn','https://www.bibliaonline.com.br/kjv/ex',
        'https://www.bibliaonline.com.br/kjv/lv','https://www.bibliaonline.com.br/kjv/nm',
        'https://www.bibliaonline.com.br/kjv/dt','https://www.bibliaonline.com.br/kjv/js',
        'https://www.bibliaonline.com.br/kjv/jz','https://www.bibliaonline.com.br/kjv/rt',
        'https://www.bibliaonline.com.br/kjv/1sm','https://www.bibliaonline.com.br/kjv/2sm',
        'https://www.bibliaonline.com.br/kjv/1rs','https://www.bibliaonline.com.br/kjv/2rs',
        'https://www.bibliaonline.com.br/kjv/1cr','https://www.bibliaonline.com.br/kjv/2cr',
        'https://www.bibliaonline.com.br/kjv/ed','https://www.bibliaonline.com.br/kjv/ne',
        'https://www.bibliaonline.com.br/kjv/et','https://www.bibliaonline.com.br/kjv/jó',
        'https://www.bibliaonline.com.br/kjv/sl','https://www.bibliaonline.com.br/kjv/pv',
        'https://www.bibliaonline.com.br/kjv/ec','https://www.bibliaonline.com.br/kjv/ct',
        'https://www.bibliaonline.com.br/kjv/is','https://www.bibliaonline.com.br/kjv/jr',
        'https://www.bibliaonline.com.br/kjv/lm','https://www.bibliaonline.com.br/kjv/ez',
        'https://www.bibliaonline.com.br/kjv/dn','https://www.bibliaonline.com.br/kjv/os',
        'https://www.bibliaonline.com.br/kjv/jl','https://www.bibliaonline.com.br/kjv/am',
        'https://www.bibliaonline.com.br/kjv/ob','https://www.bibliaonline.com.br/kjv/jn',
        'https://www.bibliaonline.com.br/kjv/mq','https://www.bibliaonline.com.br/kjv/na',
        'https://www.bibliaonline.com.br/kjv/hc','https://www.bibliaonline.com.br/kjv/sf',
        'https://www.bibliaonline.com.br/kjv/ag','https://www.bibliaonline.com.br/kjv/zc',
        'https://www.bibliaonline.com.br/kjv/ml',

        'https://www.bibliaonline.com.br/kjv/mt','https://www.bibliaonline.com.br/kjv/mc',
        'https://www.bibliaonline.com.br/kjv/lc','https://www.bibliaonline.com.br/kjv/jo',
        'https://www.bibliaonline.com.br/kjv/atos','https://www.bibliaonline.com.br/kjv/rm',
        'https://www.bibliaonline.com.br/kjv/1co','https://www.bibliaonline.com.br/kjv/2co',
        'https://www.bibliaonline.com.br/kjv/gl','https://www.bibliaonline.com.br/kjv/ef',
        'https://www.bibliaonline.com.br/kjv/fp','https://www.bibliaonline.com.br/kjv/cl',
        'https://www.bibliaonline.com.br/kjv/1ts','https://www.bibliaonline.com.br/kjv/2ts',
        'https://www.bibliaonline.com.br/kjv/1tm','https://www.bibliaonline.com.br/kjv/2tm',
        'https://www.bibliaonline.com.br/kjv/tt','https://www.bibliaonline.com.br/kjv/fm',
        'https://www.bibliaonline.com.br/kjv/hb','https://www.bibliaonline.com.br/kjv/tg',
        'https://www.bibliaonline.com.br/kjv/1pe','https://www.bibliaonline.com.br/kjv/2pe',
        'https://www.bibliaonline.com.br/kjv/1jo','https://www.bibliaonline.com.br/kjv/2jo',
        'https://www.bibliaonline.com.br/kjv/3jo','https://www.bibliaonline.com.br/kjv/jd',
        'https://www.bibliaonline.com.br/kjv/ap'
    ]
num = 0
while (num < len(livros)):
    num2=1
    capitulos = livros[num]
    reqCapitulos = requests.get(capitulos)
    soupCapitulos =BeautifulSoup(reqCapitulos.content,'html.parser')
    lenCap = soupCapitulos.find('ul').find_all('a')
    titulo = soupCapitulos.find('h1',{ "class":"MuiTypography-root MuiTypography-h1"})
    print(titulo.get_text())
    sl.write('\n  "'+ titulo.get_text() +'": [')
    while (num2 <= len(lenCap)):
        sl.write('{ \n        "v":[ \n')
        urlLivros=livros[num]+'/'+str(num2)
        reqLivros = requests.get(urlLivros)
        soupLivros = BeautifulSoup(reqLivros.content,'html.parser')
        linkLivros = soupLivros.find('article').find_all('p')  
        numVer= 1        
        for s in soupLivros.find_all('sup'):
            s.clear() 
        for versiculo in linkLivros:
            if (numVer == len(soupLivros.find_all('sup')) and num2 == len(lenCap) and (num + 1) == len(livros)):
                completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text().replace("\"","'") + '" }\n]}] \n '
                sl.write(completo)
                numVer += 1
            elif (numVer == len(soupLivros.find_all('sup')) and num2 == len(lenCap)):
                completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text().replace("\"","'") + '" }\n]}], \n '
                sl.write(completo)
                numVer += 1  
            elif (numVer == len(soupLivros.find_all('sup'))):
                completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text().replace("\"","'") + '" }\n]}, \n '
                sl.write(completo)
                numVer += 1                
            else:
                completo = '           { "num": ' + str(numVer) + ', "t": "' + versiculo.get_text().replace("\"","'") + '" },\n'
                sl.write(completo)
                numVer += 1   
        num2 += 1 
    num += 1        
sl.write('\n }')
sl.close()
    
   
        
        
            

    





