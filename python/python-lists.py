n=int(raw_input())
a=[]
for i in xrange(n):
	commands=raw_input()
	commands=commands.split()
	command=commands[0]
	if command=='print':
		print a
	elif command == 'sort':
		a.sort()
	elif command=='pop':
		a.pop()
	elif command=='reverse':
		a.reverse()
	elif command=='count':
		print count(commands[1])
	elif command=='insert':
		a.insert(int(commands[1]),int(commands[2]))
	elif command=='remove':
		a.remove(int(commands[1]))
	elif command=='append':
		a.append(int(commands[1]))