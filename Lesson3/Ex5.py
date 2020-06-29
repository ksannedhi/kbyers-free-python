import os

base_cmd_windows = 'ping -n 3'

base_ip = "192.168.0."

ip_list = []

for byte in range(1,10):
    ip = base_ip + str(byte)
    ip_list.append(ip)

for index, ip in enumerate(ip_list):
    print(f'{index} ---> {ip}')

for ip in ip_list:
    print("-" * 80)
    print ("Now pinging the", ip)
    os.system("{} {}".format(base_cmd_windows, ip))