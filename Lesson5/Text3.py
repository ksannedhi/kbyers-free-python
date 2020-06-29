import re


def normalize_mac_address(mac_address):

    mac_address = mac_address.upper()

    if ':' in mac_address or '-' in mac_address:
        new_mac = []
        octets = re.split(r"[-:]", mac_address)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif '.' in mac_address:
        new_mac = []
        sections = mac_address.split('.')
        if len(sections) != 3:
            raise ValueError("Something went wrong")

        for word in sections:
            if len(word) < 4:
                word = word.zfill(4)
            new_mac.append(word[:2])
            new_mac.append(word[2:])

    return ":".join(new_mac)


# Some tests
assert "01:23:02:34:04:56" == normalize_mac_address('123.234.456')
assert "AA:BB:CC:DD:EE:FF" == normalize_mac_address('aabb.ccdd.eeff')
assert "0A:0B:0C:0D:0E:0F" == normalize_mac_address('a:b:c:d:e:f')
assert "01:02:0A:0B:03:44" == normalize_mac_address('1:2:a:b:3:44')
assert "0A:0B:0C:0D:0E:0F" == normalize_mac_address('a-b-c-d-e-f')
assert "01:02:0A:0B:03:44" == normalize_mac_address('1-2-a-b-3-44')
print("Tests passed")