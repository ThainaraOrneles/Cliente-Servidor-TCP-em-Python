#módulo socket
import socket

#tamanho maximo da mensagem
tam = 2048

#variálvel recebe o número da porta
PORT = 80

#Na variável s é passado por parametro os atributos socket.AF_INET e socket.SOCK_STREAM
#AF_INET é a familia de endereços sendo ele o IPv4 
#SOCK_STREAM é o tipo de socket e é usando para identificar uma interface TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#o connect faz a conexão com o servidor passando como o HOST e o PORT
s.connect((socket.gethostname(), PORT))

#A variável arquivo recebe os dados lidos do arquivo.txt
arquivo = open("arquivo.txt", "r")

for i in arquivo:
    #envia todos os dados para o servidor em forma de string
    s.sendall(str.encode(i))
    
arquivo.close()
#variável recebe os dados ecoados do servidor com um determinado tamanho em bits
msg = s.recv(tam)
s.close()
#printa a mensagem lida no arquivo
print("Mensagem ecoada: \n",msg.decode())
