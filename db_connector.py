import psycopg2

def conectar():
    dbname = 'tournament_app'
    user = 'postgres'
    password = 'bran0902'
    host = 'localhost'
    port = '5432'

    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
