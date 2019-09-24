def hijos(p): #checa el nodo en p si tiene hijos
	if(len(arb)-1>=p):
		if(len(arb)-1>=2*p+1):#puede que tenga ambos hijos
			if(arb[p*2]!=None):#si tiene hijo izq
				if (arb[p*2+1]!=None):
					#tiene ambos
					return 3
				return 1 #solo hijo izq
			elif(arb[2*p+1]!=None):
				return 2#tiene hijo der
		elif (len(arb)-1 >=2*p):
			if(arb[p*2]!=None):
				#tiene hijo der
				return 1
		else:
			#no tiene hijos		
			return 0
	else:
		#no existe
		return -1
def crecer(i):
	j=i-(len(arb)-1)	
	for v in range (j):
		arb.append(None)

def decrecer():
	global arb
	while(arb[len(arb)-1]==None):
		arb=arb[:len(arb)-1]
	

def insertar(v,p): #Valor y Posicion
	if p == len(arb):
		arb.append(v)
	elif p<len(arb):
		if hijos(p)==1 or hijos(p)==3 :
			aux=arb[p]
			arb[p]=v
			insertar(aux,p*2)
		elif hijos(p)==2:
			arb[p*2]=arb[p]
			arb[p]=v
		elif hijos(p)==0:
			crecer(p*2)
			arb[2*p]=arb[p]
			arb[p]=v

def eliminar(p):
	if (hijos(p)!=-1):
		if (hijos(p)==0):
			arb[p]=None
		elif((hijos(p)==1) or (hijos(p)==3)):
			arb[p]=arb[p*2]
			eliminar(p*2)	 
		elif hijos(p)==2:
			arb[p]=arb[p*2+1]
			eliminar(p*2+1)
	decrecer()

def infix(p):
	if(hijos(p*2)!=-1 and ((arb[p*2]!=None) and (arb[p*2] not in vis))):
		p=p*2
		infix(p)
	elif (arb[p] not in vis):
		vis.append(arb[p])
		if(hijos(p*2+1)!=-1 and ((arb[p*2+1]!=None) and (arb[p*2+1] not in vis))):
			p=p*2+1
			infix(p)
		else:
			p=p//2
			infix(p)
	else:
		if(p==1):
			return		
		else: 		
			p=p//2
			infix(p)

def prefix(p):
	if(arb[p] not in vis):
		vis.append(arb[p])
		if(hijos(p*2)!=-1 and ((arb[p*2]!=None) and (arb[p*2] not in vis))):
			#p=p*2
			prefix(p*2)
		if(hijos(p*2+1)!=-1 and ((arb[p*2+1]!=None) and (arb[p*2+1] not in vis))):
			#p=p*2+1
			prefix(p*2+1)
	else: 	
		p=p//2
		prefix(p)

def posfix(p):
	if(hijos(p*2)!=-1 and ((arb[p*2]!=None) and (arb[p*2] not in vis))):
		posfix(p*2)
	if(hijos(p*2+1)!=-1 and ((arb[p*2+1]!=None) and (arb[p*2+1] not in vis))):
		posfix(p*2+1)
	if(arb[p] not in vis):
		vis.append(arb[p])
	else:
		p=p//2
		posfix(p)
