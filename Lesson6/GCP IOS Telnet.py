from netmiko import Netmiko
from getpass import getpass

password = getpass()

ios_dict = {"host": "35.213.180.99",
           "port": "32770",
           "username": "pyclass",
           "password": password,
           "secret": password,
           "device_type": "cisco_ios_telnet",
           "session_log": "telnet_log.txt"}

ios_connect = Netmiko(**ios_dict)
ios_connect.send_command_timing("disable")
print(ios_connect.find_prompt())

ios_connect.enable()
print(ios_connect.find_prompt())
