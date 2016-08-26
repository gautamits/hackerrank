"""
In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, . You must perform operations of the following types:

    append - Append string to the end of .
    delete - Delete the last characters of .
    print - Print the character of .
    undo - Undo the last (not previously undone) operation of type or , reverting to the state it was in prior to that operation.

Input Format

The first line contains an integer, , denoting the number of operations.
Each line of the subsequent lines (where ) defines an operation to be performed. Each operation starts with a single integer, (where ), denoting a type of operation as defined in the Problem Statement above. If the operation requires an argument, is followed by its space-separated argument. For example, if and , line will be 1 abcd.

Constraints

    The sum of the lengths of all in the input .
    All input characters are lowercase English letters.
    It is guaranteed that the sequence of operations given as input is possible to perform.

Output Format

Each operation of type must print the character on a new line.

Sample Input

8
1 abc
3 3
2 3
1 xy
3 2
4 
4 
3 1

Sample Output

c
y
a
"""
	

s=""
steps=[]
t=int(raw_input())
i=0
add=[]
delete=[]
while t>0:
	inp=raw_input().split()
	if len(inp)==1 and int(inp[0])==4:
		prev=steps.pop()
		if prev==1:
			# value was appended
			value=add.pop()
			#print value,' will be deleted'
			s=s[0:len(s)-len(value)]
		elif prev==2:
			#value was deleted
			value=delete.pop()
			#print value,' will be added'
			s=s+value
	else:
		a,b=inp
		
		a=int(a)
		if a!=3:
			steps.append(a)
		if a==1:
			s=s+b
			add.append(b)
		elif a==2:
			b=int(b)
			delete.append(s[len(s)-b:])
			s=s[0:len(s)-b]
			
		elif a==3:
			b=int(b)
			print s[b-1]
	#print s,steps
	t-=1
	i+=1
