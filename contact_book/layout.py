import tkinter
import tkinter.messagebox as mb
import tkinter.ttk
from data import *

book = tkinter.Tk()
book.title('')
book.geometry('680x500')
book.resizable(False,False)
book.configure(background='snow2')
book_icon = tkinter.PhotoImage(file='photos/book.png')
book.iconphoto(True, book_icon)


def show():
    global tree
    demo_list = view()
    attributes = ['Name', 'Gender', 'Phone', 'Email']
    tree = tkinter.ttk.Treeview(frame3, selectmode='extended', columns=attributes, show='headings')

    vertical_scrollbar = tkinter.ttk.Scrollbar(frame3, orient='vertical', command=tree.yview)
    horizontal_scrollbar = tkinter.ttk.Scrollbar(frame3, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    tree.grid(column=0, row=0, sticky=tkinter.NSEW)
    vertical_scrollbar.grid(column=1, row=0, sticky=tkinter.NS)
    horizontal_scrollbar.grid(column=0, row=1, sticky=tkinter.EW)

    tree.heading(0, text='Name', anchor=tkinter.NW)
    tree.heading(1, text='Gender', anchor=tkinter.NW)
    tree.heading(2, text='Phone', anchor=tkinter.NW)
    tree.heading(3, text='Email', anchor=tkinter.NW)

    tree.column(0, width=150, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(0, width=100, anchor='nw')
    tree.column(0, width=200, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)


frame1 = tkinter.Frame(book, width=680, height=60, bg='snow4')
frame1.grid(row=0, column=0,padx=0, pady=1)

frame2 = tkinter.Frame(book, width=680, height=180, bg='snow2')
frame2.grid(row=1, column=0,padx=0, pady=1)

frame3 = tkinter.Frame(book, width=600, height=120, bg='snow2', relief='flat')
frame3.grid(row=2, column=0,columnspan=2,padx=0, pady=1, sticky=tkinter.NW)
show()


def insert():
    Name = name_entry.get()
    Gender = gender_entry.get()
    Phone = phone_entry.get()
    Email = email_entry.get()

    data = [Name, Gender, Phone, Email]
    if Name =='' or Gender =='' or Phone=='' or Email=='':
        mb.showinfo('data', 'Please fill in all the fields')
    else:
        add(data)
        mb.showinfo('data', 'Contact saved successfully!')
        name_entry.delete(0, 'end')
        gender_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')

    show()


def to_update():
    try:
        tree_data = tree.focus()
        tree_dict = tree.item(tree_data)
        tree_list = [str(value) for value in tree_dict['values']]
        

        name = str(tree_list[0])
        gender = str(tree_list[1])
        phone = str(tree_list[2])
        email = str(tree_list[3])

        name_entry.insert(0, name)
        gender_entry.insert(0, gender)
        phone_entry.insert(0, phone)
        email_entry.insert(0, email)

        def confirm():
            new_name = name_entry.get()
            new_gender = gender_entry.get()
            new_phone = phone_entry.get()
            new_email = email_entry.get()

            data = [name ,new_name, new_gender, new_phone, new_email]
            update(data)

            mb.showinfo('Success', 'Contact updated successfully!')

            name_entry.delete(0, 'end')
            gender_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            email_entry.delete(0, 'end')

            for widget in frame3.winfo_children():
                widget.destroy()

            confirm_button.destroy()

            show()


        confirm_button = tkinter.Button(frame2, text='confirm',height=1,width=10, bg='snow4', font=('Times'), fg='white', command=confirm)
        confirm_button.place(x=320,y=111)
    except IndexError:
        mb.showerror('Error', 'Please select a contact.')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dict = tree.item(tree_data)
        tree_list = tree_dict['values']
        key = str(tree_list[0])
        delete(key)

        mb.showinfo('Success', 'Contact deleted successfully!')

        for widget in frame3.winfo_children():
                widget.destroy()
        
        show()

    except:
        mb.showerror('Error', 'Please select a contact.')


def to_search():
    key = search_entry.get()
    data = search(key)
    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values=item)

    search_entry.delete(0, 'end')

app_name = tkinter.Label(frame1, text='Contact Book', font=('Times',22,'bold'), bg='snow4')
app_name.place(x=6, y=6)

name_label = tkinter.Label(frame2, text='Name', width=10, height=1,font=('Times',14), bg='snow2', anchor=tkinter.NW)
name_label.place(x=10, y=20)
name_entry = tkinter.Entry(frame2, width=25, justify='left', highlightthickness=1, relief='ridge')
name_entry.place(x=80, y=20)

gender_label = tkinter.Label(frame2, text='Gender', width=10, height=1,font=('Times',14), bg='snow2', anchor=tkinter.NW)
gender_label.place(x=10, y=50)
gender_entry = tkinter.ttk.Combobox(frame2, width=10)
gender_entry['values'] = ['Female', 'Male', 'Other']
gender_entry.place(x=80, y=50)

phone_label = tkinter.Label(frame2, text='Phone', width=10, height=1,font=('Times',14), bg='snow2', anchor=tkinter.NW)
phone_label.place(x=10, y=80)
phone_entry = tkinter.Entry(frame2, width=25, justify='left', highlightthickness=1, relief='ridge')
phone_entry.place(x=80, y=80)

email_label = tkinter.Label(frame2, text='Email', width=10, height=1,font=('Times',14), bg='snow2', anchor=tkinter.NW)
email_label.place(x=10, y=110)
email_entry = tkinter.Entry(frame2, width=25, justify='left', highlightthickness=1, relief='ridge')
email_entry.place(x=80, y=110)

search_button = tkinter.Button(frame2, text='search',height=1, bg='snow4', font=('Times'), fg='white', command=to_search)
search_button.place(x=320,y=20)
search_entry = tkinter.Entry(frame2, width=20, justify='left', font=('Times',12), highlightthickness=1, relief='ridge')
search_entry.place(x=380,y=20)

view_button = tkinter.Button(frame2, text='view',height=1,width=10, bg='snow4', font=('Times'), fg='white', command=show)
view_button.place(x=320,y=81)

add_button = tkinter.Button(frame2, text='add',height=1,width=10, bg='snow4', font=('Times'), fg='white', command=insert)
add_button.place(x=450,y=50)

update_button = tkinter.Button(frame2, text='update',height=1,width=10, bg='snow4', font=('Times'), fg='white', command=to_update)
update_button.place(x=450,y=81)

delete_button = tkinter.Button(frame2, text='delete',height=1,width=10, bg='snow4', font=('Times'), fg='white', command=to_remove)
delete_button.place(x=450,y=111)


book.mainloop()