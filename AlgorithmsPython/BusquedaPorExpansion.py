import sys

#para la clase vertice

class vertex:  #nombre de la clase

	def __init__ (self,i):  #creamos un constructor que recibe un nombre
		self.id=i #para cambiar los valores, tipo this.  
		self.visitado=False
		self.nivel=-1  #para decir que esta en el nivel 0
		self.vecinos=[]

	def agregarVecino(self, v):  #self siempre se agrega
		if v not in self.vecinos:  #para no repetir al mismo vecino
			self.vecinos.append(v)

#para la clase grafica
class  graph:
	def __init__ (self):
		self.vertices={} # creamos un diccionario
	def agregarVertice (self, v):
		if v not in self.vertices:  #ya que no puede haber dos nombres iguales en un diccionario
			vert = vertex(v)  #creamos un objeto de tipo vertice
			self.vertices[v] = vert  #localidad a asignar el objeto (v) mediante su nombre 

	def agregarArista ( self,a, b): #recibe 2 vertices
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a)
        
	def imprimirGrafica (self):
		print("Grafica: ")
		
		for v in self.vertices:
			print ("Vertice: ",self.vertices[v].id)  #objeto del diccionario
			print("adyacencia ",self.vertices[v].vecinos)
	def BFS (self,r):  #
		if r in self.vertices:
			print ("("+str(r)+", "+"0)")
			cola=[]
			cola.append(r)
			self.vertices[r].visitado=True
			self.vertices[r].nivel=0  #nivel del padre
			while (len(cola)>0):
				act = cola[0]
				cola=cola[1:]
				for vec in self.vertices[act].vecinos:
					if self.vertices[vec].visitado == False:
						#print(vec)
						cola.append(vec)
						self.vertices[vec].visitado=True
						self.vertices[vec].nivel=self.vertices[act].nivel+1
						print("({0}, {1})".format(vec, self.vertices[vec].nivel))



class main:
    g=graph()
    
    vertices=input()
    aristas=input()
    verticeP=int(input())
    
    vertices=vertices.split(",")
    vertices[0]=vertices[0][1:len(vertices[0])]
    vertices[len(vertices)-1]=vertices[len(vertices)-1][0:len(vertices[len(vertices)-1])-1]
    
    
    aristas=aristas.replace("[", "")
    aristas=aristas.replace("]", "")
    aristas=aristas.split(", ")
    
    for v in vertices:
        g.agregarVertice(int(v))
    
    for a in range(0, len(aristas), 2):
        g.agregarArista(int(aristas[a]), int(aristas[a+1]))
    g.BFS(verticeP)