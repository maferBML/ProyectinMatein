class NodoLista:
    def __init__(self, nodo):
        self.nodo = nodo
        self.next = None

class ListaNodos:
    
    def __init__(self):
        self.head = None

    def agregar(self, nodo):
        nuevo = NodoLista(nodo)
        nuevo.next = self.head
        self.head = nuevo

    def quitar(self, nodo):
        actual = self.head
        anterior = None
        while actual is not None:
            if actual.nodo is nodo:
                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next
                return
            anterior = actual
            actual = actual.next

    def todos(self):
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.nodo)
            actual = actual.next
        return resultado
    
    def agregar_ordenado(self, nodo, key='columna'):
        
        valor = nodo.columna if key == 'columna' else nodo.fila
        nuevo = NodoLista(nodo)

        if self.head is None or valor <= self.head.nodo.columna:
            nuevo.next = self.head
            self.head = nuevo
            return

        actual = self.head
        while actual.next is not None:
            sig_val = actual.next.nodo.columna if key == 'columna' else actual.next.nodo.fila
            if valor <= sig_val:
                break
            actual = actual.next
        nuevo.next = actual.next
        actual.next = nuevo

    def agregar_valor(self, valor):
        nuevo = NodoLista(valor)  
        nuevo.next = self.head
        self.head = nuevo

    def quitar_valor(self, valor):
        actual = self.head
        anterior = None

        while actual is not None:

            if actual.nodo == valor:

                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next

                return

            anterior = actual
            actual = actual.next
