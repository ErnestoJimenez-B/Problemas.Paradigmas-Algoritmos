import heapq
from collections import Counter, defaultdict

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def generar_arbol_huffman(frecuencias):
    cola = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola)
    
    while len(cola) > 1:
        nodo_izquierdo = heapq.heappop(cola)
        nodo_derecho = heapq.heappop(cola)
        
        nodo_combinado = NodoHuffman(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
        nodo_combinado.izquierda = nodo_izquierdo
        nodo_combinado.derecha = nodo_derecho
        
        heapq.heappush(cola, nodo_combinado)
    
    return cola[0]

def generar_codificacion_huffman(arbol_huffman, prefijo='', codificaciones=None):
    if codificaciones is None:
        codificaciones = {}
    
    if arbol_huffman.caracter is not None:
        codificaciones[arbol_huffman.caracter] = prefijo
    else:
        generar_codificacion_huffman(arbol_huffman.izquierda, prefijo + '0', codificaciones)
        generar_codificacion_huffman(arbol_huffman.derecha, prefijo + '1', codificaciones)
    
    return codificaciones

def codificar_texto(texto, codificaciones):
    texto_codificado = ''
    for caracter in texto:
        texto_codificado += codificaciones[caracter]
    return texto_codificado

def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

def main():
    texto = input("Ingresa el texto a codificar: ")
    
    # Contar frecuencias de los caracteres
    frecuencias = Counter(texto)
    
    # Generar árbol de Huffman
    arbol_huffman = generar_arbol_huffman(frecuencias)
    
    # Generar codificaciones de Huffman
    codificaciones = generar_codificacion_huffman(arbol_huffman)
    
    # Codificar el texto
    texto_codificado = codificar_texto(texto, codificaciones)
    
    # Guardar texto original y codificado en archivos separados
    guardar_archivo("texto_original.txt", texto)
    guardar_archivo("texto_codificado.txt", texto_codificado)
    
    print("Texto original guardado en 'texto_original.txt'")
    print("Texto codificado guardado en 'texto_codificado.txt'")

if __name__ == "__main__":
    main()
