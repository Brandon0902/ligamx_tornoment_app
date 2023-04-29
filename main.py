from models import Equipo, Jugador,Torneo,DirectorTecnico,TablaPosiciones,EquipoTorneo,Partido,Resultado

# Crear los equipos
atlas = Equipo("logotipo1.png", [], "dir_tecnico1", "Atlas")
america = Equipo("logotipo2.png", [], "dir_tecnico2", "America")
chivas = Equipo("logotipo3.png", [], "dir_tecnico3", "Chivas")

# Agregar jugadores a los equipos
print("Jugadores")
print("-------------------")
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
print("-------------------")
# Crear el torneo
torneo = Torneo([atlas, america, chivas], [], [])

# Agregar un partido al torneo
torneo.agregar_partido(atlas, america, "Estadio Jalisco", "2023-05-09")
torneo.agregar_partido(chivas, atlas, "Estadio Akron", "2023-06-01")
torneo.agregar_partido(america, chivas, "Estadio Azteca", "2023-07-13")

#Crear directores tecnicos
dir_tecnico_atlas = DirectorTecnico("Benjamin Mora", "Mexicano", 40.0)


dir_tecnico_america = DirectorTecnico("Fernando ortiz", "Mexicano", 80.0)


dir_tecnico_chivas = DirectorTecnico("Veljko Paunović", "Español", 60.0)


#Instancias de EquipoTorneo
atlas_torneo = EquipoTorneo(atlas,10, 12, 3, 3, 1)
america_torneo= EquipoTorneo(america,8, 9, 2, 3, 2)
chivas_torneo = EquipoTorneo(chivas, 7, 1, 4, 1,2)

# Crea la Tabla
tabla = TablaPosiciones("Torneo Apertura", [atlas_torneo, america_torneo, chivas_torneo])

# Mostrar la tabla de posiciones
print("Tabla de Posiciones")
print("-------------------")
print("Equipo\tGoles\tPuntos\tPG\tPE\tPP")
for i, equipo_toreno in enumerate(tabla.equipos_torneo, start=1):
    print(f"{i}.{equipo_toreno.equipo.nombre}\t{equipo_toreno.goles}\t{equipo_toreno.puntos}\t{equipo_toreno.partidos_ganados}\t{equipo_toreno.partidos_empatados}\t{equipo_toreno.partidos_perdidos}")
print("-------------------")

#Crear partidos
print("Partidos")
print("-------------------")
partido1 = Partido("Atlas","America", "Estadio Jalisco", "2023-05-09")
partido2 = Partido("Atlas", "Chivas", "Estadio Akron", "2023-06-01")
partido3 = Partido("America", "Chivas", "Estadio Azteca", "2023-07-13")

print(partido1.mostrar_partido())
print(partido2.mostrar_partido())
print(partido3.mostrar_partido())
print("-------------------")
#Resultados de los partidos
print("Resultados de los partidos")
print("-------------------")
resultado1 = Resultado(("Atlas", "America", "Estadio Jalisco", "2023-05-09"), 2, 1)
resultado2 = Resultado(("Chivas", "Atlas", "Estadio Akron", "2023-06-01"), 0, 1)
resultado3 = Resultado(("America", "Chivas", "Estadio Azteca", "2023-07-13"), 3, 2)

print(resultado1.obtener_resultado_completo())
print(resultado2.obtener_resultado_completo())
print(resultado3.obtener_resultado_completo())