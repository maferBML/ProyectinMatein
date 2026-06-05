from SparseMatrix import SparseMatrix


class LeectorDeArchivos:

    def __init__(self):

        entrada = open("entrada.txt", "r")
        salida = open("salida.txt", "w")

        lineas = entrada.readlines()

        if len(lineas) == 0:
            print("El archivo está vacío")
            entrada.close()
            salida.close()
            return

        datos = lineas[0].split()
        if len(datos) < 3:
            print("Formato inválido")
            entrada.close()
            salida.close()
            return
        filas = int(datos[0])
        columnas = int(datos[1])
        n = int(datos[2])

        self.matriz = SparseMatrix(filas, columnas)

        for i in range(1, n + 1):
            fila, columna, valor = map(int, lineas[i].split())
            self.matriz.set(fila, columna, valor)

        q = int(lineas[n + 1])

        inicio = n + 2

        for i in range(inicio, inicio + q):

            if i >= len(lineas):
                print("Faltan operaciones en el archivo")
                break

            partes = lineas[i].split()
            if len(partes) == 0:
                continue
            operacion = partes[0]

            if operacion == "GET":
                fila = int(partes[1])
                columna = int(partes[2])
                resultado = self.matriz.get(fila, columna)
                salida.write(f"GET {fila} {columna} = {resultado}\n")

            elif operacion == "SET":
                fila = int(partes[1])
                columna = int(partes[2])
                valor = int(partes[3])  
                self.matriz.set(fila, columna, valor)
                salida.write(f"SET {fila} {columna} = OK\n")

            elif operacion == "DELETE":
                fila = int(partes[1])
                columna = int(partes[2])
                self.matriz.delete(fila, columna)
                salida.write(f"DELETE {fila} {columna} = OK\n")

            elif operacion == "ROW_SUM":
                fila = int(partes[1])
                resultado = self.matriz.row_sum(fila)
                salida.write(f"ROW_SUM {fila} = {resultado}\n")

            elif operacion == "COL_SUM":
                columna = int(partes[1])
                resultado = self.matriz.col_sum(columna)
                salida.write(f"COL_SUM {columna} = {resultado}\n")

            elif operacion == "REGION_SUM":
                f1 = int(partes[1])
                c1 = int(partes[2])
                f2 = int(partes[3])
                c2 = int(partes[4])
                resultado = self.matriz.region_sum(f1, c1, f2, c2)
                salida.write(f"REGION_SUM {f1} {c1} {f2} {c2} = {resultado}\n")

            elif operacion == "TRANSPOSE":
                self.matriz.transpose()
                salida.write("TRANSPOSE = OK\n")

            elif operacion == "TOP_K":
                k = int(partes[1])
                nodos = self.matriz.top_k(k)

                partes_resultados = ""
                for nodo in nodos:
                    partes_resultados += f"({nodo.fila},{nodo.columna},{nodo.valor}) "

                salida.write(f"TOP_K {k} = {partes_resultados.strip()}\n")

            elif operacion == "DENSITY":
                resultado = self.matriz.density()

                salida.write(f"DENSITY = {resultado}\n")

        entrada.close()
        salida.close()