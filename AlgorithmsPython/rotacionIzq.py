import sys
class vertex:
    def __init__(self,v):
        self.id = v
        self.padre = None
        self.hizq = None
        self.hder = None
        self.altura = -1
class arbol:
    def __init__(self):
        self.raiz = None
    
    def agregar(self,act,ver):
        if(act.id < ver.id):
            if(act.hder != None):
                self.agregar(act.hder,ver)
            else:
                act.hder = ver
                ver.padre = act
                
        else:
            if(act.hizq != None):
                self.agregar(act.hizq,ver)
            else:
                act.hizq = ver
                ver.padre = act
                
                

    def agregarVertice(self,v):
        ver = vertex(v)
        if(self.raiz == None):
            self.raiz = ver
        else:
            self.agregar(self.raiz,ver)

    def crearArbol(self,lista):
        for i in range(len(lista)):
            self.agregarVertice(lista[i])

    def imprimir(self,act):
        if(act != None):
            self.imprimir(act.hizq)
            print((act.id,act.altura))
            self.imprimir(act.hder)

    def altura(self,act):
        if(act != None):
            a1 = self.altura(act.hizq)
            a2 = self.altura(act.hder)
            act.altura = max([a1,a2]) + 1 
            return(act.altura)
        else:
            return(-1)
            
    def bus(self,act,nodo):
        if(act != None):
            if(act.id == nodo):
                prodigio = act
                # print("ya lo encontre",prodigio.id)
                self.RR(prodigio)
                
            self.bus(act.hder,nodo)
            self.bus(act.hizq,nodo)
        
    def RR(self,act):
        nr = act.hder
        act.hder = nr.hizq
        nr.hizq = act
        nr.padre = act.padre
        act.padre = nr
        if(act.hder != None):
            act.hder.padre = act
        if(nr.padre != None):
            nr.padre.hder = nr
        if(self.raiz == act):
            self.raiz = nr
            
 
        

class main:

    t = arbol()
    
    arr = []
    for line in sys.stdin:
        arr.append(line)
    arb = arr[0].replace("[","").replace("]","").replace("\n","").split(",")
    arb=list(map(int,arb))
    
    nodX = arr[1]
    
    t = arbol()
    t.crearArbol(arb)
    t.altura(t.raiz)
    t.bus(t.raiz,int(nodX))
    t.altura(t.raiz)
    t.imprimir(t.raiz)