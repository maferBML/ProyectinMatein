from HashTable import HashTable


class SpareseMatrix:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.hashTable = HashTable(100)

    # MÉTODOS:
    def get(self, fila, columna):
        
        nodo = self.hashTable.search(fila, columna)
        if nodo is not None:
            return nodo.valor
        else:
            return 0

    def set(self, fila, columna, valor):
        
        nodo = self.hashTable.search(fila, columna)
        if nodo is not None:
            nodo.valor = valor

        else:
            self.hashTable.insert(fila, columna, valor)

    def delete(self, fila, columna):
        self.hashTable.delete(fila, columna)

    def row_sum(self, fila):
        
        suma = 0
        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                if actual.fila == fila:
                    suma += actual.valor
                actual = actual.next
        return suma

    def col_sum(self, columna):
        
        suma = 0
        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                if actual.columna == columna:
                    suma += actual.valor
                actual = actual.next
        return suma

    def region_sum(self, f1, c1, f2, c2):
        
        suma = 0

        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                if f1 <= actual.fila <= f2 and c1 <= actual.columna <= c2:
                    suma += actual.valor
                actual = actual.next
        return suma

    def transpose(self):
        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                temp = actual.fila
                actual.fila = actual.columna
                actual.columna = temp
                actual = actual.next

    def top_k(self, k):
        todos = []

        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                todos.append(actual)
                actual = actual.next

        self.hashTable = HashTable(100)

        for nodo in todos
            nuevaFila = nodo.columna
            nuevaColumna = nodo.fila

            self.set(nuevaFila, nuevaColumna, nodo.valor)