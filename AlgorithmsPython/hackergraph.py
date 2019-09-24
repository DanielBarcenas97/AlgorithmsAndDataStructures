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

	for i in range(1,len(lista)-1): #Desde el elemento 1 hasta el ultimo van a estar las aristas pero en este for no contaremos el ultimo elemento
		aux=lista[i].split(", ") #Se separan cada par de vertices
		aux.remove("") #Va a haber un espacio vacio en la lista auxiliar que se quita
		aux[1]=aux[1].replace("]", "") #Se remplaza el corchete que cierra que tiene e último elemento por nada
		aristas.append(aux) #Y se a agrega a la lista de aristas
	#El ultimo elemento de la primera lista va a tener a la ultima arista y a la raiz
	aux=lista[len(lista)-1].split(", ") #Se va a separar en una lista...
	#Y el ultimo elemento de esa nueva lista va a tener a un vertice y a la raiz...
	aux[1]=aux[1].replace("]]\n", " ") #Se remplaza ]]\n por un espacio en blanco...
	aux2=aux[1].split(" ") #Y luego eso se separa en otra lista aux
	aux[1]=aux2[0] #El nodo que falta se pone junto con el otro
	aristas.append(aux) #Y se agrega esa arista a su lista
	raiz=int(aux2[1]) #LA raiz se pone en una variable con su nombre

	g=graph() #Se crea la instancia de la grafica
	for vert in vertices: #Se agregan los vertices a la grafica
		g.agregarVertice(int(vert))
	for arist in aristas: #Se agregan las aristas a la grafica
		g.agregarArista(int(arist[0]),int(arist[1]))
	#g.imprimirGrafica()
	g.BFS(int(raiz)) #Se hace la busqueda por expansion 