from models import Equipo, Jugador, Torneo, DirectorTecnico, Partido, TablaPosiciones, Resultado, EquipoTorneo
from db_connector import conectar

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


def agregar_equipo(connection, torneo):
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

    if connection:
        try:
            cursor = connection.cursor()

            # Insertar el director técnico en la tabla 'director_tecnico'
            query_dt = "INSERT INTO director_tecnico (nombre, nacionalidad, porcentaje) VALUES (%s, %s, %s) RETURNING id;"
            cursor.execute(query_dt, (dt.nombre, dt.nacionalidad, dt.porcentaje))
            dt_id = cursor.fetchone()[0]

            # Insertar el equipo en la tabla 'equipo'
            query_equipo = "INSERT INTO equipo (logotipo, nombre, director_tecnico_id) VALUES (%s, %s, %s) RETURNING id;"
            cursor.execute(query_equipo, (logotipo, nombre, dt_id))
            equipo_id = cursor.fetchone()[0]

            # Confirmar la transacción
            connection.commit()

            # Cerrar el cursor
            cursor.close()

            print("Equipo agregado con éxito.")
            return Equipo(logotipo, jugadores, dt, nombre, id=equipo_id)
        except Exception as e:
            print(f"Error al agregar equipo: {e}")
            # Revertir la transacción en caso de error
            connection.rollback()
        finally:
            # No cerramos la conexión aquí, ya que la conexión se maneja externamente
            pass
    else:
        print("No hay conexión a la base de datos.")
        # En caso de que no haya conexión, puedes devolver un objeto Equipo sin ID
        return Equipo(logotipo, jugadores, dt, nombre)


def agregar_jugadores(connection, equipos, torneo):
    mostrar_equipos(connection, torneo)

    num_equipo = int(input("Seleccione el número del equipo al que desea agregar jugadores: ")) - 1
    
    if 0 <= num_equipo < len(equipos):
        equipo_seleccionado = equipos[num_equipo]
        num_jugadores = int(input("Ingrese la cantidad de jugadores a agregar: "))
        
        if connection:
            try:
                cursor = connection.cursor()

                for i in range(num_jugadores):
                    print(f"\nJugador {i + 1}:")
                    nombre_jugador = input("Ingrese el nombre del jugador: ")
                    numero = input("Ingrese el número del jugador: ")
                    nacionalidad = input("Ingrese la nacionalidad del jugador: ")
                    posicion = input("Ingrese la posición del jugador: ")
                    rol = input("Ingrese el rol del jugador: ")

                    # Insertar el jugador en la tabla 'jugador'
                    query_jugador = """
                        INSERT INTO jugador (equipo_id, nombre, numero, nacionalidad, posicion, rol)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """
                    cursor.execute(query_jugador, (equipo_seleccionado.id, nombre_jugador, numero, nacionalidad, posicion, rol))

                # Confirmar la transacción
                connection.commit()

                # Cerrar el cursor
                cursor.close()

                print("Jugadores agregados con éxito.")
            except Exception as e:
                print(f"Error al agregar jugadores: {e}")
                # Revertir la transacción en caso de error
                connection.rollback()
            finally:
                # No cerramos la conexión aquí, ya que la conexión se maneja externamente
                pass
        else:
            print("No hay conexión a la base de datos.")
    else:
        print("Número de equipo inválido.")


def mostrar_equipos(connection, torneo):
    if connection:
        try:
            cursor = connection.cursor()

            # Obtener equipos del torneo desde la base de datos
            query_equipos = """
                SELECT e.nombre
                FROM equipo_torneo et
                JOIN equipo e ON et.equipo_id = e.id
                WHERE et.torneo_id = %s;
            """
            cursor.execute(query_equipos, (torneo.id,))
            equipos = cursor.fetchall()

            # Cerrar el cursor
            cursor.close()

            if equipos:
                print("Equipos disponibles:")
                for i, equipo in enumerate(equipos, start=1):
                    print(f"{i}. {equipo[0]}")
            else:
                print("No hay equipos registrados en el torneo.")
        except Exception as e:
            print(f"Error al mostrar equipos: {e}")
    else:
        print("No hay conexión a la base de datos.")

# Luego, puedes llamar a la función en tu código principal, pasando el torneo actual como argumento.



