def ssh_conn(ip_addr, username, password):
    print("IP address:", ip_addr)
    print("Username:", username)
    print("Password", password)

print("-" * 60)
ssh_conn("192.168.20.23", "admin", "Testing@123")
print("-" * 60)
ssh_conn(password="Password@12345", username="admin12", ip_addr="172.16.20.33")
print("-" * 60)
ssh_conn("10.200.30.56", password="Spectra@123", username="admin369")
print("-" * 60)

def ssh_conn2(ip_addr, username, password, device_type = "cisco_ios"):
    print("IP address:", ip_addr)
    print("Username:", username)
    print("Password:", password)
    print("Device Type:", device_type)

ssh_conn2("201.32.123.233", "admin23", "Comp@123", "junos")
print("-" * 60)
ssh_conn2("125.23.45.56", password="P@sat123", username="admin45")
print("-" * 60)
pa_firewall = {"ip_addr": "180.10.20.30", "device_type": "pan-os", "password": "PA-FW@PANOS", "username": "admin89"}
ssh_conn2(**pa_firewall)
print("-" * 60)