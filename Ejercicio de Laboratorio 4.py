def min_monedas(V):
    monedas = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    num_monedas = [0] * len(monedas)
    i = 0
    while V:
        num_monedas[i] = V // monedas[i]
        V %= monedas[i]
        i += 1
    return num_monedas

# Función para imprimir el desglose de monedas
def imprimir_desglose(V, num_monedas):
    monedas = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    print("Desglose para V =", V)
    for i, cantidad in enumerate(num_monedas):
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {monedas[i]}")

# Ejemplos
V_values = [2550, 8432, 263]
for V in V_values:
    monedas_utilizadas = min_monedas(V)
    imprimir_desglose(V, monedas_utilizadas)
    print()
