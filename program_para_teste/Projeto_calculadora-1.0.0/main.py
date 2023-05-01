# comando para resolver comflitos - git rebase <no da branch>
#  e resolvido o conflito git rebase --continue 
# Comando para vizualizar branch - git branch
# Deletando branch local - git  branch -D <nome da branch>
# Deletando branch  remoto - git push origin:<nome da branch>
from CALCULADORA.operacoes_simples import soma
from CALCULADORA.operacoes_simples import subtracao 


print("CALCULADORA")
if __name__ =="__main__":
    opcao = 1
    while opcao != 3:
       
        print(30*("="))
        print('1 - SOMA')
        print("2-SUBTRAÇÃO")
        print("3 - SAIR")
        print(30*("="))
        opcao = int(input("OPCAO: "))

        if opcao == 1:           
            argumento1 = int(input("Agumrnto 1: "))
            argumento2 = int(input("Agumrnto 2: "))
            resultado = soma(argumento1, argumento2)
            print(f"O resultado da soma é:{resultado}")
            print()
        elif opcao == 2:
            argumento1 = int(input("Agumrnto 1: "))
            argumento2 = int(input("Agumrnto 2: "))
            resultado1 = subtracao(argumento1, argumento2)
            print(f"O resultado da soma é:{resultado1}")
            print() 
        elif opcao == 3:
            print("OBRIGADO POR USAR A NOSSA  CALCULADORA: ")