# O PROGRAMA ACESSA E EXTRAI DADOS DO SITE DA GOOGLE IMPRIMINDUOS JUNTO COM O STATUS CODE

# para realizar instalações de bibliotecas utilizando o 
# instalador pip é necessário ' utilizar a nomeclatura da versão do pip'.
# Exemplo: pip3.11 <mais nome da bibliot>

from requests_html import HTMLSession
url = 'https://www.google.com.br'
sessao = HTMLSession() # Aqui abrimos uma sessão,"tipo um navegador."
resposta = sessao.get(url) # Usamos o método get da sessão
print(resposta.text) # Conteúdo retornado
print(resposta.status_code)