def mac_normal(mac_addr):
    mac_addr = mac_addr.upper()

    if ":" in mac_addr: # See 3-2 if you want to reduce the code to if and elif only.
        octets = mac_addr.split(":")
        updated_octets = []
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            updated_octets.append(octet)

    elif "-" in mac_addr:
        octets = mac_addr.split("-")
        updated_octets = []
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            updated_octets.append(octet)

    elif "." in mac_addr:
        octets = mac_addr.split(".")
        updated_octets = []
        for octet in octets:
            if len(octet) < 4:
                octet = octet.zfill(4)
            updated_octets.append(octet[:2])
            updated_octets.append(octet[2:])

    return ":".join(updated_octets)

print(mac_normal("a-b-c-d-e-f"))
print(mac_normal("d:e:f:1:2:3"))
print(mac_normal("01-02-03-04-05-06"))
print(mac_normal("ab:cd:ef:12:34:56"))
print(mac_normal("234.567.890"))
print(mac_normal("cedf.ab34.5678"))