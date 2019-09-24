a3=[]
class vertex:
	def __init__(self,v):
		self.id=v
		self.padre=None
		self.hizq=None
		self.hder=None
		self.altura=-1
class arbol:
	def __init__(self):
		self.raiz=None
	def agregar(self,act,ver):
		if act.id< ver.id:
			if act.hder!=None:
				self.agregar(act.hder,ver)
			else:
				act.hder=ver
				ver.padre=act
		else:
			if act.hizq!=None:
				self.agregar(act.hizq,ver)
			else:
				act.hizq=ver
				ver.padre=act
	def agregarVertice(self, v):
		ver=vertex(v) #crea el objeto
		if self.raiz==None:
			self.raiz=ver
		else:
			self.agregar(self.raiz, ver)
	def crearArbol(self, lv):
		for i in range(len(lv)):
			self.agregarVertice(lv[i])
	def imprimir(self,act):
		if act!=None:
			self.imprimir(act.hizq)
			print(act.id, act.altura)
			self.imprimir(act.hder)
	def altura(self, act):
		if act!=None:
			global a3
			a1=self.altura(act.hizq)
			a2=self.altura(act.hder)
			act.altura=max([a1,a2])+1
			if a1-a2>1:
				a3.append(act.id)
			if a2-a1>1:
				a3.append(act.id)
			a3.sort()
			return act.altura			
		else: 
			return -1

class main:
	l=input()
	l=l.strip('[')
	l=l.strip(']')
	l=l.split(',')
	l2 = []
	for j in l:
		l2.append(int(j))
	t=arbol()
	t.crearArbol(l2)
	t.altura(t.raiz)
	print(a3)