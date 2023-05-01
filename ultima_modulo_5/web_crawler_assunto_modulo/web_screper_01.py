'''
Scriping: extrair dados estruturado de fontes não estruturadas.
Crawler: visitações em páginas.
E o somatório do Scriping com o Crawler = web screper

A sessão(HTMLSession) possui os métodos http o método get é um deles 
'''
'''
Observações: usar os comando tab + F3 para realizar pesquisa
'''

# O código se trata de um programa que visita o site e retorna com o valar do 
# dolar do dia.


from requests_html import HTMLSession

# url ='https://www.melhorcambio.com/dolar-hoje'
# sessao = HTMLSession()
# resposta = sessao.get(url)
# campo = '#taxa-comercial'
# dolar = resposta.html.find(campo,first=True)
# print(dolar)
# print(dolar.attrs['value'])# *attrs - É um dicionário "dos atributos de cada elemento" contendo o value,
# # type etc



url= 'https://www.olx.com.br/imoveis/estado-ba/sul-da-bahia'
sessao = HTMLSession()
resposta = sessao.get(url)
for link in resposta.html.find('#ad-list li a'):
    print(link.attrs['href'])


