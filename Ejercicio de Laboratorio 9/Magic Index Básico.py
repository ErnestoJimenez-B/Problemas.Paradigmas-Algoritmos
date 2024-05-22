def find_magic_index(arr):
   # busqueda binaria
    def binary_search(arr, start, end):
        # caso base
        if start > end:
            return -1
        # divide el arreglo
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        # busqueda de ambos lados
        elif arr[mid] > mid:
            return binary_search(arr, start, mid - 1)
        else:
            return binary_search(arr, mid + 1, end)

    return binary_search(arr, 0, len(arr) - 1)

# Ejemplo:
arr = [-1, 0, 1, 3, 6]
magic_index = find_magic_index(arr)
print(magic_index)
