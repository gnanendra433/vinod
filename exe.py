a = input('enter a value')
b = input('enter second value')
try:
	c = a/b
except Exception as e:
	print 'division not possible'
	print e
	c = 0
print c