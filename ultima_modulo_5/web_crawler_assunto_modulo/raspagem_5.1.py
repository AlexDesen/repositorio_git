import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sqlite3

# O PROGRAMA ACESSA A PÁGINA EXTRAIR OS DADOS E COLOCALOS EM UM BANCO DE DADOS.

# a função *find_element, ela recebe algumas opções, a primeira é o tipo de busca do elemento 
# (no nosso caso indicamos que queremos buscar pelo texto do link) e em seguida o valor a ser buscado: Tempo Real.
# Quando a função *link.click é chamada e o selenium passa para o webDriver que deseja clicar no elemento 
# e este passa para o navegador.

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
sql = 'INSET INTO noticias(titulo, data, descricao) value(?, ?, ?)'
navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get('https://ultima.school/?utm_source=google&utm_medium=cpc&utm_campaign=brand&utm_content=brand&utm_term=%22ultima_school%22&utm_name=responsive_03&gad=1&gclid=Cj0KCQjwlumhBhClARIsABO6p-zAWHRt7U9FjMZQpsnIQjNTFBesyBV0roLqFm_B1MD9ja67Kui8FnQaAlV9EALw_wcB')
link = navegador.find_element(By.LINK_TEXT,'Estude de graça')
link.click()
time.sleep(7)
for noticia in navegador.find_element(By.CSS_SELECTOR, 'div.position-relative'):
    titulo = noticia.find_element(By.TAG_NAME,'h3').text
