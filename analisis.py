dataset =[10,25,37,42,58,63,71,89]

def calcular_promedio(datos):
    return sum(datos) / len(datos)
def calcular_maximo(datos):
    return max(datos)
def mostrar_resumen(datos):
    print(f"Total de registros: {len(datos)}")
    print(f"Promedio: {calcular_promedio(datos):.2f}")
    print(f"Máximo: {calcular_maximo(datos)}")

mostrar_resumen(dataset)