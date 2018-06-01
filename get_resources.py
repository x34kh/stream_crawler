#!/usr/bin/python
import json
import os

def main():
   for i in range(0,25):
      print "Iteration #%s" % i
      gen_list(i)
      scan_hosts()
def scan_hosts():
   with open('list.json') as f:
      data = json.load(f)
   for host in data['matches']:
      print "%s:%s" % (host["ip"],host["portinfo"]["port"])
      os.system("nmap --script rtsp-url-brute.nse -p %s %s | grep \"rtsp:\" > /tmp/rtsp/%s &" % (host["portinfo"]["port"], host["ip"], host["ip"]))
   
def gen_list(page):
   os.system("./get_list.sh %s" % page)

if __name__== "__main__":
   main()