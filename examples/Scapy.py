from scapy.all import * 

frame = Ether(dst="00:DE:AD:BE:EF:00")/IP("10.10.10.100")/TCP()"Check this out"

print(frame)
sendp(frame)
