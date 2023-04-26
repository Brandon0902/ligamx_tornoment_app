from models import Equipo, Jugador,Torneo,DirectorTecnico,TablaPosiciones,EquipoTorneo,Partido,Resultado

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
dir_tecnico_Atlas = DirectorTecnico("Benjamin Mora", "Mexicano", 40.0)
DirectorTecnico.agregar_director_tecnico(dir_tecnico_Atlas)

dir_tecnico_America = DirectorTecnico("Fernando ortiz", "Mexicano", 80.0)
DirectorTecnico.agregar_director_tecnico(dir_tecnico_America)

dir_tecnico_Chivas = DirectorTecnico("Veljko Paunović", "Español", 60.0)
DirectorTecnico.agregar_director_tecnico(dir_tecnico_Chivas)

#Instancias de EquipoTorneo
atlas = EquipoTorneo(10, 12, 3, 3, 1)
america = EquipoTorneo(8, 9, 2, 3, 2)
chivas = EquipoTorneo(6, 7, 1, 4, 1)

# Crea la Tabla
tabla = TablaPosiciones("Torneo Apertura", [atlas, america, chivas])

# Mostrar la tabla de posiciones
print("Tabla de Posiciones")
print("-------------------")
print("Equipo\tGoles\tPuntos\tPG\tPE\tPP")
for i, equipo in enumerate(tabla.equipo_torneo, start=1):
    print(f"{i}. {equipo}\t{equipo.goles}\t{equipo.puntos}\t{equipo.partidos_ganados}\t{equipo.partidos_empatados}\t{equipo.partidos_perdidos}")


#Crear partidos
partido1 = Partido.crear_partidos(atlas, america, "Estadio Jalisco", "2023-05-09")
partido2 = Partido.crear_partidos(chivas, atlas, "Estadio Akron", "2023-06-01")
partido3 = Partido.crear_partidos(america, chivas, "Estadio Azteca", "2023-07-13")


#Resultados de los partidos
resultado1 = Resultado((atlas, america, "Estadio Jalisco", "2023-05-09"), 2, 1)
resultado1.mostrar_equipos()
resultado1.mostrar_goles(resultado1.goles_e1, resultado1.goles_e2)

resultado2 = Resultado((chivas, atlas, "Estadio Akron", "2023-06-01"), 0, 1)
resultado2.mostrar_equipos()
resultado2.mostrar_goles(resultado2.goles_e1, resultado2.goles_e2)

resultado3 = Resultado((america, chivas, "Estadio Azteca", "2023-07-13"), 3, 2)
resultado3.mostrar_equipos()
resultado3.mostrar_goles(resultado3.goles_e1, resultado3.goles_e2)

