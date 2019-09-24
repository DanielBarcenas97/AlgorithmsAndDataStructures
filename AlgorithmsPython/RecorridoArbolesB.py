arb=[]
arb2=[]

def infix(p):
    if len(arb)-1>=2*p:
        infix(2*p)
    arb2.append(arb[p])
    if len(arb)-1>=2*p+1:
        infix(2*p+1)

def prefix(p):
    arb2.append(arb[p])
    if len(arb)-1>=2*p:
        prefix(2*p)
    if len(arb)-1>=2*p+1:
        prefix(2*p+1)

def posfix(p):
    if len(arb)-1>=2*p:
        posfix(2*p)
    if len(arb)-1>=2*p+1:
        posfix(2*p+1)
    arb2.append(arb[p])
    
        
class main:
   
    i=input()
    i=i.replace("[", "")
    i=i.replace("]", "")
    i=i.split(",")

    for x in i:
        arb.append(int(x))
    
    infix(1)
    print(arb2)
    del(arb2[:])
    prefix(1)
    print(arb2)
    del(arb2[:])
    posfix(1)
    print(arb2)
    del(arb2[:])