import pymysql


def get_connection():
    """
    Создаёт подключение к базе данных
    """
    return pymysql.connect(
        host="localhost",
        user="root",
        password="2281337",
        database="pizzeria",
        cursorclass=pymysql.cursors.DictCursor
    )