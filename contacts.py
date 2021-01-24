from os import path
from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

# database access
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name text, add1 text, add2 text, add3 text, add4 text, add5 text, telno text, email text, birthday text)")
        self.conn.commit()

    def fetch(self, name=''):
        self.cur.execute(
            "SELECT * FROM contacts ORDER BY name")
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, add1, add2, add3, add4, add5, telno, email, birthday):
        self.cur.execute("INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (name, add1, add2, add3, add4, add5, telno, email, birthday))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM contacts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, add1, add2, add3, add4, add5, telno, email, birthday):
        self.cur.execute("UPDATE contacts SET name = ?, add1 = ?, add2 = ?, add3 = ?, add4 = ?, add5 = ?, telno = ?, email = ?, birthday = ? WHERE id = ?",
                         (name, add1, add2, add3, add4, add5, telno, email, birthday, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


dbpath = path.abspath(path.join(path.dirname(__file__), 'contact.db'))

db = Database(dbpath)

# commands
def populate_list(name=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch(name):
        router_tree_view.insert('', 'end', values=row)


def populate_list2(query='select * from contacts'):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch2(query):
        router_tree_view.insert('', 'end', values=row)


def add_contact():
    db.insert(name_text.get(), add1_text.get(), add2_text.get(), add3_text.get(), add4_text.get(), add5_text.get(),
              telno_text.get(), email_text.get(), birthday_text.get())
    clear_text()
    populate_list()


def select_contact(event):
    try:
        global selected_item
        index = router_tree_view.selection()[0]
        selected_item = router_tree_view.item(index)['values']
        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        add1_entry.delete(0, END)
        add1_entry.insert(END, selected_item[2])
        add2_entry.delete(0, END)
        add2_entry.insert(END, selected_item[3])
        add3_entry.delete(0, END)
        add3_entry.insert(END, selected_item[4])
        add4_entry.delete(0, END)
        add4_entry.insert(END, selected_item[5])
        add5_entry.delete(0, END)
        add5_entry.insert(END, selected_item[6])
        telno_entry.delete(0, END)
        telno_entry.insert(END, selected_item[7])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[8])
        birthday_entry.delete(0, END)
        birthday_entry.insert(END, selected_item[9])
    except IndexError:
        pass


def remove_contact():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_contact():
    db.update(selected_item[0], name_text.get(), add1_text.get(), add2_text.get(), add3_text.get(), add4_text.get(), add5_text.get(),
              telno_text.get(), email_text.get(), birthday_text.get())
    populate_list()


def clear_text():
    name_entry.delete(0, END)
    add1_entry.delete(0, END)
    add2_entry.delete(0, END)
    add3_entry.delete(0, END)
    add4_entry.delete(0, END)
    add5_entry.delete(0, END)
    telno_entry.delete(0, END)
    email_entry.delete(0, END)
    birthday_entry.delete(0, END)


app = Tk()

# window structure
#frame 1 input fields and labels
frame_fields = Frame(app)
frame_fields.grid(row=0, column=0)
# space
space_label = Label(frame_fields, text=' ', font=('bold', 12))
space_label.grid(row=0, column=0, sticky=E)
# name
name_text = StringVar()
name_label = Label(frame_fields, text='  Name:', font=('bold', 12))
name_label.grid(row=1, column=0, sticky=E)
name_entry = Entry(frame_fields, textvariable=name_text, width=50)
name_entry.grid(row=1, column=1, sticky=W)
# add1
add1_text = StringVar()
add1_label = Label(frame_fields, text='  Address 1:', font=('bold', 12))
add1_label.grid(row=2, column=0, sticky=E)
add1_entry = Entry(frame_fields, textvariable=add1_text, width=50)
add1_entry.grid(row=2, column=1, sticky=W)
# add2
add2_text = StringVar()
add2_label = Label(frame_fields, text='  Address 2:', font=('bold', 12))
add2_label.grid(row=3, column=0, sticky=E)
add2_entry = Entry(frame_fields, textvariable=add2_text, width=50)
add2_entry.grid(row=3, column=1, sticky=W)
# add3
add3_text = StringVar()
add3_label = Label(frame_fields, text='  Address 3:', font=('bold', 12))
add3_label.grid(row=4, column=0, sticky=E)
add3_entry = Entry(frame_fields, textvariable=add3_text, width=50)
add3_entry.grid(row=4, column=1, sticky=W)
# add4
add4_text = StringVar()
add4_label = Label(frame_fields, text='  Address 4:', font=('bold', 12))
add4_label.grid(row=5, column=0, sticky=E)
add4_entry = Entry(frame_fields, textvariable=add4_text, width=50)
add4_entry.grid(row=5, column=1, sticky=W)
# add5
add5_text = StringVar()
add5_label = Label(frame_fields, text='  Address 5:', font=('bold', 12))
add5_label.grid(row=6, column=0, sticky=E)
add5_entry = Entry(frame_fields, textvariable=add5_text, width=50)
add5_entry.grid(row=6, column=1, sticky=W)
# telno
telno_text = StringVar()
telno_label = Label(frame_fields, text='  Tel. No:', font=('bold', 12))
telno_label.grid(row=7, column=0, sticky=E)
telno_entry = Entry(frame_fields, textvariable=telno_text, width=50)
telno_entry.grid(row=7, column=1, sticky=W)
# email
email_text = StringVar()
email_label = Label(frame_fields, text='  Email:', font=('bold', 12))
email_label.grid(row=8, column=0, sticky=E)
email_entry = Entry(frame_fields, textvariable=email_text, width=50)
email_entry.grid(row=8, column=1, sticky=W)
# birthday
birthday_text = StringVar()
birthday_label = Label(frame_fields, text='  Birthday:', font=('bold', 12))
birthday_label.grid(row=9, column=0, sticky=E)
birthday_entry = Entry(frame_fields, textvariable=birthday_text, width=50)
birthday_entry.grid(row=9, column=1, sticky=W)

#frame 2 buttons
frame_btns = Frame(app)
frame_btns.grid(row=1, column=0)

add_btn = Button(frame_btns, text='Add', width=12, command=add_contact)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove',
                    width=12, command=remove_contact)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update',
                    width=12, command=update_contact)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

#frame 3 contact list
frame_router = Frame(app)
frame_router.grid(row=2, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

columns = ['id', 'Name']
router_tree_view = Treeview(frame_router, columns=columns, show="headings")
router_tree_view.column("id", width=30)
for col in columns[1:]:
    router_tree_view.column(col, width=450)
    router_tree_view.heading(col, text=col)
router_tree_view.bind('<<TreeviewSelect>>', select_contact)
router_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_router, orient='vertical')
scrollbar.configure(command=router_tree_view.yview)
scrollbar.pack(side="right", fill="y")
router_tree_view.config(yscrollcommand=scrollbar.set)

app.title('Contacts')
app.geometry('525x575')

# Populate data
populate_list()

# Start program
app.mainloop()
