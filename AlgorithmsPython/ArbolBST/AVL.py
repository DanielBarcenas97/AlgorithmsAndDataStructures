a3=[]
class Vertex:
    def __init__(self,vertex):
            self.id=vertex #vertice == id
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
            if current.id != 0:
                print("("+str(current.id)+", "+str(current.altura)+")")
            self.printing(current.hder)

    def buscar(self,current,clave):
        if current == None:
            print ("No existe Arbol")
        if current != None:
            if int(current.id) == int (clave):
                print("("+str(current.id)+", "+str(current.altura)+")")
            elif int (clave) <int (current.id):
                return self.buscar(current.hizq,clave)
            elif int (clave)>int (current.id):
                return self.buscar(current.hder,clave)
            else:
                ("No encontrado")

    def eliminar(self,lista,clave):
        print(lista)
        lista.remove(clave)
        return lista
   



    def min(self,current,aux):
        if current != None:
            if int (current.id) < int (aux):
                aux=current.id
                if current.hizq==None: 
                    print("("+str(current.id)+", "+str(current.altura)+")")
                else:
                    current=current.hizq
                    if current.hizq==None:
                        print("("+str(current.id)+", "+str(current.altura)+")")
                        return 0
                    else:
                        return self.min(current,aux)

    def max(self,current,aux):
        if current != None:
            if int (current.id) > int (aux):
                aux=current.id
                if current.hder==None: 
                    print("("+str(current.id)+", "+str(current.altura)+")")
                else:
                    current=current.hder
                    if current.hder==None:
                        print("("+str(current.id)+", "+str(current.altura)+")")
                        return 0
                    else:
                        return self.max(current,aux)



    def altura(self, current):
        if current!=None:
            global a3
            a1=self.altura(current.hizq)
            a2=self.altura(current.hder)
            current.altura=max([a1,a2])+1
            if a1-a2>1:
                a3.append(current.id)
            if a2-a1>1:
                a3.append(current.id)
            a3.sort()
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

    l=input()
    l=l.strip('[')
    l=l.strip(']')
    l=l.split(',')
    l=list(map(int,l))
    lista=l
    t.crearArbol(l)
    t.altura(t.raiz)
    t.printing(t.raiz)   

    l=int (a3[0])
    print(a3)
    t.rotar(t.vertices[l])
    t.balanceBST(t.vertices[l])
    t.altura(t.raiz)
    t.printing(t.raiz)   
    
    #print("busqueda")
    #clave=input()
    #print(t.buscar(t.raiz,clave))
    #t.buscar(t.raiz,clave)

    #print ("agregar")
    #dato=(5)
    #t.agregarVertice(dato)
    #l=input()
    #l=int(l)
    #t.rotar(t.vertices[l])
    #t.balanceBST(t.vertices[l])
    #t.altura(t.raiz)
    #t.printing(t.raiz) 

    #print ("min heap")
    #x=1000
    #t.min(t.raiz,x)

    #print ("max heap")
    #t.max(t.raiz,0)

    print("borrar")
    print("indica el elemento a borrar")
    clave=int (input("clave"))
    t=Arbol()
    l=t.eliminar(lista,clave)
    t.crearArbol(l)
    t.altura(t.raiz)
    t.printing(t.raiz)   

    l=int (a3[0])
    #print(a3)
    print ("")
    t.rotar(t.vertices[l])
    t.balanceBST(t.vertices[l])
    t.altura(t.raiz)
    t.printing(t.raiz)   
    

    
