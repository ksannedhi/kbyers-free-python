import random

def ip_addr(base_ip = "10.10.10."):
    ip = base_ip + str(random.randint(1, 255))
    return ip

print("IP address: ", ip_addr())
print("IP address: ", ip_addr("172.20.123."))
print("IP address: ", ip_addr(base_ip="192.168.200."))