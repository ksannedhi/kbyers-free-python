houston_dc = ["10.100.2.3", "10.100.2.5", "10.100.2.7", "10.100.2.7", "172.16.20.23",
              "172.16.20.25", "172.16.20.25", "192.168.20.3", "192.168.20.5", "192.168.20.7"]
atlanta_dc = ["10.100.3.3", "10.100.3.5", "10.100.2.3", "172.16.20.23", "172.16.30.3", "172.16.30.5",
              "192.168.30.3", "192.168.30.5"]
chicago_dc = ["10.100.4.3", "10.100.4.5", "10.100.4.7", "10.100.2.3", "10.100.3.3", "172.16.40.5",
              "172.16.20.25", "172.16.0.5"]

houston_dc_set = set(houston_dc)
atlanta_dc_set = set(atlanta_dc)
chicago_dc_set = set(chicago_dc)

print("Houston DC IPs:", houston_dc_set)
print("Atlanta DC IPs:", atlanta_dc_set)
print("Chicago DC IPs:", chicago_dc_set)

houston_atlanta_dupes = houston_dc_set.intersection(atlanta_dc_set)
print("IPs that are duplicated between Atlanta and Houston:", houston_atlanta_dupes)

dupes_in_all_3_cities = chicago_dc_set.intersection(houston_atlanta_dupes) #You can also do & with all 3 cities together
print("IPs that are duplicated in all 3 cities:", dupes_in_all_3_cities)

houston_and_atlanta = houston_dc_set.union(atlanta_dc_set)
chicago_unique = chicago_dc_set.difference(houston_and_atlanta)
print("IPs that are unique to Chicago:", chicago_unique) #You can also do chic.diff(hou).diff(atl)