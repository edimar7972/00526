def matriz(a,b):
	m=[]
	for i in range(a+1):
		linha=[]
		for j in range(b+1):
			c=-1
			linha.append (c)
		m.append(linha)
	return m

def quantidade(x,y,m,n):
	lcs= matriz(m,n)
	r= matriz(m,n)
	for i in range(m+1):
		lcs[i][0]= i
		r[i][0]=="A"
	for j in range(n+1):
		lcs[0][j]=j
		r[0][j]="B"
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1]==y[j-1]:
				dif=0
			else:
				dif=1
			if lcs[i-1][j-1] + dif <= 1 + min(lcs[i][j-1],lcs[i-1][j]):
				lcs[i][j] = lcs[i-1][j-1]+dif
				r[i][j]="C"
			elif lcs[i][j-1] <= lcs[i][j-1]:
				lcs[i][j] = lcs[i][j-1]+1
				r[i][j]="A"
			else:
				lcs[i][j] = lcs[i-1][j]+1
				r[i][j]="B"
	percorre(x,y,r)

def  percorre(x,y,r):
	i=len(x)
	j=len(y)
	l=[]
	while j!= 0 or i !=0:
		if r[i][j] == "C":
			m=[]
			if y[j-1] != x[i-1]:
				m.append("Replace")
				m.append(i)
				m.append(x[i-1])
				i=i-1
				j=j-1
				l.append(m)	
			else:
				i=i-1
				j=j-1
		if r[i][j] == "A":
			m=[]
			if y[j-1] != x[i-1]:
				m.append("Delete")
				m.append(i+1)
				j=j-1
				l.append(m)
			else:
				j=j-1
		if r[i][j] == "B":
			m=[]
			if y[j-1] != x[i-1]:
				m.append("Delete")
				m.append(i+1)
				j=j-1
				l.append(m)
			else:
				j=j-1
	l=l[::-1]
	for i in range(len(l)):
		if l[i][0] == "Replace":
			print(i+1,l[i][0],l[i][1],",",l[i][2])
		else:
			print(i+1,l[i][0],l[i][1])
			
x="ihyenlssxuyibv"
y="sfkgphrdbufoihecwuulkhmce"
m=len(x)
n=len(y)
quantidade(x,y,m,n)


