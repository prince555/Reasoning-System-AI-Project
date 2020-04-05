from tkinter import *
import backend
window = Tk()
window.configure(bg="lightpink")

def get_selected_row(event):
    try:
        global select_tup
        index=list1.curselection()[0]
        select_tup = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, select_tup[1])
        e2.delete(0,END)
        e2.insert(END, select_tup[2])
        e3.delete(0,END)
        e3.insert(END, select_tup[3])
        e4.delete(0,END)
        e4.insert(END, select_tup[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_Disease():
    backend.insert(title_text.get(),author_text.get(),year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(), isbn_text.get()))

window.wm_title("Reasoning System")

#l1 = Label(window, text="Know the Disease by entering Symtoms", font=('arial', 18), bd=18, fg="blue")
#l1.grid()
l1 = Label(window, text="", bg="lightpink")
l1.grid(row=0,column=0)

l1 = Label(window, text="Symtom 1", font=('arial', 18), bd=18, bg="lightpink")
l1.grid(row=1,column=0)

l2 = Label(window, text="Symtom 2", font=('arial', 18), bd=18, bg="lightpink")
l2.grid(row=1,column=2)

l3 = Label(window, text="Symtom 3", font=('arial', 18), bd=18, bg="lightpink")
l3.grid(row=2,column=0)

l4 = Label(window, text="Disease", font=('arial', 18), bd=18, bg="lightpink")
l4.grid(row=2,column=2)

title_text = StringVar()
e1 = Entry(window, textvariable= title_text, font=('arial', 18), bd=18, bg="skyblue")
e1.grid(row=1, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable= author_text, font=('arial', 18), bd=18, bg="skyblue")
e2.grid(row=1, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable= year_text, font=('arial', 18), bd=18, bg="skyblue")
e3.grid(row=2, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable= isbn_text, font=('arial', 18), bd=18, bg="skyblue")
e4.grid(row=2, column=3)

list1 = Listbox(window, height=10, width=35, font=('arial', 18), bd=18, bg="yellow")
list1.grid(row=3, column =2, rowspan=6, columnspan=2,pady=20,padx=20)

list1.bind("<<ListboxSelect>>", get_selected_row)

sb1 =Scrollbar(window, bg="yellow")
sb1.grid(row=3, column=1 ,rowspan = 10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 =Button(window, text= "View All", width=12, command=view_command, font=('arial', 18), bd=18, bg="pink")
b1.grid(row=3, column=0,pady=10,padx=20)

b2 =Button(window, text= "Search Disease", width=12, command=search_command, font=('arial', 18), bd=18, bg="pink")
b2.grid(row=4, column=0,pady=10,padx=20)

b3 =Button(window, text= "Add Disease", width=12, command=add_Disease, font=('arial', 18), bd=18, bg="pink")
b3.grid(row=5, column=0,pady=10,padx=20)
window.mainloop()
