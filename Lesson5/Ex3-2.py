import re

def mac_normal(mac_addr):
    mac_addr = mac_addr.upper()

    if "-" in mac_addr or ":" in mac_addr:
        octets = re.split(r'[:-]', mac_addr)
        updated_mac = []
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            updated_mac.append(octet)

    elif "." in mac_addr:
        octets = mac_addr.split(".")
        updated_mac = []
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            updated_mac.append(octet)

    return ":".join(updated_mac)

print(mac_normal("12-34-56-78-9a-bc"))
print(mac_normal("ab.cd.ef.13.25.36"))