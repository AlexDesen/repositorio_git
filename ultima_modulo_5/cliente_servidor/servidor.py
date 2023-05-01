# socket é a biblioteca direcionada a forma mais básica de comunicação client-servidor 
# IP 127.0.0.1 é o IP da própria máquina
# O bind é a função que "aponta o IP e a porta" do nosso servidor local 
# with é uma estrutura que basicamente não permite que a conexão fique aberta.


import socket

HOST = "127.0.0.1"
PORT = 9000
print("INICIANDO O SOCKET")
s = socket.socket()
s.bind((HOST,PORT))
print('ESCUTANDO')
s.listen() # deste ponto o código fica aguardando solicitação do cliente na porta 9000.
conexao, endereco = s.accept() # Aceite da comunicação
# Enquanto a conexão estiver ativar será lido o que foi enviado da conexão.
with conexao:
    print(f'Nova conxão{endereco}')
    while True:
        dados = conexao.recv(1024) # Ocorre a leitura dos primeiros 1024 bits
        if not dados:
            break
        texto = dados.decode('utf-8') # esses 1024 bits são transformados em str
        print(f'Servidor: Recebi {texto}')
        conexao.sendall(texto.encode('utf-8')) # Reenviando bits em binário para o cliente.
s.close()

