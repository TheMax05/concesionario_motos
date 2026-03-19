from app import mysql

class Vehiculo:

    @staticmethod
    def obtener_todos(marca=None, modelo=None, precio_max=None, estado=None):
        cur = mysql.connection.cursor()
        query = "SELECT * FROM vehiculos WHERE 1=1"
        params = []
        if marca:
            query += " AND marca LIKE %s"
            params.append(f"%{marca}%")
        if modelo:
            query += " AND modelo LIKE %s"
            params.append(f"%{modelo}%")
        if precio_max:
            query += " AND precio <= %s"
            params.append(precio_max)
        if estado:
            query += " AND estado = %s"
            params.append(estado)
        query += " ORDER BY creado_en DESC"
        cur.execute(query, params)
        vehiculos = cur.fetchall()
        cur.close()
        return vehiculos

    @staticmethod
    def obtener_por_id(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM vehiculos WHERE id = %s", (id,))
        vehiculo = cur.fetchone()
        cur.close()
        return vehiculo

    @staticmethod
    def crear(datos):
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO vehiculos (marca, modelo, precio, cilindraje, color, anio, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (datos['marca'], datos['modelo'], datos['precio'],
              datos['cilindraje'], datos['color'], datos['anio'], datos['estado']))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def actualizar(id, datos):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE vehiculos SET marca=%s, modelo=%s, precio=%s,
            cilindraje=%s, color=%s, anio=%s, estado=%s
            WHERE id=%s
        """, (datos['marca'], datos['modelo'], datos['precio'],
              datos['cilindraje'], datos['color'], datos['anio'],
              datos['estado'], id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def eliminar(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM vehiculos WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def obtener_disponibles():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM vehiculos WHERE estado = 'disponible' ORDER BY marca")
        vehiculos = cur.fetchall()
        cur.close()
        return vehiculos