def crear_torneo(connection):
    nombre_torneo = input("Ingrese el nombre del torneo: ")
    
    if connection:
        try:
            cursor = connection.cursor()

            # Insertar el torneo en la tabla 'torneo'
            query_torneo = "INSERT INTO torneo (nombre, fecha) VALUES (%s, CURRENT_DATE) RETURNING id;"
            cursor.execute(query_torneo, (nombre_torneo,))
            torneo_id = cursor.fetchone()[0]

            # Confirmar la transacción
            connection.commit()

            # Cerrar el cursor
            cursor.close()

            # Crear una instancia de TablaPosiciones
            torneo = Torneo(nombre_torneo, id=torneo_id)
            torneo.tabla_posiciones = TablaPosiciones(torneo)
            print("Torneo creado con éxito.")
            return torneo
        except Exception as e:
            print(f"Error al crear torneo: {e}")
            # Revertir la transacción en caso de error
            connection.rollback()
        finally:
            # No cerramos la conexión aquí, ya que la conexión se maneja externamente
            pass
    else:
        print("No hay conexión a la base de datos.")




def agregar_equipos_al_torneo(connection, torneo, equipos):
    mostrar_equipos(connection, torneo)
    equipos_seleccionados = []

    while True:
        num_equipo = int(input("Seleccione el número del equipo que desea agregar al torneo (0 para terminar): "))
        
        if num_equipo == 0:
            break

        if 1 <= num_equipo <= len(equipos):
            equipo_seleccionado = equipos[num_equipo - 1]

            if connection:
                try:
                    cursor = connection.cursor()

                    # Insertar la relación equipo-torneo en la tabla 'equipo_torneo'
                    query_equipo_torneo = """
                        INSERT INTO equipo_torneo (torneo_id, equipo_id, goles, puntos, partidos_ganados,
                        partidos_empatados, partidos_perdidos)
                        VALUES (%s, %s, 0, 0, 0, 0, 0);
                    """
                    cursor.execute(query_equipo_torneo, (torneo.id, equipo_seleccionado.id))

                    # Confirmar la transacción
                    connection.commit()

                    # Cerrar el cursor
                    cursor.close()

                    equipos_seleccionados.append(equipo_seleccionado)
                    print(f"Equipo '{equipo_seleccionado.nombre}' agregado al torneo.")
                except Exception as e:
                    print(f"Error al agregar equipo al torneo: {e}")
                    # Revertir la transacción en caso de error
                    connection.rollback()
                finally:
                    # No cerramos la conexión aquí, ya que la conexión se maneja externamente
                    pass
            else:
                print("No hay conexión a la base de datos.")
        else:
            print("Número de equipo inválido. Por favor, seleccione un número de equipo válido.")

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


def mostrar_jugadores(connection, equipos):
    mostrar_equipos(equipos)
    num_equipo = int(input("Seleccione el número del equipo para mostrar jugadores: ")) - 1
    
    if 0 <= num_equipo < len(equipos):
        equipo_seleccionado = equipos[num_equipo]

        if connection:
            try:
                cursor = connection.cursor()

                # Obtener jugadores del equipo desde la base de datos
                query_jugadores = """
                    SELECT nombre, numero, nacionalidad, posicion, rol
                    FROM jugador
                    WHERE equipo_id = %s;
                """
                cursor.execute(query_jugadores, (equipo_seleccionado.id,))
                jugadores = cursor.fetchall()

                # Cerrar el cursor
                cursor.close()

                print(f"Jugadores del equipo '{equipo_seleccionado.nombre}':")
                for jugador in jugadores:
                    nombre, numero, nacionalidad, posicion, rol = jugador
                    print(f"Nombre: {nombre}, Número: {numero}, Nacionalidad: {nacionalidad}, Posición: {posicion}, Rol: {rol}")
            except Exception as e:
                print(f"Error al mostrar jugadores: {e}")
        else:
            print("No hay conexión a la base de datos.")
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

    # Obtener la conexión a la base de datos
    connection = conectar()  # Asegúrate de que tu función conectar() devuelve la conexión

    torneo = crear_torneo(connection)  # Pasa la conexión como argumento

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipo = agregar_equipo(connection, torneo)
            if equipo:
                equipos.append(equipo)
                print("Equipo agregado con éxito.")
        elif opcion == "2":
            if equipos:
                agregar_jugadores(connection, equipos, torneo)
            else:
                print("No hay equipos disponibles. Agregue equipos primero.")
        elif opcion == "3":
            if equipos:
                mostrar_equipos(connection, torneo)
                agregar_equipos_al_torneo(connection, torneo, equipos)
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
            mostrar_equipos(connection, torneo)
        elif opcion == "7":
            mostrar_partidos(equipos, torneo)
        elif opcion == "8":
            torneo.tabla_posiciones.mostrar_tabla_posiciones()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    # Cerrar la conexión al salir del programa
    if connection:
        connection.close()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
