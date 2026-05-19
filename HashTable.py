from ListaEnlazada import ListaEnlazada


class HashTable:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = []
        for i in range(capacidad):
            self.tabla.append(ListaEnlazada())

    # MÉTODOS:
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
        bucket.delete(fila, columna)