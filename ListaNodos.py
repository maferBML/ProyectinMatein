from Nodo import Nodo


class ListaEnlazada:

    def __init__(self):
        self.head = None
        self.size = 0

# MÉTODOS:
    def insert(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)
        nuevo.next = self.head
        self.head = nuevo
        self.size += 1
        return nuevo

    def search(self, fila, columna):
        actual = self.head
        while actual is not None:
            if actual.fila == fila and actual.columna == columna:
                return actual
            actual = actual.next
        return None

    def delete(self, fila, columna):
        actual = self.head
        anterior = None
        while actual is not None:
            if actual.fila == fila and actual.columna == columna:
                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next
                self.size -= 1
                return True
            anterior = actual
            actual = actual.next
        return False

    def get_all_nodes(self):
        actual = self.head
        nodos = []

        while actual is not None:
            nodos.append(actual)
            actual = actual.next

        return nodos

