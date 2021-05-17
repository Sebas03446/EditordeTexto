
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


# CREACIÓN DE CLASE COLA (FIFO)

class Queue:
    
    #LA COLA DEBE INICIAR VACÍA, DECLARANDOSE ANTES DE SU USO SIN NINGÚN PARAMETRO
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
    
    
    #LA FUNCIÓN enqueue AGREGA UN VALOR AL FINAL DE LA COLA, REQUIERE UN VALOR
    def enqueue(self, value):
        aux = Node(value)
        if(self.head.value == None):
            self.head = aux
            self.tail = aux
        else:
            self.tail.next = aux
            self.tail = aux
    
    #LA FUNCIÓN dequeue REGRESA EL PRIMER VALOR DE LA COLA, SACANDOLO DE ESTA.
    def dequeue(self):
        aux = self.head
        if (self.head == None):
            print("Empty Queue")
            return None
        else:
            self.head = self.head.next
            return aux

    #LA FUNCIÓN is_empty REGRESA UN BOOLEANO, TRUE SI ESTÁ VACÍA, FALSE SI TIENE ALGUN ELEMENTO 
    def is_empty(self):
        if(self.head.value == None):
            return True
        else:
            return False
    
    #FUNCIÓN EXTRA QUE PERMITE IMPRIMIR TODOS LOS VALORES DE LA COLA SEGUIDOS DE UN SALTO DE LINEA
    def print_all(self):
        aux = self.head
        if(aux!=None):
            while(aux!= None):
                print(aux.value)
                aux = aux.next
        elif (aux == None):
            print("Empty Queue")

        else:
            print("Empty")
class NodoP:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Nodo():
    def __init__(self,data,siguiente = None):
        self.data =data
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = NodoP(dato)
            return
        nuevo_nodo = NodoP(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la pila para desapilar")
            return
        self.superior = self.superior.siguiente

    def imprimir(self):
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")
class ListNodes:
    def __init__(self,data):
        self.Nodo = Nodo(data)
        self.tam =1
        self.head =self.Nodo
        self.tail =self.Nodo.siguiente

    #AGREGA UN NODO Y AUMENTA EN 1 SU TAMAÑO
    def agregarNodo(self,data):
        node = Nodo(data)
        if(self.Nodo.siguiente == None):
            self.Nodo.siguiente = node
            self.tam +=1
            return
        else:
            nodo1 = self.Nodo
            acceso = True
            while(acceso):
                if(nodo1.siguiente == None):
                    nodo1.siguiente=node
                    self.tail = node
                    self.tam += 1
                    return
                else:
                    nodo1 = nodo1.siguiente
            
    def retornarUltimoNodo(self):
        return self.tail.data
            
    def retornarTamano(self):
        return self.tam
    def devolverData(self, posicion):
        nodo = self.head
        i = 0
        while(i<self.tam):
            if(i==posicion):
                return nodo.data
            else:
                nodo = nodo.siguiente
                i+=1
    def devolverNodo(self, posicion):
        nodo = self.head
        i = 0
        while(i<self.tam):
            if(i==posicion):
                return nodo
            else:
                nodo = nodo.siguiente
                i+=1
    def editarNodo(self, posicion, value):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                nodo.data=value
                return
            else:
                nodo = nodo.siguiente
                i+=1
    def eliminarNodo(self, cantidad):
        nodo = self.Nodo
        i = 0
        posicion = self.tam-cantidad-1
        while(i<self.tam):
            if(i==posicion):
                nodo.siguiente=None
                self.tail=nodo
                self.tam = self.tam-cantidad
                return
            else:
                nodo = nodo.siguiente
                i+=1
          
if __name__ == "__main__":
    s = ''
    ops=Queue()
    pila = Pila()
    pila.apilar(s)
    numeroInstrucciones = int(input())
    j=0
    while(j<numeroInstrucciones):
        palabra = input()
        ops.enqueue(palabra)
        j+=1
    j=0
    countSalto=0
    while(j<numeroInstrucciones):
        operacion = str(ops.dequeue()).split(' ')
        if(int(operacion[0])==1):
            s+=operacion[1]
            pila.apilar(s)
        elif(int(operacion[0])==2):
            if(len(s)==int(operacion[1])):
                s=''
                pila.apilar(s)
            else:
                number = len(s)-int(operacion[1])
                s=s[0:number]
                pila.apilar(s)
        elif(int(operacion[0])==3):
            if(countSalto==0):
                print(s[int(operacion[1])-1], end='')
                countSalto+=1
            else:
                print('\n'+s[int(operacion[1])-1], end='')
        elif(int(operacion[0])==4):
            if(pila.superior.dato==s):
                pila.desapilar()
            if(pila.superior.dato==''):
                s=''
            else:
                s = pila.superior.dato
        j+=1
   


            
    
    