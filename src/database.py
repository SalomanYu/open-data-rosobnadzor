import psycopg2
from models import Certificate, ActualEducationOrganization 


# ПРЕДПОЛАГАЕТСЯ ЧТО ТАБЛИЦЫ УЖЕ СОЗДАНЫ В POSTGRES
# Не стал добавлять константы в переменные окружения, т.к. проект простенький и выполняется на локальном сервере 
DATABASE = "rosobnazdor"
USER = "demouser"
PASSWORD = "password"
HOST = "127.0.0.1"
PORT = "5432"


def check_of_existence_tables():
    TABLE1 = "certificate"
    TABLE2 = "actual_education_organization"

    connect = try_connect_to_db()
    if connect is None: return "Failed to connect to the database..."
    cursor = connect.cursor()
    try:
        cursor.execute(f"SELECT * FROM {TABLE1};")
        connect.commit()
    except:
        connect.close()
        return f"Table {TABLE1} is not exists!"
    try:
        cursor.execute(f"SELECT * FROM {TABLE2};")
        connect.commit()
    except:
        return f"Table {TABLE2} is not exists!"
    finally:
        connect.close()

def try_connect_to_db():
    try:connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    except: return None
    return connection


def add_to_table(tablename: str, data: list[Certificate | ActualEducationOrganization], columns_count: int = 29):
    """Важно передавать данные в базу в правильном порядке, в таком каком они записаны в БД"""
    connect = try_connect_to_db()
    if connect is None: return
    cursor = connect.cursor()
    
    columns = ",".join("%s" for _ in range(columns_count))
    cursor.executemany(f"INSERT INTO {tablename} VALUES({columns})", [tuple(i) for i in data])
    
    connect.commit()
    connect.close()    