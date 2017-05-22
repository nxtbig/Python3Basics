''' remove first and last character from string in list of string'''

n=int(input("Enter no. of elements in list \n"))
list1=[]
list2=[]
i=0
while i<n:
	list1.append(input())
	i=i+1

for it in list1:
	list2.append(it[1:-1])


print ("Required list\n")

print (list2)
