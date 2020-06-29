from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    text = f.readlines()

fe4 = text[-2]
details = fe4.split()

int_tuple = (details[0], details[1])
print(int_tuple)
