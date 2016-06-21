a={}
n=int(raw_input(""))
for i in xrange(n):
	q=raw_input("")
	try:
		m=a[q]
		a.pop(q)
		a[q]=m+1
	except:
		a[q]=1
q=int(raw_input(""))
for i in xrange(q):
	query=raw_input("")
	try:
		print a[query]
	except:
		print 0
