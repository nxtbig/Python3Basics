n=int(input("Enter no. of elements in list\n"))
x=int(input("Which char to remove\n"))
x=x-1
list1=[]
list2=[]
i=0
while i<n:
	list1.append(input())
	i=i+1

for it in list1:
	list2.append(it[:x]+it[x+1:])


print ("Required list\n")

print (list2)