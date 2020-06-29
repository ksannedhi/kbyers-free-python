from pprint import pprint
f = open("show_arp.txt")
arp = f.read()
arp = arp.splitlines()
arp.pop(0)
first_3_arp = arp[:3]

first_3_arp = "\n\n".join(first_3_arp)
with open("arp_entries_2.txt", "w") as f:
    f.write(first_3_arp)
