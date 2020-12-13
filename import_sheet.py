import gspread
import psycopg2

key = "My Project 98121-c7fbad9dc31b.json"
t = "Reto Horarios"

gc = gspread.service_account(filename=key)
sh = gc.open(t) # open_by_key(), open_by_url()
sheet_instance = sh.get_worksheet(0)
records_data = sheet_instance.get_all_records()
print(records_data[0])
conn = None
try:
    conn = psycopg2.connect(
        host="localhost",
        database="timetable",
        user="postgres",
        password="1234abcd")

    cur = conn.cursor()

    for data in records_data:
        # inserta fila de datos
        cur.execute(
            'INSERT INTO %s (ID, FECHA, DIA, HORA_INICIO, HORA_FIN, GRUPO, PROFE) VALUES (%s, %s, %s, %s, %s, %s)',
            ("HORARIOS", data['ID'], data['FECHA'], data['DIA'], data['HORA INICIO'], data['HORA FIN'], data['GRUPO'], data['PROFE'])
        )
    conn.commit()
    cur.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()

create_table = """
CREATE TABLE HORARIOS(
   ID   INT              NOT NULL,
   FECHA VARCHAR (20)     NOT NULL, // DATE
   DIA  VARCHAR (20)             NOT NULL,
   HORA_INICIO  INT              NOT NULL, // TIME
   HORA_FIN   INT              NOT NULL, // TIME
   GRUPO    VARCHAR (20)             NOT NULL,
   PROFE    VARCHAR (20)              NOT NULL,  
   PRIMARY KEY (ID)
"""