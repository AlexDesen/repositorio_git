import socket
HOST = '127.0.0.1'
PORT = 9000
print('Iniciando socket')
s = socket.socket()
print('Conectando com o servidor')
s.connect((HOST,PORT)) # Inicia-se a conexão
texto = "Ola mundo"
print("Enviando o texto")
s.sendall(texto.encode('utf-8')) # Transforma em binário
dados = s.recv(1024) # Envia os primeiros 1024 bits
s.close()
texto = dados.decode('utf-8')
print(f"Cliente: recebi {texto}")