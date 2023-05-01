'''
Através do selnium iremos dar o comanodo para o navegador acessar 
um determinado url.
'''

# WebDriver é uma ferramenta que simula as ações do usuário e repassa para
# o navegador, como repassa para o navegador o estado atual dele.
# o WebDriver fará a ponte entre o navegador e o selenium.
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get('https://ultima.school/?utm_source=google&utm_medium=cpc&utm_campaign=brand&utm_content=brand&utm_term=%22ultima_school%22&utm_name=responsive_03&gad=1&gclid=Cj0KCQjwlumhBhClARIsABO6p-zAWHRt7U9FjMZQpsnIQjNTFBesyBV0roLqFm_B1MD9ja67Kui8FnQaAlV9EALw_wcB')
time.sleep(7)
navegador.close()