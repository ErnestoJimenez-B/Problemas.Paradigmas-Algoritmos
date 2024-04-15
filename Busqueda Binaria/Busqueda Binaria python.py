# PYTHON
# Programa que regresa la raíz cuadrada de x
def floorSqrt(x):

	# Casos
	if (x == 0 or x == 1):
		return x

	# Búsqueda Binaria
	start = 1
	end = x//2
	while (start <= end):
		mid = (start + end) // 2

		# Si x es cuadrado perfecto
		if (mid*mid == x):
			return mid

		# Cuando mid*mid es menor que x
		if (mid * mid < x):
			start = mid + 1
			ans = mid

		else:

			# mid*mid es mayor que x
			end = mid-1

	return ans

x = 11
print(floorSqrt(x))
