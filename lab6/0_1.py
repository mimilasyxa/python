import sqlite3
from tkinter import *

connect = sqlite3.connect("barbershop.sqlite")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS barbershop
                (id INTEGER primary key autoincrement,
                name varchar,
                service varchar,
                cost int)""")

def add_instance():
    cursor.execute(f"""INSERT INTO barbershop (name, service, cost)
                VALUES ('{surname.get()}', '{service.get()}', '{cost.get()}')""")


root = Tk()
root.title("Управление парикмахерской")
root.geometry("800x500")

arg_for_search = IntVar()
arg_for_del = IntVar()
date = StringVar()
surname = StringVar()
service = StringVar()
cost = IntVar()
arg_search = StringVar()
arg_find = StringVar()
output_label = Label(text="Вывод")
array = []

def change_search_arg():
    arg = arg_for_search.get()

def find_by():
    row = 5
    if arg_for_search.get() == 1:
        result =  cursor.execute(f"""SELECT * FROM barbershop WHERE name='{arg_find.get()}'""")
    if arg_for_search.get() == 2:
        result =  cursor.execute(f"""SELECT * FROM barbershop WHERE service='{arg_find.get()}'""")
    for key in result:
        array.append(Label(text = key[1] + " " + key[2] + " " + str(key[3]) + " рублей").grid(row = row, column = 6))
        print(key[1] + " " + key[2] + " " + str(key[3]) + " рублей")
        row+=1

def delete_user():
    if arg_for_del.get() == 1:
        cursor.execute(f"""DELETE FROM barbershop WHERE name='{arg_search.get()}'""")
    if arg_for_del.get() == 2:
        cursor.execute(f"""DELETE FROM barbershop WHERE service='{arg_search.get()}'""")


add_label = Label(text="Добаление")
surname_label = Label(text="Введите фамилию:")
service_label = Label(text="Введите услугу:")
cost_label = Label(text="Введите цену:")
date_label = Label(text="Введите дату;")

add_label.grid(row=1, column=0, sticky="w")
surname_label.grid(row=2, column=0, sticky="w")
service_label.grid(row=3, column=0, sticky="w")
cost_label.grid(row=4, column=0, sticky="w")
date_label.grid(row=5, column=0, sticky="w")

output_label.grid(row=1, column=5, sticky="w")
Label(text="Значение").grid(row=3, column = 5)
Entry(textvariable=arg_find)\
                              .grid(row=3, column = 6, sticky="w")
Radiobutton(text="По фамилии",value=1, variable = arg_for_search)\
        .grid(row=2, column = 5, sticky=W)

Radiobutton(text="По услуге",value=2, variable = arg_for_search)\
        .grid(row=2, column = 6, sticky=W)

message_button = Button(text="Найти", command = find_by)
message_button.grid(row=4,column=6, padx=5, pady=5, sticky="e")


find_entry = Entry(textvariable=arg_search)
surname_entry = Entry(textvariable=surname)
service_entry = Entry(textvariable=service)
cost_entry = Entry(textvariable=cost)
date_entry = Entry(textvariable=date)
 
surname_entry.grid(row=2,column=1, padx=5, pady=5)
service_entry.grid(row=3,column=1, padx=5, pady=5)
cost_entry.grid(row=4,column=1, padx=5, pady=5)
date_entry.grid(row=5,column=1, padx=5, pady=5)
find_entry.grid(row=9,column=1, padx=5, pady=5)

message_button = Button(text="Добавить", command= add_instance)
message_button.grid(row=6,column=1, padx=5, pady=5, sticky="e")

delete_label = Label(text="Удаление")
Label(text="Значение")\
                        .grid(row=9, column=0, sticky="w")
delete_label.grid(row=7, column=0)
Radiobutton(text="Клиента",value=1, variable = arg_for_del)\
        .grid(row=8, column = 0, sticky=W)
Radiobutton(text="Услуги",value=2, variable = arg_for_del)\
        .grid(row=8, column = 1, sticky=W)

message_button = Button(text="Удалить", command = delete_user)
message_button.grid(row=10,column=1, padx=5, pady=5, sticky="e")

root.mainloop()
