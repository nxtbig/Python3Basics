''' check if a key exits or not'''


Keys=['team1','teamX','team4','team5']
Dict={'team1':'Alpha','team2':'Beta','team3':'Gamma','team4':'Delta'}
temp={}

for i in Keys:
	k=Dict.get(i,'none')
	if k!='none':
		temp[i]=k

print (temp)