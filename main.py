from models import Equipo, Jugador, Torneo, DirectorTecnico, Partido, TablaPosiciones, Resultado, EquipoTorneo

def mostrar_menu():
     print("Menu:")
     print("1. Agregar equipo")
     print("2. Agregar jugadores")
     print("3. Agregar equipos al torneo")
     print("4. Agregar partidos al torneo")
     print("5. Ingresar resultados de los partidos")
     print("6. Mostrar Jugadores")
     print("7. Mostrar partidos")
     print("8. Mostrar tabla de Posiciones")
     print("9. Salir")

def agregar_equipo():
    logotipo = input("Ingrese el logotipo del equipo: ")
    nombre = input("Ingrese el nombre del equipo: ")
   
    nombre_dt = input("Ingrese el nombre del director técnico: ")
    nacionalidad_dt = input("Ingrese la nacionalidad del director técnico: ")
    porcentaje_dt = None
    while porcentaje_dt is None:
        try:
            porcentaje_dt = int(input("Ingrese el porcentaje del director técnico: "))
        except ValueError:
            print("Error: Porcentaje inválido. Ingrese un valor numérico entero.")

    dt = DirectorTecnico(nombre_dt, nacionalidad_dt, porcentaje_dt)
    
    jugadores = []
    return Equipo(logotipo, jugadores, dt, nombre)


def agregar_jugadores(equipos):
    mostrar_equipos(equipos)
    num_equipo = int(input("Seleccione el número del equipo al que desea agregar jugadores: ")) - 1
    
    if 0 <= num_equipo < len(equipos):
        equipo_seleccionado = equipos[num_equipo]
        num_jugadores = int(input("Ingrese la cantidad de jugadores a agregar: "))
        for i in range(num_jugadores):
            print(f"\nJugador {i+1}:")
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            numero = input("Ingrese el número del jugador: ")
            nacionalidad = input("Ingrese la nacionalidad del jugador: ")
            posicion = input("Ingrese la posición del jugador: ")
            rol = input("Ingrese el rol del jugador: ")

            jugador = Jugador(nombre_jugador, numero, nacionalidad, posicion, rol)
            equipo_seleccionado.jugadores.append(jugador)
        print("Jugadores agregados con éxito.")
    else:
        print("Número de equipo inválido.")

def mostrar_equipos(equipos):
    print("Equipos disponibles:")
    for i, equipo in enumerate(equipos, start=1):
        print(f"{i}. {equipo.nombre}")

def crear_torneo():
    nombre_torneo = input("Ingrese el nombre del torneo: ")
    torneo = Torneo(nombre_torneo)
    torneo.tabla_posiciones = TablaPosiciones(torneo)  # Crear una instancia de TablaPosiciones
    return torneo


def agregar_equipos_al_torneo(torneo, equipos):
    mostrar_equipos(equipos)
    equipos_seleccionados = []

    while True:
        num_equipo = int(input("Seleccione el número del equipo que desea agregar al torneo (0 para terminar): "))
        
        if num_equipo == 0:
            break

        if 1 <= num_equipo <= len(equipos):
            equipo_seleccionado = equipos[num_equipo - 1]
            equipos_seleccionados.append(equipo_seleccionado)
            print(f"Equipo '{equipo_seleccionado.nombre}' agregado al torneo.")
        else:
            print("Número de equipo inválido.")

    for equipo in equipos_seleccionados:
        torneo.agregar_equipo(equipo)


def agregar_partido_al_torneo(torneo):
    equipo1_nombre = input("Ingrese el nombre del primer equipo: ")
    equipo2_nombre = input("Ingrese el nombre del segundo equipo: ")
    estadio = input("Ingrese el nombre del estadio: ")
    fecha = input("Ingrese la fecha del partido: ")

    equipo1 = None
    equipo2 = None

    for equipo in torneo.equipos:
        if equipo.nombre == equipo1_nombre:
            equipo1 = equipo
        elif equipo.nombre == equipo2_nombre:
            equipo2 = equipo

    if equipo1 is None or equipo2 is None:
        print("Error: Los equipos ingresados no están registrados.")
        return

    partido = Partido(equipo1, equipo2, estadio, fecha)
    torneo.partidos.append(partido)
    print("Partido agregado con éxito.")

