'''filter words greater than x characters and output is as sorted list'''

n=int(input("Enter no. of elements in list \n"))
x=int(input("Enter n \n"))
list1=[]
list2=[]
i=0
while i<n:
	list1.append(input())
	i=i+1

for it in list1:
	if len(it)>x :
		list2.append(it)

list2.sort()

print ("Required list\n")

for it in list2:
	print (it, end='\n')

