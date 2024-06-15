import heapq
from collections import defaultdict, Counter

# Definición de la clase Node para representar un nodo en el árbol de Huffman
class Node:
    def __init__(self, char, freq):
        self.char = char  # Carácter almacenado en el nodo (o None para nodos internos)
        self.freq = freq  # Frecuencia del carácter
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho

    # Definimos el comparador less_than para que los nodos puedan ser comparados por frecuencia
    def __lt__(self, other):
        return self.freq < other.freq

# Función para construir el árbol de Huffman a partir de las frecuencias de los caracteres
def build_huffman_tree(frequencies):
    # Creamos una lista de nodos a partir de las frecuencias
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    # Convertimos la lista en una cola de prioridad (heap)
    heapq.heapify(heap)
    
    # Combinamos los nodos hasta que solo quede uno
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Nodo con la menor frecuencia
        right = heapq.heappop(heap)  # Segundo nodo con la menor frecuencia
        
        # Creamos un nuevo nodo combinando los dos anteriores
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        # Insertamos el nuevo nodo en la cola de prioridad
        heapq.heappush(heap, merged)
    
    # El último nodo en el heap es la raíz del árbol de Huffman
    return heap[0]

# Función para construir el código de Huffman a partir del árbol
def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    
    # Si el nodo es una hoja, asignamos el código actual al carácter
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        # Recorremos los hijos izquierdo y derecho, agregando '0' o '1' al prefijo
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    
    return codebook

# Función para codificar el texto utilizando el código de Huffman generado
def encode(text, codebook):
    return ''.join(codebook[char] for char in text)

# Función para decodificar el texto codificado utilizando el árbol de Huffman
def decode(encoded_text, huffman_tree):
    decoded_text = []
    node = huffman_tree
    
    for bit in encoded_text:
        # Nos movemos hacia la izquierda o derecha en el árbol según el bit
        node = node.left if bit == '0' else node.right
        
        # Si llegamos a un nodo hoja, agregamos el carácter decodificado al texto
        if node.char is not None:
            decoded_text.append(node.char)
            node = huffman_tree  # Volvemos a la raíz del árbol
    
    return ''.join(decoded_text)

def main():
    # Paso 1: Obtener el texto de entrada del usuario
    text = input("Please enter the text to encode: ")
    
    # Paso 2: Calcular las frecuencias de los caracteres
    frequencies = Counter(text)
    
    # Paso 3: Construir el árbol de Huffman
    huffman_tree = build_huffman_tree(frequencies)
    
    # Paso 4: Construir los códigos de Huffman
    huffman_codes = build_codes(huffman_tree)
    
    # Paso 5: Codificar el texto utilizando los códigos de Huffman
    encoded_text = encode(text, huffman_codes)
    
    # Paso 6: Decodificar el texto codificado
    decoded_text = decode(encoded_text, huffman_tree)
    
    # Imprimir los resultados
    print(f"Encoded Text: {encoded_text}")
    print(f"Decoded Text: {decoded_text}")

# Ejecución del programa principal
if __name__ == "__main__":
    main()
