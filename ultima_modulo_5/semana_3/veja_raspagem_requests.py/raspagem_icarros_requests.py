import sqlite3
from requests_html import   HTMLSession

# url = 'https://www.icarros.com.br/ache/estoque.jsp?id=1858856'
# sessao = HTMLSession()
# resposta = sessao.get(url)
# carros = []
# for link in resposta.html.find('a.clearfix'):
    # print(link.attrs['href'])
    # url_carros = link.attrs['href']
    # print(url_carros)
    # print(url_carros)
    # resposta_icarro = sessao.get(url_carros)# Acesssando a página
    # print(resposta_icarro)
    # ano = resposta_icarro.html.fint('').text
    # print(ano)
    
    
    
url = 'https://veja.abril.com.br/economia'
sessao = HTMLSession()
resposta = sessao.get(url)
carros = []
# apontamos a div pelo seu seletor
# apontamos a primeira tag "a" dentro da div através do indice[0] e 
# o h2 dentro da primeira tag

# a = resposta.html.find('div.col-s-12 a h2')[0] 
# print(a.text)

# for link in resposta.html.find('div.col-s-12 a h2'):  
#        print(link.text)

for link in resposta.html.find('div.col-s-12 a'):  
       print(link.attrs['href'])[1]
    
    
    

    