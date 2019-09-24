import sys

class vertex:
    def __init__(self, i):
        self.id 	= i
        self.visitado 	= False
        self.nivel 	= -1
        self.vecinos 	= []

    def agregarVecino(self, v):
        if(v not in self.vecinos): #NOT
            self.vecinos.append(v)
    
    #def borrarVecinos(self, v):

    
class graph:
    def __init__(self,):
        self.vertices = {}
    def agregarVertice(self, v):
        if v not in self.vertices:
            vert 		 = vertex(v)
            self.vertices[v] = vert
        

    def agregarArista(self,a,b):
        if (a in self.vertices and b in self.vertices):
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a) 

    def imprimirGrafica(self):
        print("Grafica: ")
        for v in self.vertices:
            print("Vertices: ", self.vertices[v].id)
            print("Aristas: ", self.vertices[v].vecinos)		

    def BFS(self, r):
        if( r in self.vertices):
            cola = []
            cola.append(r)
            self.vertices[r].visitado = True
            self.vertices[r].nivel = 0
            #print(r,0) #primera linea bonita
            while(len(cola)>0):
                act = cola[0]
                cola = cola[1:]
                for vec in self.vertices[act].vecinos:
                    if(self.vertices[vec].visitado == False):
                        
                        cola.append(vec)
                        self.vertices[vec].visitado = True
                        self.vertices[vec].nivel = self.vertices[act].nivel +1
                        #print(vec, self.vertices[vec].nivel ) 
        else:
            print("Vertice no existe")	

    
    def _BFS(self,root,target):
        
        self.BFS(target)                    #Ordenamos respecto al target
        if self.vertices[root].nivel == -1: #Checamos si es disxcoexa
            print("No existe camino")
        else:

            actual = root                   
            l = []                          #path auxiliar de nodos
            l.append(actual)

            while actual != target:
                    #empezaremos desde el SOURCE hacia el TARGET
                for vec in self.vertices[actual].vecinos:
                    #Solo nos interesan los vecinos superiores en nivel, porque
                    #queremos llegar a la raiz que es nuestro target
                    if self.vertices[vec].nivel == self.vertices[actual].nivel -1:
                        l.append(vec)
                        actual = vec
            
            for i in reversed(l):       #imprimir el PATH de atras a adelante.
                print (i)

class main:

    arr = []
    for line in sys.stdin:
        arr.append(line)
                
                
    nodes   = arr[0].replace("[","").replace("]","")
    vertex  = arr[1]
    root    = arr[2].replace("[","").replace("]","")
    # extracting useful data (could be more efficient)
    root = root.split(',')
    root = list(map(int,root))

    nodes   = nodes.split(',')
    nodes   = list(map(int, nodes))
    
    first   = vertex.index('[')
    last    = vertex.rindex(']')
 
    
    vertex = vertex[first+2:]
    vertex = vertex[:last-3]
    vertex = vertex.split('], [')
    #print(vertex)

    #print(root)

    g = graph()

    for item in nodes:
        #print(item)
        g.agregarVertice(item)

    for pair in vertex:
        
        pair = pair.split(',')
        pair = list(map(int,pair))
        
        g.agregarArista(pair[0],pair[1])

    
    #g.imprimirGrafica()
    g._BFS(root[1],root[0])

    