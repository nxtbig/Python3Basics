''' generating odd even traffic schedule'''

import calendar

di={1:'January',2:'Febuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
def schedule(month):
	cal=calendar.monthrange(2017,month)
	i=1
	k=cal[0];
	while i<=cal[1]:
		if k==6:
			print ("On %d, %s, 2017: All cars are allowed"%(i,di[month]))
		elif i%2==0:
			print ("On %d, %s, 2017: Even cars are allowed"%(i,di[month]))
		else:
			print ("On %d, %s, 2017: Odd cars are allowed"%(i,di[month]))
		k=k+1
		k=k%7;
		i+=1

schedule(2)

