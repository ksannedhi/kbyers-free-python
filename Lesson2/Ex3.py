from pprint import pprint

with open("show_arp.txt") as f:
    text = f.readlines()

text.pop(0)
text.sort()

new_arp_list = text[:3]

joined_arp_list = "\n".join(new_arp_list)

with open("arp_entries.txt", "w") as f:
    f.write(joined_arp_list)
