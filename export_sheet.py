import gspread
import time


def write(data):
    key = "My Project 98121-c7fbad9dc31b.json"
    t = "Reto Horarios"

    gc = gspread.service_account(filename=key)
    sh = gc.open(t) # open_by_key(), open_by_url()
    sheet_instance = sh.get_worksheet(0)
    #records_data = sheet_instance.get_all_records()

    y=1
    while 1: # busca la ultima fila libre
        values_list = sheet_instance.row_values(y)
        print(values_list)
        if values_list==[]:
            break
        else:
            time.sleep(0.01) # espera para no superar el limite de peticiones de la api
        y+=1

    x = 1 # inserta la fila celda a celda
    for element in data: # añade cada columna de la nueva fila
        sheet_instance.update_cell(y, x, element)
        x+=1

write([7,"27/11/2020","Viernes","9:30","11:00","Apple","3874783Z"])