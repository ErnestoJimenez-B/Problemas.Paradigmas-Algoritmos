def asignar_memoria(procesos, bloques):
    # Ordenar procesos y bloques de memoria de mayor a menor
    procesos.sort(reverse=True)
    bloques.sort(reverse=True)

    asignaciones = {}
    memoria_libre_total = 0

    # Iterar sobre cada proceso
    for proceso in procesos:
        asignado = False

        # Iterar sobre cada bloque de memoria
        for i, bloque in enumerate(bloques):
            if proceso <= bloque:
                # Asignar proceso al bloque de memoria
                asignaciones[proceso] = bloque
                bloques[i] -= proceso
                asignado = True
                break

        if not asignado:
            print("No hay suficiente memoria para asignar el proceso de", proceso, "KB.")

    # Calcular memoria libre total
    for bloque in bloques:
        memoria_libre_total += bloque

    return asignaciones, memoria_libre_total

# Ejemplo de uso
procesos = [426, 417, 212, 112]
bloques = [600, 500, 300, 200, 100]

asignaciones, memoria_libre = asignar_memoria(procesos, bloques)

print("Asignaciones de procesos a bloques de memoria:")
for proceso, bloque in asignaciones.items():
    print("Proceso", proceso, "KB -> Bloque", bloque, "KB")

print("Memoria libre total:", memoria_libre, "KB")
