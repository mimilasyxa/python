from tkinter import *

clients={'Маша':['cтрижка_500', 'покраска_2500'], 'Аня':['покраска_1500'], 'Света':['стрижка_1000']}

def clear_1():
	l_list.pack_forget()
	btn_clear.pack_forget()

def clients_list():
	global l_list, btn_clear
	l_list = Label(text="\n".join(clients.keys()))
	l_list.pack()
	btn_clear = Button(text="clear list", background="#555", foreground="#ccc",
             padx="5", pady="5", font="16", command=clear_1)
	btn_clear.pack()


def add_data(k, v):
	x={k.get():v}
	global clients
	clients.update(x)
	e_name.pack_forget()
	e_data.pack_forget()
	btn_ok1.pack_forget()


def add_client():
	global e_name, e_data, btn_ok1
	k = StringVar()
	v = StringVar()
	e_name = Entry(textvariable=k)
	e_data = Entry(textvariable=v)
	e_name.pack()
	e_data.pack()
	btn_ok1=Button(text="ok", background="#555", foreground="#ccc",
             padx="5", pady="5", font="16", command=lambda: add_data(k,v))
	btn_ok1.pack()
	
def del_client():
	clients.pop(cl_del.get())

w = Tk()
w.title("example")
w.geometry("300x250")
btn_list = Button(text="list", background="#555", foreground="#ccc",
             padx="5", pady="5", font="16", command=clients_list)
btn_list.pack()

btn_add = Button(text="add client", background="#555", foreground="#ccc",
             padx="5", pady="5", font="16", command=add_client)
btn_add.pack()

btn_add = Button(text="del client", background="#555", foreground="#ccc",
             padx="5", pady="5", font="16", command=del_client)
btn_add.pack()

cl_del=StringVar()
e_del = Entry(textvariable=cl_del, width="10")
e_del.pack()

w.mainloop()