def ingresar_resultados(torneo):
    fecha_partido = input("Ingrese la fecha del partido (dd/mm/yyyy): ")
    equipo1_nombre = input("Ingrese el nombre del primer equipo: ")
    equipo2_nombre = input("Ingrese el nombre del segundo equipo: ")
    goles_equipo1 = int(input("Ingrese la cantidad de goles del primer equipo: "))
    goles_equipo2 = int(input("Ingrese la cantidad de goles del segundo equipo: "))

    partido_encontrado = None
    for partido in torneo.partidos:
        if partido.fecha == fecha_partido and partido.equipo1.nombre == equipo1_nombre and partido.equipo2.nombre == equipo2_nombre:
            partido_encontrado = partido
            break

    if partido_encontrado is not None:
        resultado = Resultado(partido_encontrado, goles_equipo1, goles_equipo2)
        torneo.registrar_resultado(resultado)
        print("Resultado registrado con éxito.")
    else:
        print("Error: No se encontró el partido.")


def mostrar_jugadores(equipos):
    mostrar_equipos(equipos)
    num_equipo = int(input("Seleccione el número del equipo para mostrar jugadores: ")) - 1
    
    if 0 <= num_equipo < len(equipos):
        equipo_seleccionado = equipos[num_equipo]
        print(f"Jugadores del equipo '{equipo_seleccionado.nombre}':")
        for jugador in equipo_seleccionado.jugadores:
            print(f"Nombre: {jugador.nombre}, Número: {jugador.numero}, Nacionalidad: {jugador.nacionalidad}, Posición: {jugador.posicion}, Rol: {jugador.rol}")
    else:
        print("Número de equipo inválido.")

def mostrar_partidos(equipos, torneo):
    print("Partidos del torneo:")
    for partido in torneo.partidos:
        resultado_encontrado = False
        for resultado in torneo.resultados:
            if resultado.partido == partido:
                print(f"{partido.equipo1.nombre} vs {partido.equipo2.nombre} en el estadio {partido.estadio} el {partido.fecha}")
                resultado_encontrado = True
                break
        if not resultado_encontrado:
            print(f"{partido.equipo1.nombre} vs {partido.equipo2.nombre} en el estadio {partido.estadio} el {partido.fecha} (sin resultado)")


def main():
    equipos = []
    torneo = crear_torneo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipo = agregar_equipo()
            equipos.append(equipo)
            print("Equipo agregado con éxito.")
        elif opcion == "2":
            if equipos:
                agregar_jugadores(equipos)
            else:
                print("No hay equipos disponibles. Agregue equipos primero.")
        elif opcion == "3":
            if equipos:
                agregar_equipos_al_torneo(torneo, equipos)
            else:
                print("No hay equipos disponibles. Agregue equipos primero.")
        elif opcion == "4":
            num_partidos = int(input("Ingrese la cantidad de partidos que desea agregar: "))
            for i in range(num_partidos):
                print(f"\nPartido {i+1}:")
                agregar_partido_al_torneo(torneo)
        elif opcion == "5":
            num_resultados = int(input("Ingrese la cantidad de resultados que desea ingresar: "))
            for i in range(num_resultados):
                print(f"\nResultado {i+1}:")
                ingresar_resultados(torneo)
        elif opcion == "6":
            mostrar_jugadores(equipos)
        elif opcion == "7":
            mostrar_partidos(equipos, torneo)
        elif opcion == "8":
            torneo.tabla_posiciones.mostrar_tabla_posiciones()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
