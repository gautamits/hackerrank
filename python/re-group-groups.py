# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.search(r'([a-zA-Z0-9])\1+', raw_input())
if m:
    print m.group(1)
else:
    print "-1"
