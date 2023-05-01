from requests_html import HTMLSession
# O PROGRAMA ACESSA TODOS OS LINKS DA TEG a DA CLASSE stretched-link e 
# EXTRAIR DESSAS PÁGINAS OS DADOS NO FORMATO DO DICIONÁRIO da variável notícias abaixo.

# Pesquisando informações numa página html
# É NECESSÁRIO QUE MUDE O URL POIS O QUE CONSTA NO CÓDIGO ESTA DESATUALIZADO

url = 'https://www.raspagem.herokuapp.com/'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.stretched-link")
noticias = []
for link in links:
    url = 'https//www.rapagem.herokuapp.com{}'.format(link.attrs['href'])
    resposta = sessao.get(url)
    infos = resposta.html.find('.blog-post-meta span') 
    noticia = {
        'titulo':resposta.html.find('h1', first=True).text,
        'data': infos[0].text,
        'tags': infos[1].text,
        'texto':resposta.html.find('post-text',first=True).text,    
    }
    noticias.append(noticia)
print(noticias)                         