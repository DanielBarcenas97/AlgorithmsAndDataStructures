#Representacion de graficas
global a
a=1
class vertex:
	def __init__(self,i): #Identificador del vertice, constructor
		self.id=i #Equivalente a this en POO
		self.visitado=False #Variable boolenena que nos indica si el nodo fue visitado en BFS 
		self.nivel=-1 #Nivel inicial de todos los nodos
		self.vecinos=[] #Lista de vecinos del nodo, a los que esta conectado
		self.costo=999999999
		self.padre=-1#float('inf')
	def agregarVecino(self,v): #Se agrega un vecino al nodo
		if v[0] not in self.vecinos:
			self.vecinos.append(v)
	def eliminarVecino(self,v): #Se elimina el vecino del nodo
		if v[0] in self.vecinos:
			self.vecinos.remove(v)

class graph:
	def __init__(self):
		self.vertices={} #Diccionario
	def agregarVertice(self,v):
		if v not in self.vertices:
			vert=vertex(v)
			self.vertices[v]=vert #Asigna v a un diccionario
	def eliminarVertice(self,v):
		if v in self.vertices: 
			del self.vertices[v] #Elimina un vertice
	def agregarArista(self,a,b,p): #Se agrega una arista
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino([b,p])			
	def eliminarArista(self,a,b): #Se elimina la arista
		if a in self.vertices and b in self.vertices:
			self.vertices[a].eliminarVecino(b)
	def imprimirGrafica(self): #Imprime grafica
		print("Grafica")
		for v in self.vertices:
			print("Vertice: ", self.vertices[v].id)
			print(self.vertices[v].vecinos)
	def BFS(self,r): #BFS
		if r in self.vertices:
			for v in self.vertices:
				self.vertices[v].nivel=-1 #Se inicializan todos los niveles en -1
			print("BFS")
			cola=[] #Cola que asigana turnos a los nodos para verificar sus vecinos y asignar niveles
			cola.append(r) #Se agrega el elemento raiz, el primero a visitar
			self.vertices[r].nivel=0 #Se le da el nivel 0
			print(r,self.vertices[r].nivel)
			self.vertices[r].visitado=True #Ya esta visitado
			while(len(cola)>0):
				act=cola[0]
				cola=cola[1:] #Funcion dequeue
				for vec in self.vertices[act].vecinos: #Se verifican los vecinos
					if self.vertices[vec].visitado == False:
						cola.append(vec) #Si no estan visitados se agregan a la cola
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel=self.vertices[act].nivel+1 #Se le asigna nivel
						print(vec,self.vertices[vec].nivel)
		else:
			print("El vertice no existe")	
	def camino(self,a,b):
		if a in self.vertices and b in self.vertices: #Se verifica que existan los nodos
			for v in self.vertices:
				self.vertices[v].nivel=-1
			self.BFS(b) #Para el nodo b que es al que se desea llegar, se hace BFS
			n=self.vertices[a].nivel
			recorrido=[] #Creamos una lista que contenga los nodos que recorrio a para llegar a b
			recorrido.append(a) 
			act=a #Se define a como el nodo actual
			while(n>=1): 
				for vec in self.vertices[act].vecinos: #Se verifican los vecinos del nodo actual
					if self.vertices[vec].nivel==n-1: #Si un nodo vecino cumple la condicion de tener un nivel menos que el actual 
						n-=1 #El nivel se vuelve menor, es decir se escala en la grafica
						recorrido.append(vec) #El nodo se agrega al recorrido
						act=vec #Ahora actual es el nodo al que nos movimos
		if b in recorrido: #Si b esta en la lista del recorrido, significa que se puede llegar a el desde a
			print("Camino")
			for i in recorrido:
				print(i)
		elif b not in recorrido: #Si b no esta en la lista, no se puede llegar a el desde a
			print("No existe un camino")
	def DFS(self,r,n):
		global a
		if r in self.vertices:
			self.vertices[r].visitado=True
			self.vertices[r].nivel=n
			#print(r,n)
			for v in self.vertices[r].vecinos:
				if self.vertices[v[0]].visitado == False:
					self.DFS(v[0],n+1)
			#self.vertices[r].a=a
			#print(self.vertices[r].a) 
			#a-=1
			#print("({},{})".format(self.vertices[r].id, self.vertices[r].a))
	def printtopo(self,r,n):
		global a
		if r in self.vertices:
			self.vertices[r].a=a
			print(self.vertices[r].a) 
			a-=1
			print("({},{})".format(self.vertices[r].id, self.vertices[r].a))
	def topoSort(self):
		global a 
		a=len(self.vertices)
		for v in self.vertices:
			if self.vertices[v].visitado == False:
				self.DFS(v,0)
			self.printtopo(v,0)
	def minimo(self,l):
		m=self.vertices[l[0]].costo
		v=l[0]
		for e in l:
			if m>self.vertices[e].costo:
				m=self.vertices[e].costo
				v=e
		return v
	def cdijktra(self,b):
		lis=[]
		if(self.vertices[b].padre==-1):
				print("No existe camino")
		else:
				lis.append(self.vertices[b].id)
				while(self.vertices[b].padre!=0):
						lis.append(self.vertices[b].padre)
						b=self.vertices[b].padre
				print(lis)
				print(self.vertices[b].costo)

	def dijktra(self,a,b):
		lista=[]
		self.vertices[a].costo=0
		self.vertices[a].padre=0
		for v in self.vertices[a].vecinos:
			self.vertices[v[0]].costo=v[1]
			self.vertices[v[0]].padre=self.vertices[a].id
			lista.append(v[0])
		while(len(lista)>0):
			m=self.minimo(lista)
			for vec in self.vertices[m].vecinos:
				if self.vertices[m].costo+vec[1]<self.vertices[vec[0]].costo:
					self.vertices[vec[0]].costo=self.vertices[m].costo+vec[1]
					self.vertices[vec[0]].padre=m
				if self.vertices[vec[0]].visitado==False:
					lista.append(vec[0])
			lista.remove(m)
			self.vertices[m].visitado=True
		self.cdijktra(b)
class main:
	g=graph()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarVertice(7)
	g.agregarArista(1,2,2)
	g.agregarArista(2,4,1)
	g.agregarArista(2,3,5)
	g.agregarArista(4,3,2)
	g.agregarArista(4,5,4)
	g.agregarArista(6,5,3)
	g.agregarArista(7,6,1)
	g.agregarArista(1,7,4)
	g.imprimirGrafica()
	#g.DFS(1,0)
	g.topoSort()	
	#g.dijktra(1,3)	
	#g.imprimirGrafica()
