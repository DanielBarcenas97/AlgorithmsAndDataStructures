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
            print("("+str(r)+", "+str(0)+")" ) #primera linea bonita
            while(len(cola)>0):
                act = cola[0]
                cola = cola[1:]
                for vec in self.vertices[act].vecinos:
                    if(self.vertices[vec].visitado == False):
                        
                        cola.append(vec)
                        self.vertices[vec].visitado = True
                        self.vertices[vec].nivel = self.vertices[act].nivel +1
                        print("("+str(vec)+", "+ str(self.vertices[vec].nivel)+")" ) 
        else:
            print("Vertice no existe")	


class main:

    arr = []
    for line in sys.stdin:
        arr.append(line)
                
                
    nodes   = arr[0].replace("[","").replace("]","")
    vertex  = arr[1]
    root    = int( arr[2])
    # extracting useful data (could be more efficient)
    nodes   = nodes.split(',')
    nodes   = list(map(int, nodes))
    
    first   = vertex.index('[')
    last    = vertex.rindex(']')
 
    
    vertex = vertex[first+2:]
    vertex = vertex[:last-3]
    vertex = vertex.split('], [')
    #print(vertex)
    g = graph()

    for item in nodes:
        #print(item)
        g.agregarVertice(item)

    for pair in vertex:
        
        pair = pair.split(',')
        pair = list(map(int,pair))
        
        g.agregarArista(pair[0],pair[1])

    
    #g.imprimirGrafica()
    g.BFS(root)

    