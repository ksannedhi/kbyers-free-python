mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

MAC1 = mac1.split()[3]
IP1 = mac1.split()[1]
MAC2 = mac2.split()[3]
IP2 = mac2.split()[1]
MAC3 = mac3.split()[3]
IP3 = mac3.split()[1]

print('{:>20} {:>20}'.format("IP ADDR", "MAC ADDR"))
print('-' *20 + " " +'-' *20)
print('{:>20}{:>20}'.format(IP1, MAC1))
print('{:>20}{:>20}'.format(IP2, MAC2))
print(f'{IP3:>20}{MAC3:>20}')