#Alumnos:Arenas Olguin Jose Gerardo y Caballero Montanio Montserrat

import sys

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
			#print("BFS")
			#print("(",r,", ", 0,")",sep="",end=" ")
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
						#print("(",vec,", ",self.vertices[vec].nivel,")",sep="",end=" ")
		else:
			print("El vertice no existe")	
	def buscarCamino(self, n): #Metodo que dice el camino mas corto entre dos vertices
		#print("\n")
		camino=[] #Lista que guarda los nodos de camino
		queue=[] #Lista que va a interactuar con los nodos buscando el padre
		#Se agrega el nodo de salida a las dos listas 
		queue.append(n)
		camino.append(n)
		while len(queue)>0: #Cuando queue este vacia ya no hay mas opciones
			act=queue.pop(0)#Se saca el primer elemento como en una cola
			for vec in self.vertices[act].vecinos: #Se revisan los vecinos de ese elemento
				if self.vertices[vec].nivel==self.vertices[act].nivel-1: #Si encuentra al padre
					#Se va agregar ese elemento a las dos listas
					queue.append(vec)
					camino.append(vec)
					#Puede que haya otros vecinos que sean un nivel menor pero esos ya no se cuentan 
					break
		if len(camino)>1: #Si la lista de camino tiene otro nodo aparte de el del inicio
			#Se imprime el camino
			for i in range(len(camino)):
				print(camino[i])
		else: #Sino se dice que no existe 
			print("No existe camino")

class main:
	aristas=[] #Arreglo donde se aguardarán nuestras aristas
	aux=sys.stdin.read() #Se lee desde consola
	lista=aux.split("[") #Se separa en una lista cuando encuentre un corchete que abre
	#Va a haber dos espacios de la lista vacios que se quitan con remove
	lista.remove("")
	lista.remove("")
	#El primer elemento de la lista tiene todos los vertices 
	vertices=lista[0].split(", ") #Se separa cada uno de los vertices en una lista de ellos
	#El ultimo elemento  va a tener un corchete que cierra y un salto de linea que se remplazan por nada
	vertices[len(vertices)-1]=vertices[len(vertices)-1].replace("]\n","")
	
	for i in range(1,len(lista)-2): #Despues desde el segundo elemento hasta dos antes del ultimo...
		aux=lista[i].split(", ") #Se van a separar las aristas en listas
		aux.remove("")
		aux[1]=aux[1].replace("]", "") #En la segunada arista se le va a quitar ]
		aristas.append(aux) #Y se agrega a la lista de aristas
	#En el penultimo elemento se le quita ]]\n y se guarda en aristas 
	aux=lista[len(lista)-2].split(", ")
	aux[1]=aux[1].replace("]]\n", "")
	aristas.append(aux)
	#El ultimo elemento son otro par de aristas que al igual que las anteriores se le quita ] 
	aux=lista[len(lista)-1].split(", ")
	#El elemento 0 es el nodo de inicio y el 1 es la raiz
	raiz=aux[1].replace("]", "")
	nodo=aux[0]
	
	g=graph() #Se hace la instancia de la grafica
	#Se agregan los vertices y las aristas al diccionario
	for vert in vertices:
		g.agregarVertice(int(vert))
	for arist in aristas:
		g.agregarArista(int(arist[0]),int(arist[1]))
	#g.imprimirGrafica()
	g.BFS(int(raiz)) #Se hace la busqueda por expansion
	g.buscarCamino(int(nodo)) #Se busca el camino mas corto