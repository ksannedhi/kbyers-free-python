with open("show_arp.txt") as f:
    text = f.readlines()
text.pop(0)

for elem in text:
    arp_details = elem.split()
    ip_addr = arp_details[1]
    mac_addr = arp_details[3]
    if ip_addr == "10.220.88.1":
        print(f'Default gateway IP/Mac: {ip_addr}/{mac_addr}')
    elif ip_addr != "10.220.88.30":
        continue
    else:
        print(f'Arista3 IP/Mac is {ip_addr}/{mac_addr}')
        break