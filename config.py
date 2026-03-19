import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta_concesionario_2024')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'concesionario_db')
    MYSQL_CURSORCLASS = 'DictCursor'
