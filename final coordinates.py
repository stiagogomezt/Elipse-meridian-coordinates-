import math

def calcular_gran_normal(eccentricity, semi_major_axis, latitude):
    # Convertir la latitud de grados a radianes
    lat_rad = math.radians(latitude)
    
    # Calcular la gran normal
    N = semi_major_axis / math.sqrt(1 - (eccentricity ) * (math.sin(lat_rad) ** 2))

    return N

def calcular_coordenadas_geodesicas(eccentricity, semi_major_axis, latitude):
    # Calcular el valor de la gran normal
    N = calcular_gran_normal(eccentricity, semi_major_axis, latitude)
    
    # Convertir la latitud de grados a radianes
    lat_rad = math.radians(latitude)
    
    # Calcular las coordenadas X y Z en el sistema geodésico
    x = N * math.cos(lat_rad)
    z = N * (1 - eccentricity ) * math.sin(lat_rad)

    return x, z

def calcular_coordenadas_geocentricas(x, z, atan_angle):
    # Calcular Rg
    Rg = math.sqrt(x ** 2 + z ** 2)

    # Calcular la latitud en radianes
    w = math.atan2(z, x)

    # Calcular Xg y Zg
    xg = Rg * math.cos(w)
    zg = Rg * math.sin(w)

    return xg, zg

def calcular_parametro_theta(x, z, semi_major_axis, eccentricity):
    # Calcular b
    b = semi_major_axis * math.sqrt(1 - eccentricity )

    # Calcular el parámetro theta
    theta = math.atan(z / x * (semi_major_axis / b))

    return math.degrees(theta)

def calcular_arcotangente(z, x):
    # Calcular la arcotangente de z/x
    atan_angle = math.atan2(z, x)

    return math.degrees(atan_angle)

def calcular_coordenadas_parametricas(theta, semi_major_axis, semi_minor_axis):
    # Calcular Xp y Zp
    xp = semi_major_axis * math.cos(math.radians(theta))
    zp = semi_minor_axis * math.sin(math.radians(theta))

    return xp, zp

def main():
    eccentricity = float(input("Ingrese la excentricidad del elipsoide: "))
    semi_major_axis = float(input("Ingrese el semieje mayor del elipsoide (en metros): "))
    semi_minor_axis = semi_major_axis * math.sqrt(1 - eccentricity )
    latitud = float(input("Ingrese la latitud (en grados decimales): "))

    x, z = calcular_coordenadas_geodesicas(eccentricity, semi_major_axis, latitud)

    N = calcular_gran_normal(eccentricity, semi_major_axis, latitud)
    print(f"Gran Normal en la latitud {latitud}°: {N}")

    print(f"Coordenadas geodésicas en la latitud {latitud}°: (X={x}, Z={z})")

    angulo_arcotangente = calcular_arcotangente(z, x)
    print(f"Arcotangente de Z/X: {angulo_arcotangente}°")

    xg, zg = calcular_coordenadas_geocentricas(x, z, angulo_arcotangente)
    print(f"Coordenadas geocéntricas: (Xg={xg}, Zg={zg})")

    theta = calcular_parametro_theta(x, z, semi_major_axis, eccentricity)
    print(f"Parámetro theta: {theta}°")

    xp, zp = calcular_coordenadas_parametricas(theta, semi_major_axis, semi_minor_axis)
    print(f"Coordenadas paramétricas: (Xp={xp}, Zp={zp})")

if __name__ == "__main__":
    main()
