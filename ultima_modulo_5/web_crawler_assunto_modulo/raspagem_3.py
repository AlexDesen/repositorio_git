# O PROGRAMA ACESSA  A PÁGINA E RESGATA OS DADOS ATRAVÉS DA API. 

# Resulmo de uma página dinâmica:
# o código fonte do html é chamado na primeira solicitação e o restante
# do contúdo é preenchido após a página carrega. Através de chamada javascript
# para o servidor buscar dados de API'S.
# Essa é a essência de algumas ferramentas modernas em Javascript, 
# a página HTML inicial é simples e os elementos da página são 
# construídos dinamicamente buscando os dados de API 's.

# A selenium - ela atua na redenrização?

#o webdriver-manager, ele gerencia a instalação 
# (quando necessária) do WebDriver correspondente ao navegador que iremos utilizar. 
# WebDriver fará a ponte entre o navegador e o selenium.


from requests_html import HTMLSession

url = ' https://http//:www.raspagem.herokuapp.com/noticias/api/post/' 
sessao = HTMLSession()
resposta = sessao.get(url)
dados = resposta.json() # Traformando a nossa requisição em um dicionário
for dado in dados['results']:# retirando da chave results de duas outras chaves que estão dentro dela.
    print(dado['title'],'--', dado['headline'])
    
    
