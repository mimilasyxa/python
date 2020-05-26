import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
window.geometry('300x300')
 
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()
 
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Ruby ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I like neither')
    else:
        l.config(text='I love both')
 
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Ruby',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
 
window.mainloop()
