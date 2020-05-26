import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
window.geometry('100x100')
goods = {"Рыба":100}
 
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()

 
def sum_up(event):
	print(event)

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Рыба',variable=var1, onvalue=1, offvalue=0, command=sum_up)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=sum_up)
c2.pack()

frame = tk.Frame(window, width = 100, height = 100)
frame.bind("<Button-1>", sum_up)
frame.pack()
print(var1)

window.mainloop()
