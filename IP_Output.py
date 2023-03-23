import subprocess
import re

subprocess.call("ifconfig > if_out.txt", shell=True)
interface_rule = re.compile(r'(.*?):\W')
ip_rule = re.compile(r'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
with open('if_out.txt', 'r') as f:
  content = f.read()
  ip_address = re.findall(ip_rule, content)
  interface = re.findall(interface_rule, content)
  for i in range(len(ip_address)):
    print(interface[i].strip() + ": " + ip_address[i][4:])
  f.close()
subprocess.call("rm if_out.txt", shell=True)
