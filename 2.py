'''filter multiple of 5 and print it as sorted list'''

n=int(input("Enter no. of elements in list \n"))
list1=[]
list2=[]
i=0
while i<n:
	list1.append(int(input()))
	i=i+1;

for it in list1:
	if it%5 ==0 :
		list2.append(it)

list2.sort()

print ("Required list\n")

for it in list2:
	print (it, end='\n')
