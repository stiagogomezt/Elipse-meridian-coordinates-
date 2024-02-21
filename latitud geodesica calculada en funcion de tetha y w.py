import math

def calcular_coordenadas_geodesicas(a, f, latitud_parametrica, latitud_geocentrica):
    # Convertir las latitudes a radianes
    latitud_parametrica_rad = math.radians(latitud_parametrica)
    latitud_geocentrica_rad = math.radians(latitud_geocentrica)
    
    # Calcular excentricidad
    excentricidad_cuadrada = (2 * f) - (f ** 2)
    
    # Calcular latitud geodesica en funcion de lat parametrica
    latitud_geodesicatetha = math.atan( (1-f)* math.tan(latitud_parametrica_rad)/(1 - excentricidad_cuadrada))
    
    # Calcular latitud geodesica en funcion de lat geocentrica
    latitud_geodesicaw = math.atan(math.tan(latitud_geocentrica_rad) / (1 - excentricidad_cuadrada))
    
    return latitud_geodesicatetha, latitud_geodesicaw

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
latitud_parametrica = float(input("Ingrese la latitud parametrica en grados: "))
latitud_geocentrica = float(input("Ingrese la latitud geocéntrica en grados: "))

# Calcular las coordenadas paramétricas
latitud_geodesicatetha, latitud_geodesicaw = calcular_coordenadas_geodesicas(a, f, latitud_parametrica, latitud_geocentrica)

# Mostrar resultados
print("Coordenadas paramétricas calculadas:")
print("Latitud geodesica en funcion de parametrica:", math.degrees(latitud_geodesicatetha))
print("Latitud geodesica en funcion de geocentrica:", math.degrees(latitud_geodesicaw))
