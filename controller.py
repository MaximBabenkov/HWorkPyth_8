from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

def button_click():
    clr0 = "#ffffff"
    clr1 = "#000000"
    clr2 = "#4456F0"

    window = Tk()
    window.title("Phonebook using Tkinter, CSV")
    window.geometry("485x450")
    window.configure(background = clr0)
    window.resizable(width=FALSE, height=FALSE)


    frame_up = Frame(window, width=500, height=50, bg=clr2)
    frame_up.grid(row=0, column=0, padx=0, pady=1)

    frame_down = Frame(window, width=500, height=150, bg=clr0)
    frame_down.grid(row=1, column=0, padx=0, pady=1)

    frame_table = Frame(window, width=500, height=100, bg=clr0, relief="flat")
    frame_table.grid(row=2, column=0, padx=10, pady=1, columnspan=2, sticky=NW)


    def to_view():
        global tree
        list_header = ['Surname', 'Name', 'Telephone', 'Description']

        demo_list = view()

        tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

        y_scroll = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        x_scroll = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        tree.grid(column=0, row=0, sticky='nsew')
        y_scroll.grid(column=1, row=0, sticky='ns')
        x_scroll.grid(column=0, row=1, sticky='ew')

    
        tree.heading(0, text='Surname', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Telephone', anchor=NW)
        tree.heading(3, text='Description', anchor=NW)

        tree.column(0, width=120, anchor='nw')
        tree.column(1, width=50, anchor='nw')
        tree.column(2, width=100, anchor='nw')
        tree.column(3, width=180, anchor='nw')

        for item in demo_list:
            tree.insert('', 'end', values=item)

    to_view()

    def to_add():
        surname = e_surname.get()
        name = e_name.get()
        telephone = e_telephone.get()
        description = e_description.get()

        data = [surname, name, telephone, description]

        if surname == '' or name == '' or telephone == '' or description == '':
            messagebox.showwarning('Error', 'Please fill all the fields!')
        else:
            add(data)
            messagebox.showinfo('', 'Press OK to confirm')
            e_surname.delete(0,'end')
            e_name.delete(0,'end')
            e_telephone.delete(0,'end')
            e_description.delete(0,'end')

            to_view()


    def to_update():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']

            surname = str(tree_list[0])
            name = str(tree_list[1])
            telephone = str(tree_list[2])
            description = str(tree_list[3])

            e_surname.insert(0, surname)
            e_name.insert(0, name)
            e_telephone.insert(0, telephone)
            e_description.insert(0, description)

            def confirm():
                new_surname = e_surname.get()
                new_name = e_name.get()
                new_telephone = e_telephone.get()
                new_description = e_description.get()

                data = [new_surname, new_name, new_telephone, new_description]
                messagebox.showinfo('', 'Press OK to comfirm')
                update(data)

                e_surname.delete(0,'end')
                e_name.delete(0,'end')
                e_telephone.delete(0,'end')
                e_description.delete(0,'end')

        except IndexError:
            messagebox.showerror('Error','Select one record from table!')

    def to_delete():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_telephone = str(tree_list[2])
            delete(tree_telephone)
            messagebox.showinfo('','Press OK to confirm!')
            for widget in frame_table.winfo_children():
                widget.destroy()
            to_view()
        except IndexError:
            messagebox.showerror('Error','Select one record from table!')

    def to_search():
        telephone = e_search.get()
        data = search(telephone)

        def delete_command():
            tree.delete(*tree.get_children())
        delete_command()

        for item in data:
            tree.insert('', 'end', values=item)

        e_search.delete(0, 'end')



    app_name = Label(frame_up, text="MY PHONEBOOK", height=1, font=('Verdana 17 bold'), fg = clr0, bg=clr2)
    app_name.place(x=5, y=5)


    l_surname = Label(frame_down, text="Surname", width=20, height=1, font=('Ivy 10'), bg=clr0, anchor=NW)
    l_surname.place(x=10, y=20)
    e_surname = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
    e_surname.place(x=80, y=20)

    l_name = Label(frame_down, text="Name", width=20, height=1, font=('Ivy 10'), bg=clr0, anchor=NW)
    l_name.place(x=10, y=50)
    e_name = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
    e_name.place(x=80, y=50)

    l_telephone = Label(frame_down, text="Telephone", width=20, height=1, font=('Ivy 10'), bg=clr0, anchor=NW)
    l_telephone.place(x=10, y=80)
    e_telephone = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
    e_telephone.place(x=80, y=80)

    l_description = Label(frame_down, text="Description", width=20, height=1, font=('Ivy 10'), bg=clr0, anchor=NW)
    l_description.place(x=10, y=110)
    e_description = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
    e_description.place(x=80, y=110)

    b_search = Button(frame_down, text="Search", height=1, bg=clr2, fg=clr0, font=('Ivy 8 bold'), command=to_search)
    b_search.place(x=290, y=20)
    e_search = Entry(frame_down, width=16, justify="left", font=('Ivy 11'), highlightthickness=1, relief="solid")
    e_search.place(x=347, y=20)

    b_view = Button(frame_down, text="View", width=10, height=1, bg=clr2, fg=clr0, font=('Ivy 8 bold'), command=to_view)
    b_view.place(x=290, y=50)

    b_add = Button(frame_down, text="Add", width=10, height=1, bg=clr2, fg=clr0, font=('Ivy 8 bold'), command=to_add)
    b_add.place(x=400, y=50)

    b_update = Button(frame_down, text="Update", width=10, height=1, bg=clr2, fg=clr0, font=('Ivy 8 bold'), command=to_update)
    b_update.place(x=400, y=80)

    b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=clr2, fg=clr0, font=('Ivy 8 bold'), command=to_delete)
    b_delete.place(x=400, y=110)



    window.mainloop()