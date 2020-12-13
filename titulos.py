import requests
from bs4 import BeautifulSoup

sl = open('titulosArray.jon','a+',encoding='utf8')
livros= ['https://www.bibliaonline.com.br/acf/gn','https://www.bibliaonline.com.br/acf/ex',
        'https://www.bibliaonline.com.br/acf/lv','https://www.bibliaonline.com.br/acf/nm',
        'https://www.bibliaonline.com.br/acf/dt','https://www.bibliaonline.com.br/acf/js',
        'https://www.bibliaonline.com.br/acf/jz','https://www.bibliaonline.com.br/acf/rt',
        'https://www.bibliaonline.com.br/acf/1sm','https://www.bibliaonline.com.br/acf/2sm',
        'https://www.bibliaonline.com.br/acf/1rs','https://www.bibliaonline.com.br/acf/2rs',
        'https://www.bibliaonline.com.br/acf/1cr','https://www.bibliaonline.com.br/acf/2cr',
        'https://www.bibliaonline.com.br/acf/ed','https://www.bibliaonline.com.br/acf/ne',
        'https://www.bibliaonline.com.br/acf/et','https://www.bibliaonline.com.br/acf/jó',
        'https://www.bibliaonline.com.br/acf/sl','https://www.bibliaonline.com.br/acf/pv',
        'https://www.bibliaonline.com.br/acf/ec','https://www.bibliaonline.com.br/acf/ct',
        'https://www.bibliaonline.com.br/acf/is','https://www.bibliaonline.com.br/acf/jr',
        'https://www.bibliaonline.com.br/acf/lm','https://www.bibliaonline.com.br/acf/ez',
        'https://www.bibliaonline.com.br/acf/dn','https://www.bibliaonline.com.br/acf/os',
        'https://www.bibliaonline.com.br/acf/jl','https://www.bibliaonline.com.br/acf/am',
        'https://www.bibliaonline.com.br/acf/ob','https://www.bibliaonline.com.br/acf/jn',
        'https://www.bibliaonline.com.br/acf/mq','https://www.bibliaonline.com.br/acf/na',
        'https://www.bibliaonline.com.br/acf/hc','https://www.bibliaonline.com.br/acf/sf',
        'https://www.bibliaonline.com.br/acf/ag','https://www.bibliaonline.com.br/acf/zc',
        'https://www.bibliaonline.com.br/acf/ml',

        'https://www.bibliaonline.com.br/acf/mt','https://www.bibliaonline.com.br/acf/mc',
        'https://www.bibliaonline.com.br/acf/lc','https://www.bibliaonline.com.br/acf/jo',
        'https://www.bibliaonline.com.br/acf/atos','https://www.bibliaonline.com.br/acf/rm',
        'https://www.bibliaonline.com.br/acf/1co','https://www.bibliaonline.com.br/acf/2co',
        'https://www.bibliaonline.com.br/acf/gl','https://www.bibliaonline.com.br/acf/ef',
        'https://www.bibliaonline.com.br/acf/fp','https://www.bibliaonline.com.br/acf/cl',
        'https://www.bibliaonline.com.br/acf/1ts','https://www.bibliaonline.com.br/acf/2ts',
        'https://www.bibliaonline.com.br/acf/1tm','https://www.bibliaonline.com.br/acf/2tm',
        'https://www.bibliaonline.com.br/acf/tt','https://www.bibliaonline.com.br/acf/fm',
        'https://www.bibliaonline.com.br/acf/hb','https://www.bibliaonline.com.br/acf/tg',
        'https://www.bibliaonline.com.br/acf/1pe','https://www.bibliaonline.com.br/acf/2pe',
        'https://www.bibliaonline.com.br/acf/1jo','https://www.bibliaonline.com.br/acf/2jo',
        'https://www.bibliaonline.com.br/acf/3jo','https://www.bibliaonline.com.br/acf/jd',
        'https://www.bibliaonline.com.br/acf/ap']

num = 0
while (num < len(livros)):
    capitulos = livros[num]
    reqCapitulos = requests.get(capitulos)
    soupCapitulos =BeautifulSoup(reqCapitulos.content,'html.parser')
    titulo = soupCapitulos.find('h1',{ "class":"MuiTypography-root MuiTypography-h1"})
    sl.write('{ l: "'+str(num)+'",\n livro: '+'"'+ titulo.get_text() +'" },')
    num += 1