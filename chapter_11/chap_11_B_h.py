dict_lan = {
    'eth0': {'IP': '1.1.1.1', 'status': 'up'},
    'eth1': {'IP': '2.2.2.2', 'status': 'up'},
    'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
    'wlan1': {'IP': '4.4.4.4', 'status': 'up'}

}

# given_int = input("Enter the interface: ")
# print(dict_lan[given_int]['status'])

for k, v in dict_lan.items():
    if v['status'] == "up":
        print(k, v['IP'])
print(f"Total interfaces: {len(dict_lan)}")

dict_lan['wlan2'] = {'IP': '5.5.5.5', 'status': 'up'}
dict_lan['wlan3'] = {'IP': '6.6.6.6', 'status': 'up'}
print(dict_lan)
