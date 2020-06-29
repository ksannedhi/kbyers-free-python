ip_list = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5']
ip_list.append('6.6.6.6')
ip_list.extend(["7.7.7.7", "8.8.8.8"])
new_ip_list = ["9.9.9.9", "10.10.10.10"]
ip_list = ip_list + new_ip_list
print(ip_list[0])
print(ip_list[-1])
ip_list.pop()
ip_list.pop(0)
print(ip_list)
ip_list.insert(0, "1.1.1.1")
print(ip_list)
