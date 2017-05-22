'''converting multiple of 5 as string and sorting it and observing difference from 2.py'''
n=int(input("Enter no. of elements in list \n"))
list1=[]
list2=[]
i=0
while i<n:
	list1.append(int(input()))
	i=i+1;

for it in list1:
	if it%5 ==0 :
		list2.append(str(it))

list2.sort()

print ("Required list\n")

for it in list2:
	print (it, end='\n')

'''difference is after sorting 

for ex 5 will come after 15 in this program whereas in 2.py it 5 will come before 15

 '''