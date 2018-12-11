#py2
from collections import defaultdict

n = int(raw_input().strip())
bucket = defaultdict(list)

for _ in xrange(n):
    number = raw_input().strip()
    bucket[len(number)].append(number)
    
for key in sorted(bucket):
    for value in sorted(bucket[key]):
        print(value)