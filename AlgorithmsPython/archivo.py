import os #modulo que permite acceder a funcionalidades dependientes del Sistema Operativo
def crearDirectorio(ruta):
    try:
        os.makedirs(ruta)#Crea un directorio a partir de la ruta dada
    except OSError:
        pass
    os.chdir(ruta)#cambia de directorio

dic={}#diccionario
a=open('perroschidos.txt','r') #abre el archivo en modo de lectura
l=a.readlines()
for reng in l: #se "suprimen" los saltos de linea, puntos y comas, y se separan las palabras
    reng=reng.replace('\n','')
    reng=reng.replace(',','')
    reng=reng.replace('.','')
    sl=reng.split()
    for i in sl: #se recorren todas las pallabras del texto
            if i not in dic.keys():#si no se encuentra la palabra en el diccionario, su ocurrencia sera de 1
                dic[i]=1
            else:#si la palabra ya estaba en el diccionario, a su ocurrencia se le anade uno
                dic[i]+=1
print(dic)
crearDirectorio('/home/alan/Escritorio/eda/p10/perronuevo')
for pal in dic.keys():
    print(pal)
    crearDirectorio('/home/alan/Escritorio/eda/p10/perronuevo/'+str(pal))#crea directorios para cada archivo creado por palabra del texto
    archivo=open(pal,'w')#abre el archivo en modo escritura
    archivo.write(pal+' '+str(dic[pal]))#escribe la palabra y su ocurrencia en su archivo y directorio correspondiente
    archivo.close #cierra el archivo
