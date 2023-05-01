
'''Programa que acessa capitura os dados da página olx.'''
# primeira etapa do programa: buscar todos os links
# segundo etapa: acessar as páginas dos imóveis e capiture os dados
  
# Utilizando xpef - "o xpef é como se fosse o sql do html", realizar consulta
# em uma página web.

''' *O programa quando incluo o comando da linha 22 esta gerando um erro.  '''

import sqlite3
from requests_html import HTMLSession

url = 'https://www.olx.com.br/imoveis/estado-ba/grande-salvador '

sessao = HTMLSession()
resposta = sessao.get(url)
imovel = []
for link in resposta.html.find('#ad-list li a'):# "apontamos o caminho de onde estar a nossa href"
    url_imovel = link.attrs['href']
    resposta_imovel = sessao.get(url_imovel)# acessando a página
    print(resposta_imovel)
    
    # print(url_imovel)
    # titulo = resposta_imovel.html.find('h1',first=True).text # Imprimindo o texto de dentro da h1.
    # preco = resposta_imovel.html.find('h2')[2].text 
    # print(resposta_imovel)

    '''Imprimindo o dicionário somente com  a url e o título deveido a um erro que ocorre quando eu incluo o preço.'''
    # imovel.append({
    #     'url': url_imovel,
    #     'titulo': titulo,
        # 'preco': preco
#    })
# print(imovel)

# conexao = sqlite3.connect('banco.sqlite3')
# cursor = conexao.cursor()
# sql = 'INSERT INTO  anuncio (url, titulo) values(?,?);'
# for  imoveis in imovel:
#     valores = [ imoveis['url'], imoveis['titulo']]
#     cursor.execute(sql, valores)
# conexao.commit()
# conexao.close()    
    



