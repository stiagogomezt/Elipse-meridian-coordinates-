import math

def calcular_coordenadas_parametricas(a, f, latitud_geodesica, latitud_geocentrica):
    # Convertir las latitudes a radianes
    latitud_geodesica_rad = math.radians(latitud_geodesica)
    latitud_geocentrica_rad = math.radians(latitud_geocentrica)
    
    # Calcular excentricidad
    excentricidad_cuadrada = (2 * f) - (f ** 2)
    
    # Calcular latitud paramétrica
    latitud_parametrica = math.atan((1 - excentricidad_cuadrada) * math.tan(latitud_geodesica_rad)/(1-f))
    
    # Calcular latitud geocéntrica
    latitud_geocentrica_calc = math.atan(math.tan(latitud_geocentrica_rad) / (1 - f))
    
    return latitud_parametrica, latitud_geocentrica_calc

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
latitud_geodesica = float(input("Ingrese la latitud geodésica en grados: "))
latitud_geocentrica = float(input("Ingrese la latitud geocéntrica en grados: "))

# Calcular las coordenadas paramétricas
parametrica, geocentrica_calc = calcular_coordenadas_parametricas(a, f, latitud_geodesica, latitud_geocentrica)

# Mostrar resultados
print("Coordenadas paramétricas calculadas:")
print("Latitud paramétrica en funcion de geodesica:", math.degrees(parametrica))
print("Latitud parametrica en funcion de geocentrica:", math.degrees(geocentrica_calc))
