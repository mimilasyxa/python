from tkinter import *

root = Tk()
root.title("Управление парикмахерской")
root.geometry("800x500")

arg_for_search = IntVar()
arg_for_del = IntVar()
date = StringVar()
surname = StringVar()
service = StringVar()
cost = StringVar()
arg_search = StringVar()
arg_find = StringVar()
output_label = Label(text="Вывод")

def change_search_arg():
    arg = arg_for_search.get()
    print(arg)



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

Radiobutton(text="По фамилии",value=2, variable = arg_for_search)\
        .grid(row=2, column = 6, sticky=W)

Radiobutton(text="По дате",value=3,  variable = arg_for_search)\
        .grid(row=2, column = 7, sticky=W)
message_button = Button(text="Найти", command = change_search_arg)
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

message_button = Button(text="Добавить")
message_button.grid(row=6,column=1, padx=5, pady=5, sticky="e")

delete_label = Label(text="Удаление")
Label(text="Значение")\
                        .grid(row=9, column=0, sticky="w")
delete_label.grid(row=7, column=0)
Radiobutton(text="Клиента",value=1, variable = arg_for_del)\
        .grid(row=8, column = 0, sticky=W)
Radiobutton(text="Услуги",value=2, variable = arg_for_del)\
        .grid(row=8, column = 1, sticky=W)

message_button = Button(text="Удалить")
message_button.grid(row=10,column=1, padx=5, pady=5, sticky="e")

root.mainloop()
