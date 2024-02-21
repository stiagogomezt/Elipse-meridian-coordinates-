import math

def calcular_coordenadas_geocentricas(a, f, latitud_parametrica, latitud_geodesica):
    # Convertir las latitudes a radianes
    latitud_parametrica_rad = math.radians(latitud_parametrica)
    latitud_geodesica_rad = math.radians(latitud_geodesica)
    
    # Calcular excentricidad
    excentricidad_cuadrada = (2 * f) - (f ** 2)
    
    # Calcular latitud geodesica en funcion de lat parametrica
    latitud_geocentricatetha = math.atan( (math.tan(latitud_parametrica_rad)*(1-f)))
    
    # Calcular latitud geodesica en funcion de lat geocentrica
    latitud_geocentricaphi= math.atan(math.tan(latitud_geodesica_rad) * (1 - excentricidad_cuadrada))
    
    return latitud_geocentricatetha, latitud_geocentricaphi

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
latitud_parametrica = float(input("Ingrese la latitud parametrica en grados: "))
latitud_geodesica = float(input("Ingrese la latitud geodesica en grados: "))

# Calcular las coordenadas paramétricas
latitud_geocentricatetha, latitud_geocentricaphi = calcular_coordenadas_geocentricas(a, f, latitud_parametrica, latitud_geodesica)

# Mostrar resultados
print("Coordenadas paramétricas calculadas:")
print("Latitud geocentrica en funcion de parametrica:", math.degrees(latitud_geocentricatetha))
print("Latitud geocentrica en funcion de geodesica:", math.degrees(latitud_geocentricaphi))
