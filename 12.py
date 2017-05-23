''' count occurences of numbers'''

inp=[1,2,3,4,5,6,7,8,9,2,4,6,5]

dic={}
for i in inp:
	k=dic.get(i,'none')
	if(k!='none'):
		dic[i]=dic[i]+1
	else:
		dic[i]=1

for i in dic:
	print ("value %d occured %d time(s) in the list" %(i,dic[i]))
