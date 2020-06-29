import jinja2

bgp_params = {}

bgp_template = '''
feature bgp
router bgp 10
    address-family ipv4 unicast
        net 10.10.200.0/24
        net 10.10.201.0/24
        net 10.10.202.0/24
    neighbor 10.255.255.2 remote-as 20
        update-source loopback1
        ebgp-multihop 2
        address-family ipv4 unicast 
'''

temp = jinja2.Template(bgp_template)
print(temp.render(bgp_params))
