#!/bin/python3.7
import ipaddress
import pprint

enter_ip = input('Enter ip: ')
enter_mask = int(input('Enter prefix: '))
bin_netmask = []

# Create ip/prefix
united  = []
united.append(enter_ip)
united.append('/')
united.append(str(enter_mask))

ip_prefix = ''.join(united)

ip_addr = ipaddress.ip_interface(ip_prefix)

#Choose netmask (metod interface)
netmask = ip_addr.netmask

#Choose wildcard mask
wildcard_ip_mask = ip_addr.with_hostmask
wildcard__mask = wildcard_ip_mask.split('/')
wildcard_mask = ''.join(wildcard__mask[-1])

#Choose network network_ip (IPv4 to str and select (number 0))
net = ()
network_ip_mask = ip_addr.network
network_ip = network_ip_mask[0]

#Broadcast_address
broad = ipaddress.IPv4Network(enter_ip+'/'+str(netmask), False).broadcast_address

#HostMin
hostmin = list(ip_addr.network)

#HostMax
hostmax = list(ip_addr.network)

#Len hosts
len_hosts = len(hostmax)

#Insert 1 and 0 to net_mask (0-32)
for i in range(0,enter_mask):
    bin_netmask.append(1)

for i in range(enter_mask,32):
    bin_netmask.append(0)    

#Chunks list for 8x4 
mask_octets = [bin_netmask[i:i+8] for i in range(0,len(bin_netmask),8)]

octet_1 = mask_octets[0]
octet_2 = mask_octets[1]
octet_3 = mask_octets[2]
octet_4 = mask_octets[3]

#Conver octets to str
str_oct_1 = []
str_oct_2 = []
str_oct_3 = []
str_oct_4 = []

for i in octet_1:
    str_oct_1.append(str(i))   
str_oct_1 = ''.join(str_oct_1)    

for i in octet_2:
    str_oct_2.append(str(i))   
str_oct_2 = ''.join(str_oct_2)    

for i in octet_3:
    str_oct_3.append(str(i))   
str_oct_3 = ''.join(str_oct_3)

for i in octet_4:
    str_oct_4.append(str(i))   
str_oct_4 = ''.join(str_oct_4)


print ('*'*20,'Output','*'*20)
print (f'IP Address: {enter_ip}')
print (f'Mask (prefix): {enter_mask}')
print (f'Bin NetMask: {str_oct_1}.{str_oct_2}.{str_oct_3}.{str_oct_4}')
print (f'Netmask: {netmask}')
print (f'Wildcard mask: {wildcard_mask}')
print (f'Networ IP: {network_ip}')
print (f'Broadcast Address: {broad}')
print (f'Hostmin: {hostmin[1]}')
print (f'Hostmax: {hostmax[-2]}')
print (f'Hosts: {len_hosts-2}')