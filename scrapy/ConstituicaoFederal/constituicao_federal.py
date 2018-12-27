#Scrapy feito em 12/12

import requests, sqlite3, psycopg2
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from datetime import date, datetime

conn = sqlite3.connect('../../db.sqlite3', check_same_thread=False)
#conn = psycopg2.connect('postgres://gumpusaddqrkcg:3894ca3d0276a4ed486e2435681c8da47bd6eae270322a5a4b532ad320f4cc80@ec2-54-235-156-60.compute-1.amazonaws.com:5432/d2p9n2h48bq3sj')

with open('cfederal.html', 'rb') as f:
#with open('/app/scrapy/ConstituicaoFederal/cfederal.html', 'rb') as f:    
    soup = BeautifulSoup(f, 'html.parser')
for tag in soup.findAll():
    if tag.name in ['a', 'strike']:
      tag.decompose()

i = 0
is_titulo = False
allp = soup.findAll('p')
for p in allp:
    nonBreakSpace = u'\xa0'
    result = p.text#.replace('\n', '').replace(nonBreakSpace, '')  
    curs = conn.cursor()
    if len(result) > 5:     
        if p.span != None:   
            if p.span["style"]=="text-transform: uppercase":       
                is_titulo = True            
        elif p.get('align') == 'CENTER':
             is_titulo = True               
        else:
             result = p.text.replace('\n', '').replace(nonBreakSpace, '')  

        curs.execute("INSERT INTO leis_artigo ( artigo, created_at, updated_at, lei_id, id_artigo_lei, is_titulo) values (?, ?, ?, ?, ?, ?)", (result, date.today(), date.today(),  '1' , i, is_titulo))
        #curs.execute("INSERT INTO leis_artigo ( artigo, created_at, updated_at, lei_id, id_artigo_lei, is_titulo) values (%s, %s, %s, %s, %s, %s)", (result, date.today(), date.today(),  '1' , i, is_titulo))

        is_titulo = False
        i = i+1 
conn.commit()


