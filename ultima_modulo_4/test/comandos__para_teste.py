# *"O pytest levará em considerção os returns e não os prints"
# NOMEAR OS TEST DE FORMA MAIS ESPECÍFICA POSSÍVEL - FACILITA NA HORA 
# DE INDENTIFICAR UM ERRO  
# Modularizar um código = "colocar um código dentro da função"
# Aplicamos o comando pytest dentro da pasta onde esta o arquivo para realizarmos o test 
#                                   OU
# Comando para test mais detalhados: pytest --vv (retorna nome do test e a porcentagem)
# Comando para verificar a cobertura de teste: pytest -vv --cov <nome_aquivo.py>
# Outro comando para a visualização de cobertura:
# pytest --cov <nome do arquivo sem test_ e a terminação .py> --cov-report term-missing
# o term-missing esta relacionada com alguma parte que não esteja coberta.
 
# TDD(test driven development)-desenvolvimento voltado a test -primeiro se
# desenvolve os testes para criar as funções que irão ser testadas.
from aplicacao import imprime_email

def test_imprime_email():
    assert imprime_email('Carlos', 'Drumond') == 'Carlos.Drumond@email.com.br'

# class test_cadastro:
#     def test_imprime_email(self):
#         assert imprime_email(self)
#         self.aplicacao = cadastro('Carlos', 'Unberto')
        