
class vertex:

	def __init__(self,i): #Constructor
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]
		#self.costo=9999999

	def agregarVecino(self,v):
		if v not in self.vecinos:
			self.vecinos.append(v)


	def eliminarVecino(self,v):#Pasar a graph, recibe vertices
		if v in self.vecinos:
			self.vecinos.remove(v)

class graph:
	d =[]
	def __init__(self):
		self.vertices={}

	def agregarVertice(self,v): #instanciar a la clase para generar un objeto
		if v not in self.vertices:
			vert=vertex(v) #instancia de la clase vertex
			self.vertices[v]=vert #Agregar el objeto al diccionario
	
	def agregarArista(self,a,b):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b)
			#self.vertices[b].agregarVecino(a)		
	
	def imprimirGrafica(self):
		print("Grafica: ")
		for v in self.vertices:
			print("Vertice, costo: ", self.vertices[v].id, self.vertices[v].costo)
			print(self.vertices[v].vecinos)
            
	def DFS(self, r):
		if r in self.vertices:
			self.vertices[r].visitado = True
			#self.vertices[r].nivel = n
			for v in self.vertices[r].vecinos:
				if self.vertices[v].visitado == False:
					self.DFS(v)
					self.d.append([v,self.n])
					self.n = self.n -1
                
	def topoSort(self):
		self.n = len(self.vertices)
		for v in self.vertices:
			if self.vertices[v].visitado == False:
				self.DFS(v)
				self.d.append([v,self.n])
				self.n = self.n -1
                
class main:
	g=graph()
    
	v=input()
	a=input()
    
	v=v.split(",")
	v[0]=v[0][1:len(v[0])]
	v[len(v)-1]=v[len(v)-1][0:len(v[len(v)-1])-1]   
	for i in range(len(v)):
		v[i] = int(v[i])
          
	a=a.replace("[", "")
	a=a.replace("]", "")
	a=a.split(",")
	for i in range(len(a)):
		a[i] = int(a[i])
    
	for x in v:
		g.agregarVertice(x)
    
	for y in range(0, len(a), 2):
		g.agregarArista(a[y], a[y+1])
        
	g.topoSort()
	#print(a)
	#print(v)
	for i in g.d:
		print("({0}, {1})".format(i[0], i[1]))
	#g.imprimirGrafica()