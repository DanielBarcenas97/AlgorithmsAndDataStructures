arb=[0,20,1,57,46,6,88,40]
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
def crecer(i):
	j=i-len(arb)+1
	for l in range(j):
		arb.append(None)
def decrecer():
	global arb
	while(arb[len(arb)-1]==None):				
		arb=arb[:len(arb)-1]
		#arb.remove(arb[len(arb)-1])
		#decrecer()
def insertar(v,p):
	if p==len(arb):
		arb.append(v)
	elif p<len(arb):
		if hijos(p)==1 or hijos(p)==3:
			aux=arb[p]
			arb[p]=v
			insertar(aux, 2*p)#hacer el derecho con 2p+1	
		elif hijos(p)==2:
			#solo tiene hijo derecho
			arb[2*p]=arb[p]
			arb[p]=v
		elif hijos(p)==0: 			
			crecer(2*p)
			arb[2*p]=arb[p]
			arb[p]=v
def eliminar(p):
	if hijos(p)!=-1:
		if hijos(p)==0:
			arb[p]=None
		elif hijos(p)==1 or hijos(p)==3:
			arb[p]=arb[2*p]
			eliminar(2*p)
		elif hijos(p)==2:
			arb[p]=arb[2*p+1]
			eliminar(2*p+1)
		decrecer()
		
		
print(arb)
insertar(114,5)
eliminar(3)
print(arb)
