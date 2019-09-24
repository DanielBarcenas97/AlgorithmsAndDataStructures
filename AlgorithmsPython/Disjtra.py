import sys
import math
class Vertex:
	def __init__(self, i):
		self.id = i
		self.visitado = False
		self.nivel = -1
		self.vecinos = []
		self.anterior = -1
		self.costo=float('inf')	
	def agregarVecino(self, v):
		if(v[0] not in self.vecinos):
			self.vecinos.append(v)
class graph:
	def __init__(self):
		self.vertices = {}
	def agregarVertice(self,v):
		if(v not in self.vertices):
			vert = Vertex(v)
			self.vertices[v] = vert
	def agregarArista(self, a,b,p):
		if(a in self.vertices and b in self.vertices):
			self.vertices[a].agregarVecino([b,p])
			#self.vertices[b].agregarVecino(a)
	def imprimirGrafo(self):
		print("Grafica: ")
		for v in self.vertices:
			print("Vertice: ", self.vertices[v].id,self.vertices[v].costo)
			print(self.vertices[v].vecinos)
	def BFS(self,r):
		if r in self.vertices:
			print("Estoy en la funcion de BEFOS")
			print(r,0)
			cola=[]
			cola.append(r)
			self.vertices[r].visitado = True
			self.vertices[r].nivel = 0
			while(len(cola) > 0):
				act = cola.pop(0)
				for vec in self.vertices[act].vecinos:
					if(self.vertices[vec].visitado == False):
						cola.append(vec)
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel = self.vertices[act].nivel+1
						print(vec, self.vertices[vec].nivel)
		else:
			print("El Vertice NO EXISTE.")

	def DFS(self,r,n):
		if r in self.vertices:
			self.vertices[r].visitado=True
			self.vertices[r].nivel=n
			print(r,n)
			for v in self.vertices[r].vecinos:
				if self.vertices[v[0]].visitado == False:
					self.DFS(v[0],n+1)

	def topoSort(self):
		n=len(self.vertices)
		for v in self.vertices:
			if self.vertices[v].visitado == False:
				self.DFS(v,0)
	def minimo(self,l):
		m = self.vertices[l[0]].costo
		v=l[0]
		for e in l:
			if m > self.vertices[e].costo:
				m = self.vertices[e].costo
				v=e
		return v	
				

	def dijkstra(self,a,b):
		lista = []
		self.vertices[a].costo = 0
		for v in self.vertices[a].vecinos:
			self.vertices[v[0]].costo = v[1]
			lista.append(v[0])
		while(len(lista)>0):
			m=self.minimo(lista)
			for vec in self.vertices[m].vecinos:
				if self.vertices[m].costo + vec[1] <  self.vertices[vec[0]].costo:
					self.vertices[vec[0]].costo = self.vertices[m].costo  + vec[1]
					self.vertices[vec[0]].anterior = m
				if self.vertices[vec[0]].visitado == False:
					lista.append(vec[0])
			lista.remove(m)
			self.vertices[m].visitado = True
		total = self.vertices[b].costo
		if(math.isinf(total)):
			print("No existe camino")
		else:
			aux = b
			camino=[]
			while(aux != -1):
				camino.append(aux)
				aux = self.vertices[aux].anterior
			camino.append(a)
			camino.reverse()
			print(camino)
			print(total)
			

class main:
    g=graph()
    vertices=input()
    aristas=input()
    w=input()
    
    vertices=vertices.split(",")
    vertices[0]=vertices[0][1:len(vertices[0])]
    vertices[len(vertices)-1]=vertices[len(vertices)-1][0:len(vertices[len(vertices)-1])-1]
    
    
    aristas=aristas.replace("[", "")
    aristas=aristas.replace("]", "")
    aristas=aristas.split(",")
    
    
    w=w.split(",")
    w[0]=w[0][1:len(w[0])]
    w[len(w)-1]=w[len(w)-1][0:len(w[len(w)-1])-1]
    
    for x in vertices:
        g.agregarVertice(int(x))
    
    for y in range(0, len(aristas), 3):
        g.agregarArista(int(aristas[y]), int(aristas[y+1]), int(aristas[y+2]))
    g.dijkstra(int(w[0]),int(w[1]))