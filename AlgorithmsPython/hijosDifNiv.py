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
            print(act.id,act.altura)
            self.imprimir(act.hder)

    def altura(self,act):
        if(act != None):
            a1 = self.altura(act.hizq)
            a2 = self.altura(act.hder)
            act.altura = max([a1,a2]) + 1 
            return(act.altura)
        else:
            return(-1)
            
    def RR(self,act):
        nr = act.hizq
        act.hizq = nr.hder
        nr.hder = act
        nr.padre = act.padre
        act.padre = nr
        if(act.hizq != None):
            act.hizq.padre = act
        if(nr.padre != None):
            nr.padre.hizq = nr
        if(self.raiz == act):
            self.raiz = nr
            
    listaPadresHijosDes = []
    def hijosDesNivelados(self,act):
        # print("estoy con: ",act.id)
        
        if(act.hizq != None and act.hder != None ): # QUE TENGA LOS DOS HIJOS
            if(abs(abs(act.hizq.altura) - abs(act.hder.altura)) >= 2):
                # print("El padre tine sus hijos desvalanceadso : ",act.id)
                self.listaPadresHijosDes.append(act.id)
            self.hijosDesNivelados(act.hizq)
            self.hijosDesNivelados(act.hder)
            
        if(act.hizq != None and act.hder == None): # QUE SOLO TENGA HIJO HIZQUIERDO
            if(abs(abs(act.hizq.altura) + 1) >= 2):
                # print("El padre tine sus hijos desvalanceadso : ",act.id)
                self.listaPadresHijosDes.append(act.id)
            self.hijosDesNivelados(act.hizq)
            
        if(act.hizq == None and act.hder != None): # QUE SOLO TENGA HIJO DERECHO
            if(abs(abs(act.hder.altura) + 1 ) >= 2):
                # print("El padre tine sus hijos desvalanceadso : ",act.id)
                self.listaPadresHijosDes.append(act.id)
            self.hijosDesNivelados(act.hder)
            
        self.listaPadresHijosDes.sort()
        return(self.listaPadresHijosDes)
        

class main:
    
    
    for line in sys.stdin.readlines():
        line = line.replace('[','')
        line = line.replace(']','')
        line = line.split(',')
        line = list(map(int,line))
        laux = list(map(int,line))
    arb = laux

    t = arbol()
    t.crearArbol(arb)
    t.altura(t.raiz)
    print(t.hijosDesNivelados(t.raiz))