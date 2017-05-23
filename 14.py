'''filter only integer from list'''

inp=[1,'a',['d','e','f'],2,-1,(1,2,3),'g']
out=filter(lambda x: type(x) is int,inp)
for i in out:
	print (i)