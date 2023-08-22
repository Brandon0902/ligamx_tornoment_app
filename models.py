class Equipo:
    def __init__(self, logotipo, jugadores, dt, nombre):
        self.logotipo = logotipo
        self.jugadores = jugadores
        self.dt = dt
        self.nombre = nombre
       
class Jugador:
   def __init__(self,nombre, numero, nacionalidad,posicion,rol):
        self.nombre = nombre
        self.numero = numero
        self.nacionalidad = nacionalidad
        self.posicion = posicion
        self.rol = rol

   def agregar_jugador(self,jugador):
    self.jugadores.append(jugador)


class DirectorTecnico:
    def __init__(self, nombre, nacionalidad, porcentaje):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.porcentaje = porcentaje
    
    def agregar_director_tecnico(self, director_tecnico):
        self.director_tecnico = director_tecnico

class Torneo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.partidos = []
        self.tabla_posiciones = TablaPosiciones(self)  
        self.resultados = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
        print(f"Equipo '{equipo.nombre}' agregado al torneo '{self.nombre}'")

    def obtener_equipo_torneo(self, equipo):
        for equipo_torneo in self.tabla_posiciones.equipos_torneo:
            if equipo_torneo.equipo == equipo:
                return equipo_torneo
        # Si no se encuentra el equipo, crear un nuevo objeto EquipoTorneo y agregarlo a la lista
        equipo_torneo = EquipoTorneo(equipo)
        self.tabla_posiciones.equipos_torneo.append(equipo_torneo)
        return equipo_torneo

    def registrar_resultado(self, resultado):
        partido = resultado.partido
        equipo1 = partido.equipo1
        equipo2 = partido.equipo2
        goles_e1 = resultado.goles_e1
        goles_e2 = resultado.goles_e2

        partido.mostrar_partido()
        print(f"Resultado: {equipo1.nombre} {goles_e1} - {goles_e2} {equipo2.nombre}")

        equipo_torneo1 = self.obtener_equipo_torneo(equipo1)  
        equipo_torneo2 = self.obtener_equipo_torneo(equipo2)  

        if goles_e1 > goles_e2:
            equipo_torneo1.agregar_puntos(3)
            equipo_torneo1.agregar_partido_ganado()
            equipo_torneo2.agregar_partido_perdido()
            equipo_torneo1.agregar_goles(goles_e1)
            equipo_torneo2.agregar_goles(goles_e2)
        elif goles_e1 < goles_e2:
            equipo_torneo2.agregar_puntos(3)
            equipo_torneo2.agregar_partido_ganado()
            equipo_torneo1.agregar_partido_perdido()
            equipo_torneo1.agregar_goles(goles_e1)
            equipo_torneo2.agregar_goles(goles_e2)
        else:
            equipo_torneo1.agregar_puntos(1)
            equipo_torneo2.agregar_puntos(1)
            equipo_torneo1.agregar_partido_empatado()
            equipo_torneo2.agregar_partido_empatado()
            equipo_torneo1.agregar_goles(goles_e1)
            equipo_torneo2.agregar_goles(goles_e2)

        self.resultados.append(resultado)


class TablaPosiciones:
    def __init__(self, torneo):
        self.torneo = torneo
        self.equipos_torneo = []

    def obtener_equipo_torneo(self, equipo):
        for equipo_torneo in self.equipos_torneo:
            if equipo_torneo.equipo == equipo:
                return equipo_torneo
        equipo_torneo = EquipoTorneo(equipo)
        self.equipos_torneo.append(equipo_torneo)
        return equipo_torneo

    def agregar_equipo(self, equipo):
        equipo_torneo = EquipoTorneo(equipo)
        self.equipos_torneo.append(equipo_torneo)

    
    def mostrar_tabla_posiciones(self):
        # Ordenar los equipos por puntos de mayor a menor
        self.equipos_torneo.sort(key=lambda x: x.puntos, reverse=True)

        print("Tabla de Posiciones:")
        print("Equipo\t\tPuntos\tPartidos Ganados\tPartidos Empatados\tPartidos Perdidos\tGoles")

        for equipo_torneo in self.equipos_torneo:
            print(f"{equipo_torneo.equipo.nombre}\t{equipo_torneo.puntos}\t{equipo_torneo.partidos_ganados}\t{equipo_torneo.partidos_empatados}\t{equipo_torneo.partidos_perdidos}\t{equipo_torneo.goles}")


class EquipoTorneo:
    def __init__(self, equipo):
        self.equipo = equipo
        self.nombre = equipo.nombre 
        self.puntos = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles = 0


    def agregar_puntos(self, puntos):
        self.puntos += puntos

    def agregar_partido_ganado(self):
        self.partidos_ganados += 1

    def agregar_partido_empatado(self):
        self.partidos_empatados += 1

    def agregar_partido_perdido(self):
        self.partidos_perdidos += 1

    def agregar_goles(self, goles):
        self.goles += goles


class Partido:
    def __init__(self, equipo1, equipo2, estadio, fecha):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.estadio = estadio
        self.fecha = fecha

    def mostrar_partido(self):
        print(f"{self.equipo1.nombre} vs {self.equipo2.nombre} en el estadio {self.estadio} el {self.fecha}")


class Resultado:
    def __init__(self, partido, goles_e1, goles_e2):
        self.partido = partido
        self.goles_e1 = goles_e1
        self.goles_e2 = goles_e2

    def mostrar_resultado(self):
        print(f"Resultado: {self.partido.equipo1.nombre} {self.goles_e1} - {self.goles_e2} {self.partido.equipo2.nombre}")

