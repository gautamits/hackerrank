def reduced(s):
	if s=="":
		return "Empty String"
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			s=s[:i]+s[i+2:]
			return reduced(s)
	return s
#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    if s=="":
        return "Empty String"
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s=s[:i]+s[i+2:]
            return super_reduced_string(s)
    return s


s = input().strip()
result = super_reduced_string(s)
print(result)
