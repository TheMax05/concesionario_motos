from app import mysql

class Cliente:

    @staticmethod
    def obtener_todos(nombre=None, documento=None, telefono=None):
        cur = mysql.connection.cursor()
        query = "SELECT * FROM clientes WHERE 1=1"
        params = []
        if nombre:
            query += " AND nombre LIKE %s"
            params.append(f"%{nombre}%")
        if documento:
            query += " AND documento LIKE %s"
            params.append(f"%{documento}%")
        if telefono:
            query += " AND telefono LIKE %s"
            params.append(f"%{telefono}%")
        query += " ORDER BY nombre ASC"
        cur.execute(query, params)
        clientes = cur.fetchall()
        cur.close()
        return clientes

    @staticmethod
    def obtener_por_id(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cur.fetchone()
        cur.close()
        return cliente

    @staticmethod
    def crear(datos):
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO clientes (nombre, documento, telefono, email, direccion)
            VALUES (%s, %s, %s, %s, %s)
        """, (datos['nombre'], datos['documento'], datos['telefono'],
              datos['email'], datos['direccion']))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def actualizar(id, datos):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE clientes SET nombre=%s, documento=%s, telefono=%s,
            email=%s, direccion=%s WHERE id=%s
        """, (datos['nombre'], datos['documento'], datos['telefono'],
              datos['email'], datos['direccion'], id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def eliminar(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM clientes WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
