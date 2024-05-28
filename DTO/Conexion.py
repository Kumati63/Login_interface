import pymysql


class Conexion:  # El codigo de conexion siempre sera el mismo
    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        self.cursor = self.db.cursor()

    def ejecuta_query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor

    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
