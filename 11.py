''' merge two dictionaries '''

D1={'team1':'Alpha','team2':'Beta'}
D2={'team3':'Gamma','team4':'Delta'}

D3={}

D3=D1.copy()
D3.update(D2)

print (D3)