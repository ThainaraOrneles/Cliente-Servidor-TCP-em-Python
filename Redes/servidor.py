#módulo socket
import socket

#tamanho maximo da mensagem
tam = 2048

#variálvel recebe o número da porta
PORT = 80

#Na variável s é passando por parametro os atributos socket.AF_INET e socket.SOCK_STREAM
#AF_INET é a familia de endereços sendo ele o IPv4 
#SOCK_STREAM é o tipo de socket e é usando para identificar uma interface TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# o bind Víncula o endereço do HOST obtido e o PORT
#O gethostname() possibilita que o servidor fique visível em qualquer computador
s.bind((socket.gethostname(), PORT))

# O listen fica aguardando o cliente se conectar com o servidor
s.listen()
print("Aguardando conexao...")

#as variáveis recebem os dados da conexão e o endereço do cliente
conn, ender = s.accept()

#printa o endereço
print("Conectado em ", ender)


while True:
    #variável recebe as mensagens transmitidas com um determinado tamanho em bits
    msg = conn.recv(tam)
    #se não tiver dados a conexão é fechada
    if not msg:
        print("Fechando a conexao")
        conn.close()
        break
    #envia todos os dados para o cliente
    conn.sendall(msg)
