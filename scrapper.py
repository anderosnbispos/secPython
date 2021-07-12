# teste de ferramentas para webscrapping
# curso DIO - Python for Security

from bs4 import BeautifulSoup
import requests
import ipaddress

# objeto site recebendo o conteudo da requisicao http do siste...
site = requests.get("https://www.meuip.com.br/").content

# objeto soup esta baixando o html do site
soup = BeautifulSoup(site, 'html.parser')

# transforma o html em string e imprimpe
# print(soup.prettify())

txtip = soup.find("h3", class_="m-0 font-weight-bold")
ip = txtip.string.split()
# ip = ipaddress.ip_address(ip[3])
ip = ip[3]+"/32"
ip = print(ip)

# temperatura = soup.find("p", class_="-gray _flex _align-center")
# print(temperatura.prettify())

# print(soup.title)
# print(soup.title.string)
#
# print(soup.a)
# print(soup.p)

# print(soup.find('Temperatura'))