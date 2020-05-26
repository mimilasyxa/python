from tkinter import *
from tkinter import messagebox
 
def display_full_name():
    messagebox.showinfo("окно сообщения","Вас зовут " + name.get() + " " + surname.get() + " вы " + gender.get() + " вам " + age.get() + " лет/год/года, ваше любимое животное " + fav_animal.get() + " из еды вы любите " + fav_food.get()) 
 
root = Tk()
root.title("Анкета")
 
name = StringVar()
surname = StringVar()
gender = StringVar()
age = StringVar()
fav_animal = StringVar()
fav_food = StringVar()
 
name_label = Label(text = "Введите имя:")
surname_label = Label(text = "Введите фамилию:")
gender_label = Label(text = "Введите ваш пол")
age_label = Label(text = "Введите ваш возраст")
fav_animal_label = Label(text = "Ваше любимое животное?")
fav_food_label = Label(text = "Ваша любимая еда?")



 
name_label.grid(row = 0, column = 0, sticky = "w")
surname_label.grid(row=1, column=0, sticky = "w")
gender_label.grid(row = 2, column = 0, sticky = "w")
age_label.grid(row = 3, column = 0, sticky = "w")
fav_animal_label.grid(row = 4, column = 0, sticky = "w")
fav_food_label.grid(row = 5, column = 0, sticky = "w")



 
name_entry = Entry(textvariable = name)
surname_entry = Entry(textvariable = surname)
gender_entry = Entry(textvariable = gender)
age_entry = Entry(textvariable = age)
fav_animal = Entry(textvariable = fav_animal)
fav_food = Entry(textvariable = fav_food)



 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
gender_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
age_entry.grid(row = 3, column = 1, padx = 5, pady = 5)
fav_animal.grid(row = 4, column = 1, padx = 5, pady = 5)
fav_food.grid(row = 5, column = 1, padx = 5, pady = 5)




 
message_button = Button(text="показать", command=display_full_name)
message_button.grid(row=6,column=1, padx=5, pady=5, sticky="e")

root.mainloop()