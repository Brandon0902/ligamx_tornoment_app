class Equipo:
   def __init__(self,logotipo, jugador, dir_tecnico,nombre):
        self._logotipo = logotipo
        self._author = jugador
        self._dir_tecnico = dir_tecnico
        self._nombre = nombre

class Juagdor:
   def __init__(self,nombre, numero, nacionalidad,posicion,rol):
        self._nombre = nombre
        self._numero = numero
        self._nacionalidad = nacionalidad
        self._posicion = posicion
        self._rol = rol

class Torneo:
   def __init__(self,equipo, partidos,fechas):
        self._equipo = equipo
        self._partidos = partidos
        self._fechas = fechas


class Dir_tecnico:
   def __init__(self,nombre, nacionalidad,porcentaje):
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._porcentaje = porcentaje

class Tabla_posiciones:
   def __init__(self,torneo, equipo_torneo):
        self._torneo = torneo
        self._equipo_torneo = equipo_torneo


class Eq_torneo:
   def __init__(self,goles, puntos, partidos_ganados,partidos_empatados,partidos_perdidos):
        self._goles = goles
        self._puntos = puntos
        self._partidos_ganados = partidos_ganados
        self._partidos_empatados = partidos_empatados
        self._partidos_perdidos = partidos_perdidos

class Partidos:
   def __init__(self,equipo1, equipo2, estadio,fecha):
        self._equipo1 = equipo1
        self._equipo2= equipo2
        self._estadio = estadio
        self._fecha = fecha

class Resulatdo:
   def __init__(self,partido, goles_e1,goles_e2):
        self._partido = partido
        self._goles_e1 = goles_e1
        self._goles_e2 = goles_e2