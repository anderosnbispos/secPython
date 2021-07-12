import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexao falou!!! {}'.format(e))
        sys.exit(1)

    print("Socket criado")

    host = input("Digite o host ou ip: ")
    porta = input("Digite a porta: ")

    try:
        s.connect((host, int(porta)))
        s.settimeout(10.0)
        print("Cliente TCP conectado, no host: {} e porta: {}!"
              .format(host,porta))
        s.shutdown(2)
    except socket.error as e:
        print('A conexao falou!!! {}'.format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()