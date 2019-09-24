class Vertex: #Clase vertice (molde de o plantilla)
	def __init__(self, i): #Metodo constructor de la clase vertices
		#Atributos de instancia
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]
	def agregarVecino(self, v): #Metodo que agrega a la lista de vecinos estos
		if v not in self.vecinos: #Se verifica que el vecino no se encuentre en la lista para no repetir
			self.vecinos.append(v)

class graph: #Clase grafica
	def __init__(self): #Metodo constructor
		self.vertices={} #Diccionario de vertices
	def agregarVertice(self, v): #Metodo de agregar vertices al diccionario
		if v not in self.vertices:
			vert=Vertex(v)
			self.vertices[v]=vert
	def agregarArista(self, a, b): #Metodo que agrega una arista
		if a in self.vertices and b in self.vertices: #Se verifica que ambos vertices estén en nuestro diccionario 
			#Se agrega cada vertice a la lista de vecinos de el otro
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a)
	def imprimirGrafica(self): #Metodo que imprime la grafica 
		print("Grafica: ")
		for v in self.vertices: #Por cada vertice que haya en la tabla hash
			#Se muestra el id y sus vecinos
			print("Vertices: ",self.vertices[v].id)
			print(self.vertices[v].vecinos)
	def BFS(self, r): #Metodo de busqueda por expansion 
		if r in self.vertices: #Si el vertice si esta en el diccionario se puede busca si no se manda un mensaje avisando que no
			print("BFS")
			print("(",r,", ", 0,")",sep="")
			cola=[] #Se declara la cola (FIFO)donde se almacenaran los nodos que se van a revisar
			cola.append(r)# Se agrega el primero que será la raiz
			self.vertices[r].visitado=True #Se actualiza a visitado
			self.vertices[r].nivel=0 #Y se le pone su nivel(como es la raiz es cero)
			while(len(cola)>0): #Lo siguiente se tiene que hacer hasta que la cola quede vacia
				act=cola[0] #Se saca un elemento de la cola
				cola=cola[1:] #Se actualiza
				for vec in self.vertices[act].vecinos: #Se van a revisar todos los vecinos de ese nodo
					if self.vertices[vec].visitado == False: #Si el vecino no ha sido visitado ...
						cola.append(vec) #Se agrega a la cola
						self.vertices[vec].visitado=True #Se actualiza a visitado
						self.vertices[vec].nivel=self.vertices[act].nivel + 1 #Se le agrega su nivel que es uno más que su padre
						print("(",vec,", ",self.vertices[vec].nivel,")",sep="") #Se imprime la informacion
		else:
			print("El vertice no existe")	

class main: #Main de nuestro programa
	v=[2, 46, 164, 76, 128, 36, 183, 156, 58, 70] #Lista de vertices
	#Lista de aristas
	a=[[76, 46], [46, 156], [183, 164], [70, 156], [2, 164], [2, 164], [76, 164], [76, 2], [128, 46], [58, 46], [164, 128], [46, 128], [2, 128]]
	r="46" #Nuestra raiz
	g=graph() #Se hace la instancia de la grafica
	#Se agregan los vertices y las aristas al diccionario
	for vert in v:
		g.agregarVertice(vert)
	for arist in a:
		g.agregarArista(arist[0],arist[1])
	#g.imprimirGrafica()
	#Se hace la busqueda por expansion
	g.BFS(int(r))	