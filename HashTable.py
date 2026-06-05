from ListaEnlazada import ListaEnlazada


class HashTable:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = []
        for i in range(capacidad):
            self.tabla.append(ListaEnlazada())

    # METODOS:
    def hash_function(self, fila, columna):
        return (fila * 31 + columna) % self.capacidad

    def insert(self, fila, columna, valor):
        index = self.hash_function(fila, columna)
        bucket = self.tabla[index]
        bucket.insert(fila, columna, valor)

    def search(self, fila, columna):
        index = self.hash_function(fila, columna)
        bucket = self.tabla[index]
        return bucket.search(fila, columna)

    def delete(self, fila, columna):  
        index = self.hash_function(fila, columna)
        bucket = self.tabla[index]
        return bucket.delete(fila, columna)


class NodoSimple:

    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.next = None

class ListaEnlazadaSimple:

    def __init__(self):
        self.head = None
        
    def get(self, clave):
        actual = self.head
        while actual is not None:
            if actual.clave == clave:
                return actual.valor
            actual = actual.next
        return None
    
    def set(self, clave, valor):
        actual = self.head
        while actual is not None:
            if actual.clave == clave:
                actual.valor = valor
                return
            actual = actual.next
        nuevo = NodoSimple(clave, valor)
        nuevo.next = self.head
        self.head = nuevo
        

    def delete(self, clave):
        actual = self.head
        anterior = None
        while actual is not None:
            if actual.clave == clave:
                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next
                return True
            anterior = actual
            actual = actual.next
        
class HashTableSimple:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = []
        for i in range(capacidad):
            self.tabla.append(ListaEnlazadaSimple())

    def hash_function(self, clave):
        return (clave * 31) % self.capacidad

    def set(self, clave, valor):
        index = self.hash_function(clave)
        self.tabla[index].set(clave, valor)

    def get(self, clave):
        index = self.hash_function(clave)
        return self.tabla[index].get(clave)

    def delete(self, clave):
        index = self.hash_function(clave)
        return self.tabla[index].delete(clave)