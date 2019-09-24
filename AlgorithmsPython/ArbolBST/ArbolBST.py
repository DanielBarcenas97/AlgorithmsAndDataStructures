#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter import ttk, font
import getpass
 
# Gestor de geometría (place)
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

class Aplicacion():
    def __init__(self):
        self.ventana = Tk()
        # Define la dimensión de la ventana 
        self.ventana.geometry("600x300")
        self.ventana.title("Arbol BST")   
        c = Canvas(self.ventana,width=600,height=300)
        c.place(x=0,y=0)
        c.create_rectangle(0,0,600,300,fill="blue")
        #c.create_oval(120,120,200,200,fill="red")

        self.fuente=font.Font(family="Helvetica",size=12,weight="bold")
        self.etiq1=Label(self.ventana,text="ARBOL BST AUTOBALANCEADO",font=self.fuente).place(x=167, y=0)
        
        self.mensa = StringVar()
        self.mensa2 = StringVar()
        self.mensa3=StringVar()

        self.etiq3 = ttk.Label(self.ventana,text="Dato ingresado:",font=self.fuente, foreground='blue').place(x=50, y=35)
        self.etiq4 = ttk.Label(self.ventana,textvariable=self.mensa2,font=self.fuente, foreground='blue')
        self.etiq5 = ttk.Label(self.ventana,textvariable=self.mensa3,font=self.fuente, foreground='blue').place(x=50, y=300)
        
        self.insertar=IntVar()
        self.borrar=IntVar() #recibir datos de cajas de texto
        self.buscar=IntVar()            
        self.arbol = StringVar()

        self.Menu(self.ventana)
        boton1=Button(self.ventana,text="Obtener el  Min del BST.",command=self.obtenerMin).place(x=420,y=35) #crt shift d
        boton2=Button(self.ventana,text="Obtener el  Max del BST.",command=self.obtenerMax).place(x=420,y=65) #crt shift d
        boton3=Button(self.ventana,text="Altura   de   cada   nodo.",command=self.obtenerAl).place(x=420,y=95) #crt shift d
        boton4=Button(self.ventana,text="Vista   Previa   del  Arbol.",command=self.printingAr).place(x=420,y=125) #crt shift d

        self.etiq4.place(x=185, y=35)
        InsetarCaja=Entry(self.ventana,textvariable=self.insertar).place(x=135,y=67)
        botonI=Button(self.ventana,text="Insertar Dato",command=self.Insertar).place(x=50, y=65)

        BorrarCaja=Entry(self.ventana,textvariable=self.buscar).place(x=135,y=127)
        botonBu= Button(self.ventana,text="Buscar  Dato",command=self.Buscar).place(x=50, y=125)

        BuscarCaja=Entry(self.ventana,textvariable=self.borrar).place(x=135,y=97)
        botonBo= Button(self.ventana,text="Borrar   Dato",command=self.Borrar).place(x=50, y=95)

        ArbolCaja=Entry(self.ventana,textvariable=self.arbol).place(x=135,y=157)
        botonar= Button(self.ventana,text="Ingresa el arbol",command=self.ARB).place(x=35, y=155)
        # El método 'bind()' asocia el evento de 'hacer clic 
        # con el botón izquierdo del ratón en la caja de entrada
        # de la contraseña' expresado con '<button-1>' con el 
        # método 'self.borrar_mensa' que borra el mensaje y la 
        # contraseña y devuelve el foco al mismo control.
        # Otros ejemplos de acciones que se pueden capturar:
        # <double-button-1>, <buttonrelease-1>, <enter>, <leave>,
        # <focusin>, <focusout>, <return>, <shift-up>, <key-f10>, 
        # <key-space>, <key-print>, <keypress-h>, etc.
         
        #self.ctext2.bind('<button-1>', self.borrar_mensa)
        self.ventana.mainloop()
    def vent3(self,ventana):
        ventana.title("Arbol BST")
        ventana.geometry("500x500")
        c = Canvas(ventana,width=500,height=500)
        c.place(x=0,y=0)
        c.create_rectangle(0,0,500,500,fill="blue")
        c.create_oval(200,200,300,300,fill="red")


    def vent2(self,ventana):
        ventana.title("Arbol desde archivo")
        ventana.geometry("300x200")
        c = Canvas(ventana,width=300,height=200)
        c.place(x=0,y=0)
        c.create_rectangle(0,0,300,200,fill="blue")

    def GuardarArchivo(self):
        archivo=open("escri.txt","a+")
        l=self.ARB()
        archivo.write("["+l+"]")

    def AbrirArchivo(self):
        ventana= Tk()
        self.vent2(ventana)
        archivo=open("arb.txt","r")
        for linea in archivo:
            archivo.close
        l=linea
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        Estilo=font.Font(family="Helvetica",size=13,weight="bold")
        arbolito=Label(ventana,text="El arbol es:\n"+ str (l),font=Estilo ).place(x=80,y=60)
        self.arbol.set(str(l)) 
        return l

    def Menu (self,ventana):#menu
        barraMenu=Menu (ventana)
        mnuArchivo=Menu(barraMenu)
        mnuArchivo.add_command(label="Abrir desde archivo",command=self.AbrirArchivo)#arbolito=self.AbrirArchivo()          
        mnuArchivo.add_command(label="Guardar en archivo",command=self.GuardarArchivo)
        mnuArchivo.add_separator()
        mnuArchivo.add_command(label="Salir",command=ventana.destroy)
        barraMenu.add_cascade(label="Archivos",menu=mnuArchivo)
        ventana.config(menu=barraMenu)

    def Insertar(self):
        t=Arbol() 
        dato=self.insertar.get()
        print (self.insertar.get())
        self.mensa2.set(dato) 
        print ("agregar")

        l=self.arbol.get()
        print (l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        l.append(int(dato))
        t.crearArbol(l)
        t.altura(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz)


    def Borrar(self):
        t=Arbol()
        l=self.arbol.get()
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        print ("Borrar")
        clave=self.borrar.get()
        print (self.borrar.get())
        self.mensa2.set(clave) 

        t=Arbol()
        l=t.eliminar(lista,clave)
        t.crearArbol(l)
        t.altura(t.raiz)
        t.printing(t.raiz)   
        l=int (a3[0])
        print ("")
        t.rotar(t.vertices[l])
        t.balanceBST(t.vertices[l])
        t.altura(t.raiz)
        t.printing(t.raiz)  
 
    def Buscar(self):
        t=Arbol() 
        
        l=self.arbol.get()
        print (l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        t.crearArbol(l)
        t.altura(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz)
        print("busqueda")
        clave=self.buscar.get()
        self.mensa2.set(clave) 
        print (clave)
        #print(t.buscar(t.raiz,clave))
        bus=t.buscar(t.raiz,clave)

    def ARB(self):
        t=Arbol()
        l=self.arbol.get()
        print (l)
        self.mensa2.set(l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        t.crearArbol(l)
        t.altura(t.raiz)
        #t.printing(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz) 
        #self.mensa3(t.printing(t.raiz))
        return self.arbol.get()

    def obtenerAl(self):
        t=Arbol()
        l=self.arbol.get()
        print (l)
        self.mensa2.set(l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        t.crearArbol(l)
        t.altura(t.raiz)
        #t.printing(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz) 
        #self.mensa3(t.printing(t.raiz))
        return self.arbol.get()
    
    def obtenerMin (self):
        t=Arbol()
        l=self.arbol.get()
        print (l)
        self.mensa2.set(l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        t.crearArbol(l)
        t.altura(t.raiz)
        #t.printing(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz)
        print ("min heap")
        x=1000
        t.min(t.raiz,x)

    def obtenerMax (self):
        t=Arbol()
        l=self.arbol.get()
        print (l)
        self.mensa2.set(l)
        l=l.strip('[')
        l=l.strip(']')
        l=l.split(',')
        l=list(map(int,l))
        lista=l
        t.crearArbol(l)
        t.altura(t.raiz)
        #t.printing(t.raiz)
        li=int (a3[0])
        t.rotar(t.vertices[li])
        t.balanceBST(t.vertices[li])
        t.altura(t.raiz)
        t.printing(t.raiz)
        print ("max heap")
        t.max(t.raiz,0)


    def Funciones (self,current):

        if current != None:
            self.printing(current.hizq)
            if current.id != 0:
                print("("+str(current.id)+", "+str(current.altura)+")")

            self.printing(current.hder)

    def printingAr (self):
        ventana= Tk()
        self.vent3(ventana)
        c = Canvas(ventana,width=500,height=500)
        c.place(x=0,y=0)
        c.create_rectangle(0,0,500,500,fill="blue")
        Estilo=font.Font(family="Helvetica",size=13,weight="bold")
        l=self.ARB()
        arbolito=Label(ventana,text="El arbol es:\n"+ str (l),font=Estilo ).place(x=200,y=60)
        c.create_oval(100,100,150,150,fill="red")
        


        return l
 
def main():
    mi_app = Aplicacion()
 
if __name__ == '__main__':
    main()