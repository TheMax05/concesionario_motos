from app import mysql

class Venta:

    @staticmethod
    def obtener_todas():
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT v.*, c.nombre AS nombre_cliente, c.documento,
                   ve.marca, ve.modelo, ve.cilindraje
            FROM ventas v
            JOIN clientes c  ON v.id_cliente  = c.id
            JOIN vehiculos ve ON v.id_vehiculo = ve.id
            ORDER BY v.fecha_venta DESC
        """)
        ventas = cur.fetchall()
        cur.close()
        return ventas

    @staticmethod
    def obtener_por_id(id):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT v.*, c.nombre AS nombre_cliente,
                   ve.marca, ve.modelo
            FROM ventas v
            JOIN clientes c   ON v.id_cliente  = c.id
            JOIN vehiculos ve ON v.id_vehiculo = ve.id
            WHERE v.id = %s
        """, (id,))
        venta = cur.fetchone()
        cur.close()
        return venta

    @staticmethod
    def crear(datos):
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO ventas (id_cliente, id_vehiculo, fecha_venta, valor, observacion)
            VALUES (%s, %s, %s, %s, %s)
        """, (datos['id_cliente'], datos['id_vehiculo'], datos['fecha_venta'],
              datos['valor'], datos['observacion']))
        cur.execute("UPDATE vehiculos SET estado='vendido' WHERE id=%s", (datos['id_vehiculo'],))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def total_ingresos():
        cur = mysql.connection.cursor()
        cur.execute("SELECT SUM(valor) AS total FROM ventas")
        resultado = cur.fetchone()
        cur.close()
        return resultado['total'] or 0

    @staticmethod
    def historial():
        return Venta.obtener_todas()
