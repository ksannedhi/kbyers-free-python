import re

with open("show_ipv6_intf.txt") as f:
    text = f.read()

match = re.search(r'^.*IPv6 address:\s+(.*)\s+IPv6 subnet:\s', text, flags=re.DOTALL) #Here a space can be used before IPv6 as there is really a space in the text.
ipv6_addrs = match.group(1).split()
ipv6_addrs.pop(1)
print(ipv6_addrs[0] +"\n" +ipv6_addrs[1])

print("-" * 45)

match_ipv6 = re.search(r'.* IPv6 address:\n(.*?)IPv6', text, flags=re.DOTALL).group(1) #DOTALL to extend the output across multiple lines.
ipv6 = match_ipv6.split()
print(f'{ipv6[0]}\n{ipv6[2]}')
