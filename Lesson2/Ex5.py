with open("show_ip_bgp_summ.txt") as f:
    text = f.readlines()

first_entry_details = text[0].split()
last_entry_details = text[-1].split()

local_as_number = first_entry_details[-1]
bgp_peer_ip = last_entry_details[0]

print(f'AS number is {local_as_number} and the BGP peer IP is {bgp_peer_ip}')