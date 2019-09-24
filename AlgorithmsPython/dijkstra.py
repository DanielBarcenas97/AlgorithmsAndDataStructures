class vertex:
	def __init__(self, i):
		self.id = i #self es como el this de java
		self.visitado = False
		self.nivel = -1 #raiz
		self.vecinos = []
		self.costo = float("inf") ###########
		self.antecesor = -1

	def agregarVecino(self, v):
		if v[0] not in self.vecinos: #para flojos que no quieren iterar ###########
			self.vecinos.append(v)

class graph:
	def __init__(self):
		self.vertices = {}
	
	def agregarVertice(self, v):
		if v not in self.vertices:
			vert = vertex(v) #instancia de clase vertice y la asigna a vert
			self.vertices[v] = vert #la llave es v
	
	def agregarArista(self, a, b, p):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino([b, p]) ###########
			#self.vertices[b].agregarVecino(a) ###########
	
	def imprimirGrafica(self):
		print("Grafica: ")
		for v in self.vertices:
			print("Vertice: ", self.vertices[v].id, self.vertices[v].costo)
			print(self.vertices[v].vecinos)
	
	def DFS(self, r, n):
		if r in self.vertices:
			self.vertices[r].visitado = True
			self.vertices[r].nivel = n
			print(r, n)
			for v in self.vertices[r].vecinos:
				if self.vertices[v[0]].visitado == False:
					self.DFS(v[0], n+1) #v es una tupla de [id, costo]

	def topoSort(self):
		n = len(self.vertices)
		for v in self.vertices:
			if self.vertices[v].visitado == False:
				self.DFS(v, 0)

	def minheap(self, l, i):
		if(2*i+1 <= len(l)-1):
			if(self.vertices[l[2*i]].costo < self.vertices[l[2*i+1]].costo):
				min = 2*i 
			else:
				min = 2*i+1
				if(self.vertices[l[i]].costo > self.vertices[l[min]].costo):
					aux = l[i]
					l[i] = l[min]
					l[min] = aux
					self.minheap(l,min)

		elif(2*i <= len(l)-1):
			if(self.vertices[l[i]].costo > self.vertices[l[2*i]].costo):
				aux = l[i]
				l[i] = l[2*i]
				l[2*i] = aux
				self.minheap(l,2*i)
		return l

	def camino(self, r, c):
		if(r != -1):
			self.camino(self.vertices[r].antecesor,c)
			c.append(int(r))
		return c
			
	def dijkstra(self,a,b):
		lista = [] #Vertices que se van a evaluar
		self.vertices[a].costo = 0  #a[0]
		for v in self.vertices[a].vecinos:  #a[0]
			self.vertices[v[0]].costo = v[1]
			lista.append(v[0])
		while(len(lista) > 0):
			#m = self.minimo(lista)
			minimo = self.minheap(lista,0)
			m = minimo[0]
			for vec in self.vertices[m].vecinos:
				if self.vertices[m].costo + vec[1] < self.vertices[vec[0]].costo:
					self.vertices[vec[0]].costo = self.vertices[m].costo + vec[1]
					self.vertices[vec[0]].antecesor = m
					if self.vertices[vec[0]].visitado == False:
						lista.append(vec[0])
			lista.remove(m)
			self.vertices[m].visitado = True #Para que no se vuelva a agregar a lista
		c=[]
		c.append(int(a))

		if (self.vertices[b].visitado == True):
			c=self.camino(b, c)
			print(c)
			print(self.vertices[b].costo)
		else:
			print("No existe camino")
	
#----------main---------------------------------------------
l = []
for i in range(3):
    l.append(input())
    
#primera linea    
l[0] = l[0][1:len(l[0])-1]
l[0] = l[0].split(", ")

#segunda linea
l[1] = l[1][1:len(l[1])-2]
l[1] = l[1].split("], ")

#lista de lista
for i in range(len(l[1])):
    l[1][i] = l[1][i][1:]
    l[1][i] = l[1][i].split(", ")
    
#lista 3
l[2] = l[2][1:len(l[2])-1]
l[2] = l[2].split(", ")
#print(l[2])
#----------
g = graph()

for i in l[0]:
    g.agregarVertice(i)
    
for i in l[1]:
    g.agregarArista(i[0],i[1],int(i[2]))
    
#g.imprimirGrafica()
g.dijkstra(l[2][0],l[2][1])