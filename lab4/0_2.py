from tkinter import *

root = Tk()
root.title("Платите налоги")
root.geometry("600x500")
workers = {"Петрович":10000, "Сидоров":12000, "Андре":11000, "Монкас":21000}
lastname = StringVar()
salary = IntVar()

def add_worker():
    workers[lastname.get()] = salary.get();

def decision_all():
    show_all("all")

def decision_tax():
    show_all("tax")

def show_all(status):
    row = 5
    for key in workers:
        percent = 10
        salary_full = workers[key]
        salary = workers[key]
        salary += salary * (percent / 100)
        taxes_ret = salary * 0.06
        taxes_fin = (salary - 12130 - taxes_ret) * 0.13
        taxes_prof = salary * 0.01
        award = salary * (percent / 100)
        salary = salary - (taxes_ret + taxes_fin + taxes_prof)
        if status == "all":
            Label(text=key + " получил " + str(salary_full) + " до налогов                                               ").grid(row=row,column = 0, sticky="w")
        if status == "tax":
            Label(text=key + " получил " + str(salary) + " , из которых " + str(award) +" - премия").grid(row=row,column = 0, sticky="w")
        row += 1

Label(text="Добавить человека").grid(row=0,column = 0, sticky="w")
Label(text="Фамилия").grid(row=1,column = 0, sticky="w")
Label(text="Зарплата").grid(row=2,column = 0, sticky="w")
Button(text="Добавить", command = add_worker).grid(row=2, column=2,sticky="e")
Entry(textvariable=lastname).grid(row=1,column=1, sticky="w")
Entry(textvariable=salary).grid(row=2,column=1, sticky="w")
Label(text="Вывести").grid(row=3, column=0, sticky="w")
Button(text="Всё без налогов и премии", command = decision_all).grid(row=4, column=0,sticky="e")
Button(text="Всё после налогов и премии", command = decision_tax).grid(row=4, column=1,sticky="e")

root.mainloop()
