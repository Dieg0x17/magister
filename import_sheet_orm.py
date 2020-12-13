# ORM
import os
from datetime import datetime
import django
from django.conf import settings
# django setup
path = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    USE_TZ = True,
    TIME_ZONE = "Europe/Madrid",
    BASE_DIR = path,
    INSTALLED_APPS = ['event_manager.cal',],
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'event_manager/db.sqlite3',
        }

        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'timetable',
        #     'USER': 'myuser',
        #     'PASSWORD': 'mypassword',
        #     'HOST': "localhost",
        #     'PORT': '5432',
        #     'OPTIONS': {
        #         'sslmode': 'disable',
        #     },
        # }
    },
)
django.setup()
from event_manager.cal.models import Event

import gspread

key = "My Project 98121-c7fbad9dc31b.json"
t = "Reto Horarios"

gc = gspread.service_account(filename=key)
sh = gc.open(t) # open_by_key(), open_by_url()
sheet_instance = sh.get_worksheet(0)
records_data = sheet_instance.get_all_records()

for data in records_data:
    # inserta fila de datos
    event = Event() # crear objeto ORM

    event.id = data['ID']
    dt_string = data['FECHA']
    dt = datetime.strptime(dt_string, "%d/%m/%Y")
    event.fecha = dt
    event.dia = data['DIA']
    dt_string1 = data['FECHA'] + " " + data['HORA INICIO'] # ejemplo "12/11/2018 09:15"
    dt_string2 = data['FECHA'] + " " + data['HORA FIN']
    # dd/mm/yyyy formato
    dt_1 = datetime.strptime(dt_string1, "%d/%m/%Y %H:%M")
    dt_2 = datetime.strptime(dt_string2, "%d/%m/%Y %H:%M")
    event.hora_inicio= dt_1
    event.hora_fin= dt_2
    event.grupo= data['GRUPO']
    event.profesor = data['PROFE']

    event.save() # persistencia en la bbdd