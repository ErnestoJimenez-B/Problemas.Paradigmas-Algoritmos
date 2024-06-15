import heapq
from collections import Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def cargar_arbol_desde_codificaciones(codificaciones):
    # Reconstruir el árbol de Huffman utilizando las codificaciones
    nodos = []
    for caracter, codigo in codificaciones.items():
        nodo_actual = None
        for bit in codigo:
            if bit == '0':
                if nodo_actual is None:
                    nodo_actual = NodoHuffman(None, 0)
                    nodos.append(nodo_actual)
                if nodo_actual.izquierda is None:
                    nodo_actual.izquierda = NodoHuffman(None, 0)
                    nodos.append(nodo_actual.izquierda)
                nodo_actual = nodo_actual.izquierda
            else:
                if nodo_actual is None:
                    nodo_actual = NodoHuffman(None, 0)
                    nodos.append(nodo_actual)
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = NodoHuffman(None, 0)
                    nodos.append(nodo_actual.derecha)
                nodo_actual = nodo_actual.derecha
        nodo_actual.caracter = caracter
    
    return nodos[0] if nodos else None

def decodificar_texto(texto_codificado, arbol_huffman):
    texto_decodificado = ''
    nodo_actual = arbol_huffman
    for bit in texto_codificado:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        
        if nodo_actual.caracter is not None:
            texto_decodificado += nodo_actual.caracter
            nodo_actual = arbol_huffman
    
    return texto_decodificado

def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

def main():
    # Read the coded message from 'texto_codificado.txt'
    with open("texto_codificado.txt", 'r') as archivo_codificado:
        texto_codificado = archivo_codificado.read()
    
    # Load or reconstruct Huffman tree from previously generated codifications
    # This example assumes you have a dictionary of codifications
    codificaciones = {'a': '00', 'b': '01', 'c': '10', 'd': '11'}  # Example codifications
    arbol_huffman = cargar_arbol_desde_codificaciones(codificaciones)
    
    # Decodificar el texto
    texto_decodificado = decodificar_texto(texto_codificado, arbol_huffman)
    
    # Guardar texto decodificado en un archivo separado
    guardar_archivo("texto_decodificado.txt", texto_decodificado)
    
    print("Texto decodificado guardado en 'texto_decodificado.txt'")

if __name__ == "__main__":
    main()
