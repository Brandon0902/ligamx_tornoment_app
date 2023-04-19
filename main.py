from models import Equipo, Jugador,Torneo,DirectorTecnico,TablaPosiciones,Partido

# Crear los equipos
atlas = Equipo("logotipo1.png", [], "dir_tecnico1", "nombre_atlas")
america = Equipo("logotipo2.png", [], "dir_tecnico2", "nombre_america")
chivas = Equipo("logotipo3.png", [], "dir_tecnico3", "nombre_chivas")

# Agregar jugadores a los equipos
atlas.agregar_jugador(Jugador("Julian Quiñones", 33, "Colombiano", "Delantero", "Titular"))
atlas.agregar_jugador(Jugador("Julio Furch", 9, "Argentino", "Delantero", "Titular"))
atlas.agregar_jugador(Jugador("Oziel Herrera", 7, "Mexicano/Cubano", "Extremo", "Titular"))

america.agregar_jugador(Jugador("Jonathan Rodriguez", 10, "Uruguayo", "Extremo", "Titular"))
america.agregar_jugador(Jugador("Henry Martin", 21, "Mexicano", "Delantero", "Titular"))
america.agregar_jugador(Jugador("Alejandro Zendejas", 17, "Estadounidense", "Extremo", "Titular"))

chivas.agregar_jugador(Jugador("Pavel Perez", 6, "Mexicano", "Delantero", "Suplente"))
chivas.agregar_jugador(Jugador("Alexis Vega", 10, "Mexicano", "Extremo", "Titular"))
chivas.agregar_jugador(Jugador("Roberto Alvarado", 26, "Mexicano", "Extremo", "Titular"))

for equipo in [atlas, america, chivas]:
    print(f"Equipo: {equipo.nombre}")
    for jugador in equipo.jugadores:
        print(f"Jugador: {jugador.nombre}, número: {jugador.numero}, nacionalidad: {jugador.nacionalidad}, posición: {jugador.posicion}, rol: {jugador.rol}") 

# Crear el torneo
torneo = Torneo([atlas, america, chivas], [], [])

# Agregar un partido al torneo
torneo.agregar_partido(atlas, america, "Estadio Jalisco", "2023-05-09")
torneo.agregar_partido(chivas, atlas, "Estadio Akron", "2023-06-01")
torneo.agregar_partido(america, chivas, "Estadio Azteca", "2023-07-13")

#Crear directores tecnicos
Dir_tecnico_Atlas = DirectorTecnico.crear_director_tecnico("Benjamin Mora", "Mexicano", 40.0)
Dir_tecnico_America = DirectorTecnico.crear_director_tecnico("Fernando ortiz", "Mexicano", 80.0)
Dir_tecnico_Chivas = DirectorTecnico.crear_director_tecnico("Veljko Paunović", "Español", 60.0)

#Asignar Rol
Quiñones = Jugador("Julian Quiñones", 33, "Colombiano", "Delantero", "Titular")
Quiñones.asignar_rol("Titular")
