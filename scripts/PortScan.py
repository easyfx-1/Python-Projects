# Python Port Scanner (TCP Connect)

## Funcionalidades
- Scan TCP Connect
- Suporte a IPv4
- Suporte a domínios e endereços IP
- Timeout
- Exibição das portas abertas
- Medição do tempo de execução

## Tecnologias
- Python 3
- Socket



import socket
from datetime import datetime

print('PortScanner by easy_dev\n')

ip = input('Digite o IP ou endereço do alvo: ')

inicio = datetime.now()

for porta in range(1,1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    resultado = sock.connect_ex((ip,porta))
    
    if resultado == 0:
        print(f'Porta TCP aberta: {porta}')
    
    sock.close()

fim = datetime.now()

print(f'inicio: {inicio} -- Fim:{fim}')
print(f'tempo estimado: {fim - inicio}')
