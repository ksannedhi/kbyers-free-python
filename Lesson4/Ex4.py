import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

model_match = re.search(r'Cisco (?P<model>\S+)\s', show_version, flags=re.M) #You need three things: ?P, <stri>, and text you want to see..
memory_match = re.search(r'^.* \(revision 1.0\) with (?P<memory>\S+)\s', show_version, flags=re.M)

model = model_match.groupdict()["model"] #Get value by key from the model_match dictionary
memory = memory_match.groupdict()["memory"]
print(f'Model: {model} \nMemory: {memory}')