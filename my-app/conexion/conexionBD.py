

# Importando Libreria mysql.connector para conectar Python con MySQL
import pymysql as mysql 


def connectionBD():
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            db="crud_python"
            

        )
        if connection:
            print("Conexión exitosa a la BD")
            return connection

    except mysql.Error as error:
        print(f"No se pudo conectar: {error}")


connectionBD()
