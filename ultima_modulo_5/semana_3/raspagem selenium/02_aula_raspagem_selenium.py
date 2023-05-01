'''
Através do selnium iremos dar o comanodo para o navegador acessar 
um determinado url.
'''


import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# O web driver fará o meio de campo entre o selenium e o navegador.
# "A ferramenta selenium silmula a atuação do usuário no navegador"
# Lebrano que cada navegador tem sua particularidades em renderizar as páginas.
# Essas difirenças hoje são poucas mais existem.
# Cada navegador tem o seu driver o driver que iremos usar é o chromeDriverManager
# que é o driver do navegador chrome ele é resposável por realizar a pote entre
# o selenium e o navegador atuando como um interpretador traduzindo os comandos
# enviando os comandos do selenium para o navegador. 
# Cada navegador possui o seu driver popularmente chamando de "enjaine"


opcoes = Options()
'''Usamos a função add_argument('--headless') com o objetivo de não abrir a tela do navegador '''
opcoes.add_argument('--headless')# Esse método impede que a tela do navegador abra
navegador = Chrome(service=Service(ChromeDriverManager().install()),options=opcoes) # "equivale a sessão do requests"
navegador.set_window_size(1280, 1080) # aumentando o tamanho da janela 
navegador.maximize_window()# maximizando o tamnaho da janela


'''O código vista a página da olx, printa a página inicial,aplica um time de 1 segundo,
    em seguida clica no butão "Entra", direcionado a página de referência realiza um segundo printe.
    Logo em seguida preechemos os campos de email e senha da página referêciada e logo após realizamos
    o terceiro printe.
'''
navegador.get('https://www.olx.com.br/')
time.sleep(1)# esse time é importante para a renderização
navegador.save_screenshot('pagina_inicial.png')# Esse método printa a tela navegada
buton = navegador.find_element(By.LINK_TEXT,'Entrar')#By.LINK_TEXT irá buscar por qualquer link com nome 'Entrar' na tela do navegador
buton.click()
time.sleep(1)
navegador.save_screenshot('sem_preenchimento.png')

campo_email = navegador.find_element(By.ID,'input-1')#campo de e-mail a ser preechido na página web
campo_senha = navegador.find_element(By.ID,'password-input')#campo de senha a ser preenchido na página web

# preechimento dos campos e-mail/senha
campo_email.send_keys('alexnevestrade@gmail.com')
campo_senha.send_keys('1234567890')
navegador.save_screenshot('campos_preechidos.png')
entrar = navegador.find_element(By.CLASS_NAME,'sc-LKuAh bdWxIJ')
entrar.click()
time.sleep(1)
navegador.save_screenshot('resultado.preenchido.png')
navegador.close()
