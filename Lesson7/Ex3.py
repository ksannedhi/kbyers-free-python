import jinja2

bgp_params = {"local_as": 10, "peer1_ip": "10.200.200.5", "peer1_as": 20,
              "neighbor_net1": "10.200.201.0/24", "neighbor_net2": "10.200.202.0/24", "neighbor_net3": "10.200.203.0/24"}

bgp_temp = """
feature bgp
router bgp {{local_as}}
    address-family ipv4 unicast
        net {{neighbor_net1}}
        net {{neighbor_net2}}
        net {{neighbor_net3}}
    neighbor {{peer1_ip}} remote-as {{peer1_as}}
        update-source loopback1
        ebgp-multihop 2
        address-family ipv4 unicast
"""

temp = jinja2.Template(bgp_temp)
print(temp.render(bgp_params))
