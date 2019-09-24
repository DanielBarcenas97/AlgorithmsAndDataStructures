class Vertex:
    def __init__(self,vertex):
            self.id=vertex
            self.padre=None
            self.hizq=None
            self.hder=None
            self.altura=-1
            self.parent=None

class Arbol:
    def __init__(self):
        self.raiz=None
        self.nodesToRotate=[]
        self.vertices={}

    def agregar(self,current,vertex):
        if current.id < vertex.id :
            if current.hder != None:
                self.agregar(current.hder,vertex)
            else:
                vertex.parent=current
                current.hder=vertex #asigno al objeto de la clase vertex hder al vertex
        else:
            if current.hizq != None:
                self.agregar(current.hizq,vertex)
            else:
                vertex.parent=current
                current.hizq=vertex


    def agregarVertice(self,v):

        vertex=Vertex(v)
        self.vertices[v]=vertex
        if self.raiz == None :
            self.raiz=vertex
        else:
            self.agregar(self.raiz,vertex)

    def crearArbol(self,listOfVertices):
        for value in listOfVertices:
            self.agregarVertice(value)


    def printing(self,current):
        if current != None:
            self.printing(current.hizq)
            print("("+str(current.id)+", "+str(current.altura)+")")
            self.printing(current.hder)

    def altura(self,current):
        #post orden
        if current != None:
            a1=self.altura(current.hizq)
            a2=self.altura(current.hder)
            current.altura=max([a1,a2])+1
            return current.altura
        else:
            return -1

    def rotar(self,current):
        if current != None:

            if current.hizq != None:
                hIzq=current.hizq.altura
            else:
                hIzq=-1

            if current.hder != None:
                hDer=current.hder.altura
            else:
                hDer=-1

            balanceFactor=abs(hIzq - hDer)
            #print("balance de "+str(current.id),balanceFactor)
            if balanceFactor > 1:
                #print("posibble node",current.id)
                self.nodesToRotate.append(current)
            self.rotar(current.hizq)
            self.rotar(current.hder)

    def rr(self,current):
        newroot=current.hizq
        current.hizq=newroot.hder
        newroot.hder=current
        newroot.parent=current.parent
        current.parent=newroot
        if current.hizq != None:
            current.hizq.parent=current
        if newroot.parent != None :
            newroot.parent.hizq=newroot
        if self.raiz == current:
            self.raiz=newroot

    def ll(self,current):
        newroot=current.hder
        current.hder=newroot.hizq
        newroot.hizq=current
        newroot.parent=current.parent
        current.parent=newroot
        if current.hder != None:
            current.hder.parent=current
            #asignar al nodo cambiado el nuevo padre
        if newroot.parent != None:
            newroot.parent.hder=newroot
            #asignar si no es la raiz el nodo rrotado asignarle a la raiz ese nodo
        if self.raiz == current:
            self.raiz=newroot
            #si el nodo rotado se convierto la raiz cambiar la raiz
            
    def balanceBST(self,current):
        if current in self.nodesToRotate:
            for i in self.nodesToRotate:
                #print(i.id)
                if i.hizq == None:
                    self.ll(i)

                elif i.hder == None:
                    self.rr(i)

                elif(i.hizq.altura < i.hder.altura):
                    self.ll(i)
                elif(i.hder.altura > i.hizq.altura):
                    self.rr(i)

        

class Main:
    t=Arbol()
    for i in range(2):
        if i == 0:
            l=input()
            l=l.strip('[')
            l=l.strip(']')
            l=l.split(',')
            l=list(map(int,l))
            t.crearArbol(l)
            t.altura(t.raiz)

        if i==1:
            l=input()
            l=int(l)
            t.rotar(t.vertices[l])
            t.balanceBST(t.vertices[l])
            t.altura(t.raiz)
            t.printing(t.raiz)   