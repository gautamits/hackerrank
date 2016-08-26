import math
for _ in xrange(int(raw_input())):
	a,b=map(int,raw_input().split())
	if a==0 or int(math.log(a,2)) != int(math.log(b,2)):
		print('0')
	else:
		pos = int(math.log(a^b,2))+1
		mask = ~int(''.join(map(str,['1']*pos)),2)
		print(str(mask&b))