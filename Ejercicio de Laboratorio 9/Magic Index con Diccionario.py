def find_magic_index(arr):
    # funcion
    def binary_search(arr, start, end, memo):
       # casos base
        if start > end:
            return -1
        if start in memo:
            return memo[start]
        # división y búsqueda
        mid = (start + end) // 2
        if arr[mid] == mid:
            memo[start] = mid
            return mid
        elif arr[mid] > mid:
            result = binary_search(arr, start, mid - 1, memo)
            memo[start] = result
            return result
        else:
            result = binary_search(arr, mid + 1, end, memo)
            memo[start] = result
            return result
    # diccionario de datos
    memo = {}
    return binary_search(arr, 0, len(arr) - 1, memo)

# Ejemplo:
arr = [-1, 0, 2, 4, 6]
magic_index = find_magic_index(arr)
print(magic_index)
