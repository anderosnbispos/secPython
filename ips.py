import ipaddress

ip = '192.168.30.57/28'

net = ipaddress.ip_network(ip, strict=False)

for ip in net:
    print(ip)