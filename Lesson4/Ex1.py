dev_details = {'ip_addr': '192.168.1.23', 'vendor': 'Cisco', 'username': 'admin', 'password': 'password'}
print(dev_details['ip_addr'])

if dev_details['vendor'].capitalize() == "Cisco":
    dev_details["platform"] = "ios"
elif dev_details['vendor'] == "juniper":
    dev_details["platform"] = "junos" #"else" is not mandatory

print(f'Updated device dictionary - {dev_details}')

bgp_fileds = {'bgp_as': '65300', 'peer_as': '64800', 'peer_ip': '172.16.20.230'}
bgp_fileds.update(dev_details)
print(f'Updated BGP dictionary - {bgp_fileds}')

print("-" * 60)
for key in bgp_fileds.keys():
    print(key)

print("-" * 60)
for key, value in bgp_fileds.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))