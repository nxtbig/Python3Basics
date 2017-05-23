''' flatten a list'''
from functools import reduce
inp=[[1,2,3],[4,5],[6,7,8]]
out=reduce(lambda x,y: x+y,inp)

for i in out:
	print(i)

