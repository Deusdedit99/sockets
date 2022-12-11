#Cliente.py 
import socket

 
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
 
# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)


print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')
 
# Recebendo a mensagem do usuário final pelo teclado
mensagem = input("Digite uma palavra ou frase curta para saber a tradução: ")
 
# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
    tcp.send(str(mensagem).encode())
    msg2 = tcp.recv(1024)
    print(msg2.decode())
    mensagem = input("Digite uma palavra ou frase curta para saber a tradução: ")
 
# Fechando o Socket
tcp.close()