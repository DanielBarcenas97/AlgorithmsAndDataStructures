a=input()   
arb=[]
a=a.split(", ")
a[0]=a[0][1:len(a[0])]
a[len(a)-1]=a[len(a)-1][0:len(a[len(a)-1])-1]
for w in a:
    arb.append(int(w))


def eliminar(p):
	if hijo(p) != -1:
		if hijo(p)==0:
			arb[p]=None
		elif hijo(p)==1 or hijo(p)==3: #hijo izquierdo
			arb[p]=arb[2*p]
			eliminar(2*p)
		elif hijo(p)==2:
			arb[p]=arb[2*p+1]
			eliminar(2*p+1)
	decrecer()
def decrecer ():
	global arb
	while (arb[len(arb)-1] == None ):
		arb = arb [:len(arb)-1]

def aumentar(i):
	j=i-len(arb)+1  #nos indica cuantos elementos hay que agregar
	for l in range (j):
		arb.append(None)
		
def insertar (v,p):
	if p==len(arb):
		arb.append(v)
	elif p < len(arb):
		if hijo(p) == 1 or hijo(p) ==3: #si tiene un hijo o mas
			aux = arb[p]
			arb[p]=v
			insertar(aux, 2*p)
		elif hijo(p)==2: #si no tine hijos
			aux=arb[p]
			arb[p]=v
			insertar(aux, 2*p+1)

		elif hijo(p)==0: #si no tine hijos
			aumentar(2*p)
			arb[2*p]=arb[p]
			arb[p]=v

def hijo (p):
	
	if len(arb)-1>=p:
		if len(arb)-1 >= 2*p and arb[2*p] != None:  #verificamos que tenga hijo izquierdo
			if len (arb)-1 >= 2*p+1 and arb[2*p]!= None: #hijo derecho
				return 3
			return 1
		elif len(arb)-1 >= 2*p+1 and arb[2*p]!=None:
			return 2

		else:	#no tiene hijo izquierdo ni derecho
			return 0
	else:
		return -1
ins=input()
ins=ins.split(", ")
ins[0]=ins[0][1:len(ins[0])]
ins[len(ins)-1]=ins[len(ins)-1][0:len(ins[len(ins)-1])-1]
insertar (int(ins[0]),int(ins[1]))
elim=input()
elim=elim.replace("[", "")
elim=elim.replace("]", "")
eliminar(int(elim))
print(arb)