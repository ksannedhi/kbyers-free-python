from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

net_dev = [{"host": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_xe"},
         {"host": "cisco4.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_xe"},
         {"host": "arista1.lasthop.io", "username": "pyclass", "password": password, "device_type": "arista_eos"}]

for dev in net_dev:
    dev_connect = ConnectHandler(**dev)
    output = dev_connect.send_command("show ip arp")
    print(output)
    print("-" * 81)
