from HashTable import HashTable


class SparseMatrix:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.hashTable = HashTable(100003)  # Usamos un número primo grande para reducir colisiones

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
        
        todos = []

        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                todos.append(actual)
                actual = actual.next

        self.hashTable = HashTable(100003)

        for nodo in todos:
            nuevaFila = nodo.columna
            nuevaColumna = nodo.fila

            self.set(nuevaFila, nuevaColumna, nodo.valor)

    def top_k(self, k):
            nodos = self.get_all_nodes()
            nodos_ordenados = self.mergeSort(nodos)
            return nodos_ordenados[:k]
        

    def get_all_nodes(self):
            nodos = []
            for bucket in self.hashTable.tabla:
                actual = bucket.head

                while actual is not None:
                    nodos.append(actual)
                    actual = actual.next
            return nodos

    def mergeSort(self, lista):
            if len(lista) <= 1:
                return lista

            medio = len(lista) // 2

            izquierda = lista[:medio]
            derecha = lista[medio:] 

            izquierda = self.mergeSort(izquierda)
            derecha = self.mergeSort(derecha)

            return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
            resultado = []
            i = j = 0

            while i < len(izquierda) and j < len(derecha):
                if izquierda[i].valor > derecha[j].valor:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1

            while i < len(izquierda):
                resultado.append(izquierda[i])
                i += 1

            while j < len(derecha):
                resultado.append(derecha[j])
                j += 1  

            return resultado
    
    def density(self):
        total_nodos = 0
        for bucket in self.hashTable.tabla:
            actual = bucket.head

            while actual is not None:
                total_nodos += 1
                actual = actual.next

        total_elementos = self.filas * self.columnas
        if total_elementos == 0:
            return 0
        return total_nodos / total_elementos