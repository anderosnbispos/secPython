import os
import time

def ping_simples():
    print("#" * 60)
    ip_ou_host = input('Digite o IP ou Host: ')
    print(type(ip_ou_host))
    os.system('ping -c 4 {}'.format(ip_ou_host))
    print("#" * 60)


def ping6():
    host = input('Digite o nome ou Host: ')
    os.system('ping6 -c 4 {}'.format(host))

def ping_multiplo():
    # file = open('./hosts.txt','r')
    # ips = file.read()
    # lista_ips = ips.split('\n')
    # qtd_ips = len(lista_ips)
    # for x in range(qtd_ips):
    #     print(lista_ips[x])
    # file.close()
    with open('hosts.txt') as file:
        dump = file.read()
        dump = dump.splitlines()
        for ip in dump:
            os.system('ping -c2 {}'.format(ip))
            time.sleep(5)
        file.close()


if __name__ == '__main__':
    # ping_simples()
    # ping6()
    ping_multiplo()
