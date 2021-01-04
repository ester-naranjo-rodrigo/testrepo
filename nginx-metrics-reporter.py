import re
from collections import Counter

patron1 = re.compile(r'::1')
patron2 = re.compile(r'\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
ips = []

with open("/var/log/nginx/access.log") as f:
    for line in f:
        for ip1 in re.findall(patron1, line):
            ips.append(ip1)
        for ip2 in re.findall(patron2, line):
            ips.append(ip2)
    
    counter = Counter(ips)
    print(counter)

with open("/opt/report.txt", "w") as f:
    for key, val in counter.items():
        f.write(f'{key} {val}\n')


