import pymysql
from tkinter import *  # библиотека для создания GUI
from tkinter import ttk   # для отображеня иерархических данных
from tkinter import messagebox  # для отоброжения диалоговых окон с сообщениями

import tkinter as tk
from config import host , user, password, db_name

# connection later

def connection():
    conn = pymysql.connect(       # подключение к БД
        host=host, 
        port=3306,
        user=user,
        password=password,
        db=db_name) 
    return conn  

def refreshTable(): # функция для обновления данных в виджете Treeview. Она очищает все записи
                    # в Treeview, затем выполняет функцию read() для получения данных
                    #  из базы данных и вставляет их в Treeview
    
    for data in my_tree.get_children():
         my_tree.delete(data)
               
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8,column=0,columnspan=5, rowspan=11, padx=10,pady=20)

# gui
root = Tk()                   # создание графического окна приложения
root.title("Book shop")       # заголовок окна приложения
root.geometry("1180x720")     # устанавливает разменры окна приложения

my_tree = ttk.Treeview(root)  # создает объект ttk.Treeview, который будет использоваться
                              # для отображения данных в виде иерархического списка

# functions later
# placeholders for entry later

ph1 = tk.StringVar()  # переменные типа StringVar, используемые для установки значения
                      # в поля ввода (Entry) и получения данных оттуда
ph2 = tk.StringVar()  # ph1,ph2,ph3,ph4,ph5 будут использоваться в 
                      # качестве заполнителей для пяти полей ввода (Entry) 
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

# set placeholder values

def setph(word,num):  # функция для установки значений переменных 
                      # ph1, ph2, ph3, ph4, ph5 на основе переданного word и num
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    bookid = str(bookidEntry.get())
    booktitle = str(titleEntry.get())
    author = str(authorEntry.get())
    amount = str(amountEntry.get())
    price = str(priceEntry.get())

    if (bookid == "" or bookid == " ") or (booktitle=="" or booktitle==" ") or (author=="" or author==" ") or (amount=="" or amount==" ") or (price=="" or price==" "):
        messagebox.showinfo("Error", "Please fill up blank entry")
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO books VALUES ('"+bookid+"','"+booktitle+"', '"+author+"', '"+amount+"', '"+price+"') ")
            conn.commit()
            conn.close()
            
        except:
            messagebox.showinfo("Error", "Book is already exist")
            return

    refreshTable()  

def reset():
    desicion = messagebox.askquestion("Warning!", "Delete all data?")
    if desicion != "yes":
        return   
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books")
            conn.commit()
            conn.close()
            
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return        

    refreshTable()

def delete():
    desicion = messagebox.askquestion("Warning!", "Delete the selected data?")
    if desicion != "yes":
        return   
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE bookid= '"+str(deleteData)+"'")
            conn.commit()
            conn.close()
            
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return        

    refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        bookid = str(my_tree.item(selected_item)['values'][0])
        booktitle = str(my_tree.item(selected_item)['values'][1])
        author = str(my_tree.item(selected_item)['values'][2])
        amount = str(my_tree.item(selected_item)['values'][3])
        price = str(my_tree.item(selected_item)['values'][4])

        setph(bookid,1)
        setph(booktitle,2)
        setph(author,3)
        setph(amount,4)
        setph(price,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    bookid = str(bookidEntry.get())
    booktitle = str(titleEntry.get())
    author = str(authorEntry.get())
    amount = str(amountEntry.get())
   price = str(priceEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE bookid='"+
    bookid+"' or book_title='"+
    booktitle+"' or author='"+
    author+"' or amount='"+
    amount+"' or price='"+
    price+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedBookid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedBookid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    bookid = str(bookidEntry.get())
    booktitle = str(titleEntry.get())
    author = str(authorEntry.get())
    amount = str(amountEntry.get())
    price = str(priceEntry.get())

    if (bookid == "" or bookid == " ") or (booktitle == "" or booktitle == " ") or (author == "" or author == " ") or (amount == "" or amount == " ") or (price == "" or price == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
   else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET bookid='"+
            bookid+"', book_title='"+
            booktitle+"', author='"+
            author+"', amount='"+
            amount+"', price='"+
            price+"' WHERE bookid='"+
            selectedBookid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Book ID already exist")
            return

    refreshTable()

# gui
label = Label(root,text="Book shop", font=('Arial Bold', 30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

bookidLabel = Label(root, text="Book ID", font=('Arial', 15))
titleLabel = Label(root, text="Book title", font=('Arial', 15))
authorLabel = Label(root, text="Author", font=('Arial', 15))
amountLabel = Label(root, text="Quantity available", font=('Arial', 15))
priceLabel = Label(root, text="Price", font=('Arial', 15))

bookidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
titleLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
authorLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
amountLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
priceLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

#  Создание объектов Entry (поля ввода) с различными параметрами и связывавание
#  их с соответствующими заполнителями (StringVar переменными).
bookidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)  #  связанная переменная (StringVar), которая будет 
                                                                                   # использоваться для хранения значения, введенного пользователем
titleEntry = Entry(root,width=55,bd=5,font=('Arial', 15), textvariable = ph2)
authorEntry = Entry(root,width=55,bd=5,font=('Arial', 15), textvariable = ph3)
amountEntry = Entry(root,width=55,bd=5,font=('Arial', 15), textvariable = ph4)
priceEntry = Entry(root,width=55,bd=5,font=('Arial', 15), textvariable = ph5)

bookidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
titleEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
authorEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
amountEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
priceEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

# command later

addBtn = Button(
    root,text="Add",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#84F894', command=add
)
updateBtn = Button(
    root,text="Update",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#84E8F8', command=update
)
deleteBtn = Button(
    root,text="Delete",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#FF9999', command=delete
)
searchBtn = Button(
    root,text="Search",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#F4FE82', command=search
)
resetBtn = Button(
    root,text="Reset",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#F398FF', command=reset
)
selectBtn = Button(
    root,text="Select",padx=65,pady=25,width=10,bd=5,font=('Arial', 15),bg='#EEEEEE', command=select
)

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial', 15))
my_tree['columns'] = ("Book ID", "Book title", "Author", "Quantity available", "Price")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Book ID", anchor=W, width=170)
my_tree.column("Book title", anchor=W, width=150)
my_tree.column("Author", anchor=W, width=150)
my_tree.column("Quantity available", anchor=W, width=165)
my_tree.column("Price", anchor=W, width=150)

my_tree.heading("Book ID", text="Book ID", anchor=W)
my_tree.heading("Book title", text="Book title", anchor=W)
my_tree.heading("Author", text="Author", anchor=W)
my_tree.heading("Quantity available", text="Quantity available", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)

refreshTable()

root.mainloop()