from requests_html import HTMLSession
# O PROGRAMA ACESSSA A PÁGINA E NOS RETONA TODOS OS LINKS DA 
# TAG a DA CLASSE canditate-submenu-item

# A função find faz parte da propriedade html da resposta da função get 
# O find recebe como parâmetro a tag a e classe com o nome stretched-link
# A propriedade html possui várias funções para o navegador do HTML 
url ='https://www.empregos.com.br'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.candidate-submenu-item")
for link in links:
    print(link.attrs['href'])
    # print(link.attrs['href'])#Todo elemento extraido da função find,
# tem uma propriedade chamada "attrs"
# (é um dicionário que contém todos os atributos Html) neste 
# códogo utilizamos o strrs para extrair todos os hrefs de cada link. 
    