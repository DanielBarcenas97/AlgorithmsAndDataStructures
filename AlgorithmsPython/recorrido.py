arb=[0,67,27,28,79,72,14,48]
l=[]
def hijos(p):
	if p<=len(arb)-1:
		if len(arb)-1>=2*p+1: #puede que tenga ambos hijos
			if arb[2*p]!=None: #si tiene hijo derecho
				if arb[2*p+1]!=None: #tiene ambos hijos
					return 3
				return 1 #Si solo no tiene hijo izquierdo
			elif arb[2*p+1]!=None: #solo tiene hijo derecho
				return 2
		elif len(arb)-1>=2*p:#puede que solo tenga hijo izquierdo
			if arb[2*p]!=None:
				#solo tiene hijo derecho
				return 1
		else:
			#no tiene hijos
			return 0
	else: 
		#no exite
		return -1
def infix(i,l=[]):
	if hijos(i)!=-1:
		infix(2*i,l)
		if arb[i]!=None:
			l.append(arb[i])
		infix(2*i+1,l)
	return l
def prefix(i,l=[]):
	if hijos(i)!=-1:
		if arb[i]!=None:
			l.append(arb[i])
		prefix(2*i,l)
		prefix(2*i+1,l)
	return l
def postfix(i, l=[]):
	if hijos(i)!=-1:
		postfix(2*i,l)
		postfix(2*i+1,l)
		if arb[i]!=None:
			l.append(arb[i])
	return l	
			

print(arb)
print(infix(1))
print(prefix(1))
print(postfix(1))