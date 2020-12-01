from requests.auth import HTTPBasicAuth
import requests

#
# Note: It's a bad practice to keep username and password inside code file.
#
auth = HTTPBasicAuth('cisco', 'cisco')
url = 'https://csr1kv/restconf/data/Cisco-IOS-XE-native:native/interface'
xml_headers = {'Content-Type': 'application/vnd.yang.data+xml'}

gigabit_interface_data  = """<GigabitEthernet><name>1</name></GigabitEthernet>"""
loopback_interface_data = """<Loopback><name>1</name></Loopback>"""

response = requests.request("POST", url, data=gigabit_interface_data, headers=xml_headers, verify=False, auth=auth)
print (response.text)

response = requests.request("POST", url, data=loopback_interface_data, headers=xml_headers, verify=False, auth=auth)
print (response.text)


