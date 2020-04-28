import pcapy

# find and print devices
devices = pcapy.findalldevs()
print(devices)

# device, # of byt to capture per packet, promiscous mode, timeout (ms)
capture = pcapy.open_live("en0", 65536, 1, 0)

count = 1
while count:
    #print count of captured packets
    (header, payload) = capture.next()
    print(count)
    count = count + 1
