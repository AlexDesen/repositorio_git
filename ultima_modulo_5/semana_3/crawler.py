from requests_html import HTMLSession
# Desafio: Extrair o que esta dentro dos links

url = 'https://www.empregos.com.br'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.candidate-submenu-item")
noticias = []
for link in links:
    url = '{}'.format(link.attrs['href'])
    resposta = sessao.get(url)
    infos = resposta.html.find('a.candidate-submenu-item') 
    
    # infos.append(noticias)
print(infos)  