from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    mobile = e_mobile.get()

    if(id=="" or name=="" or mobile==""):
        MessageBox.showinfo("insert Status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkstu")
        cursor = con.cursor()
        cursor.execute("insert into student values('"+ id + "','"+ name +"','"+ mobile +"')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_mobile.delete(0, 'end')
        show()
        MessageBox.showinfo("insert status", "Inserted success")
        con.close()
        
def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete status", "ID is composary for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkstu")
        cursor = con.cursor()
        cursor.execute("delete from where id='"+ e_id.get() +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_mobile.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete status", "Deleted successful")
        con.close()

def update():
    id = e_id.get()
    name=e_name.get()
    mobile=e_mobile.get()

    if(id=="" or name=="" or mobile==""):
        MessageBox.showinfo("Update status", "All fiels are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkstu")
        cursor = con.cursor()
        cursor.execute("update student set name='"+ name +"', mobile='"+ mobile +"' where id='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_mobile.delete(0, 'end')
        show()
        MessageBox.showinfo("Update status", "Updated success")
        con.close()

def get():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch status", "ID is compalsary for read")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkstu")
        cursor = con.cursor()
        cursor.execute("select * from student where id='"+ e_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_mobile.insert(0, row[2])

        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="", database="tkstu")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0])+ '       '+ row[1]
        list.insert(list.size()+1, insertData)
    con.close()

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+MySql")
id=Label(root, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30)
name=Label(root, text="Enter name", font=('bold', 10))
name.place(x=20, y=60)
mobile=Label(root, text="Enter Mobile", font=('bold', 10))
mobile.place(x=20, y=90)
e_id=Entry()
e_id.place(x=150, y=30)
e_name=Entry()
e_name.place(x=150, y=60)
e_mobile=Entry()
e_mobile.place(x=150, y=90)
insert=Button(root, text="insert", font=("italic",10), bg="white", command=insert)
insert.place(x=20, y=140)
delete=Button(root, text="Delete", font=("italic",10), bg="white", command=delete)
delete.place(x=100, y=140)
update=Button(root, text="Update", font=("italic",10), bg="white", command=update)
update.place(x=180, y=140)
get=Button(root, text="Get", font=("italic",10), bg="white", command=get)
get.place(x=260, y=140)
list=Listbox(root)
list.place(x=390, y=30)
show()
root.mainloop()
