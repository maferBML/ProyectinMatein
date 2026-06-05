# SparseMatrix.py
from HashTable import HashTable, HashTableSimple


class SparseMatrix:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.hashTable = HashTable(100003)

        self.indiceFila = HashTableSimple(100003)
        self.indiceColumna = HashTableSimple(100003)

        self.totalNodos = 0

        #AUXILIARES

    def _agregar_a_indice(self, nodo):
        
        lista = self.indiceFila.get(nodo.fila)
        if lista is None:
            lista = []
            self.indiceFila.set(nodo.fila, lista)
        lista.append(nodo)

    
        lista2 = self.indiceColumna.get(nodo.columna)
        if lista2 is None:
            lista2 = []
            self.indiceColumna.set(nodo.columna, lista2)
        lista2.append(nodo)

    def _quitar_de_indice(self, nodo):

        lista = self.indiceFila.get(nodo.fila)
        if lista is not None:
            i = 0
            nueva = []
            while i < len(lista):
                if lista[i] is not nodo:
                    nueva.append(lista[i])
                i += 1
            self.indiceFila.set(nodo.fila, nueva)

        lista2 = self.indiceColumna.get(nodo.columna)
        if lista2 is not None:
            i = 0
            nueva2 = []
            while i < len(lista2):
                if lista2[i] is not nodo:
                    nueva2.append(lista2[i])
                i += 1
            self.indiceColumna.set(nodo.columna, nueva2)

    #METODOS

    def get(self, fila, columna):
        nodo = self.hashTable.search(fila, columna)
        if nodo is not None:
            return nodo.valor
        return 0

    def set(self, fila, columna, valor):
        nodo = self.hashTable.search(fila, columna)
        if nodo is not None:
            # Ya existe, solo actualiza valor
            nodo.valor = valor
        else:
            # Nuevo nodo
            self.hashTable.insert(fila, columna, valor)
            nodo = self.hashTable.search(fila, columna)
            self._agregar_a_indice(nodo)
            self.totalNodos += 1

    def delete(self, fila, columna):
        nodo = self.hashTable.search(fila, columna)
        if nodo is not None:
            self._quitar_de_indice(nodo)
            self.hashTable.delete(fila, columna)
            self.totalNodos -= 1

    def row_sum(self, fila):
        
        lista = self.indiceFila.get(fila)
        if lista is None:
            return 0
        suma = 0
        for nodo in lista:
            suma += nodo.valor
        return suma

    def col_sum(self, columna):
        
        lista = self.indiceColumna.get(columna)
        if lista is None:
            return 0
        suma = 0
        for nodo in lista:
            suma += nodo.valor
        return suma

    def region_sum(self, f1, c1, f2, c2):
        
        suma = 0
        todos = self.get_all_nodes()
        for nodo in todos:
            if f1 <= nodo.fila <= f2 and c1 <= nodo.columna <= c2:
                suma += nodo.valor
        return suma


    def transpose(self):
        
        datos = []
        for bucket in self.hashTable.tabla:
            actual = bucket.head
            while actual is not None:
                datos.append((actual.fila, actual.columna, actual.valor))
                actual = actual.next

        # Resetear todo
        self.hashTable = HashTable(100003)
        self.indiceFila = HashTableSimple(100003)
        self.indiceColumna = HashTableSimple(100003)
        self.totalNodos = 0

        for fila, columna, valor in datos:
            self.set(columna, fila, valor)

    def top_k(self, k):
        nodos = self.get_all_nodes()
        nodos_ordenados = self.mergeSort(nodos)
        if k <= 0:
            return []

        if k > len(nodos):
            k = len(nodos)

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
        izquierda = self.mergeSort(lista[:medio])
        derecha = self.mergeSort(lista[medio:])
        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        resultado = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].valor >= derecha[j].valor:
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
        total_elementos = self.filas * self.columnas
        if total_elementos == 0:
            return 0
        return self.totalNodos / total_elementos