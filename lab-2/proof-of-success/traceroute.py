from scapy.all import *

ttl=1
while True:
  ip = IP(dst='8.8.8.8', ttl=ttl)
  icmp = ICMP()
  p = ip/icmp
  
  resp = sr1(p, verbose=0, timeout=5)
  
  if (resp==None):
    print("TTL: {0}, Source: ???".format(ttl))
    ttl+=1
  elif (resp[ICMP].type==0):
    print("Complete", resp[IP].src)
    break
  else:
    print("TTL: {0}, Source: {1}".format(ttl, resp[IP].src))
    ttl+=1
