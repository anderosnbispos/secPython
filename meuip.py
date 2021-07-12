from bs4 import BeautifulSoup
import requests

def meuip():
    # objeto site recebendo o conteudo da requisicao http do siste...
    site = requests.get("https://www.meuip.com.br/").content

    # objeto soup esta baixando o html do site
    soup = BeautifulSoup(site, 'html.parser')

    txtip = soup.find("h3", class_="m-0 font-weight-bold")
    ip = txtip.string.split()
    # ip = ipaddress.ip_address(ip[3])
    ip = ip[3]+"/32"
    ip = print(ip)

if __name__ == '__main__':
    meuip()