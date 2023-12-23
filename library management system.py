import tkinter
import tkcalendar
from datetime import *
from tkinter import ttk,messagebox
from customtkinter import *
from pymysql import *
con = connect(host="localhost",user= "hackereye",passwd="omega7lamda1024",database="tamilan")
cur = con.cursor()


def branch():
    bid = StringVar()
    sid=StringVar() 
    sname=StringVar()
    sclass =StringVar()
    def delete():
        srow = t2.focus()
        data = t2.item(srow)
        row = data["values"]
        cur.execute(f"delete from borrow where BID='{row[0]}'")
        con.commit()
        t2.delete(*t2.get_children())
        for row in fetch1():
            t2.insert("",END,values=row)
    def clear1():
        bid.set("")
        sid.set("")
        sname.set("")
        sclass.set("")
    def fetch1():
        cur.execute("select * from borrow")
        rows = cur.fetchall()
        return rows
    def insert1(id,id2,name,class1,dt1,dt2):
        cur.execute(f"insert into borrow values('{id}','{id2}','{name}','{class1}','{dt1}','{dt2}')")
        con.commit()
    def add_data1():
        Bid=bid.get()
        Sid=sid.get()
        Sname =sname.get()
        Sclass =sclass.get()
        date0 = d1.get_date()
        rv = date.today()
        date2 = f"{rv.day}-{rv.month}-{rv.year}"
        if bid == "" or sid == '' or sname == "" or sclass == "" :
            messagebox.showerror('INPUT ERROR','ENTER ALL DETAILS')
            return
        insert1(Bid,Sid,Sname,Sclass,date2,date0)
        clear1()
        t2.delete(*t2.get_children())
        for row in fetch1():
            t2.insert("",END,values=row)
        

    
    top = CTkToplevel()
    top.geometry("1100x650")
    f1 = CTkFrame(top,width=1100,height=50,fg_color="grey",border_width=2,border_color=r"#00BEFF")
    f1.place(relx=0,rely=0,anchor=tkinter.NW)
    lb0 = CTkLabel(f1,text="BORROWER INFORMATIONS",fg_color="grey",text_color= "white",font =('calibri',16,'bold'))
    lb0.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    lb1 = CTkLabel(top,text="BOOK ID:",text_color='red',font=('arial black',12,'bold')).place(x=90,y=100,anchor=tkinter.NW)
    eb1=CTkEntry(top,textvariable=bid,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=200,y=100,anchor=tkinter.NW)
    lb2 = CTkLabel(top,text="STUDENT ID:",text_color='red',font=('arial black',12,'bold')).place(x=450,y=100,anchor=tkinter.NW)
    eb2=CTkEntry(top,textvariable=sid,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=550,y=100,anchor=tkinter.NW)  
    lb3 = CTkLabel(top,text="STUD NAME:",text_color='red',font=('arial black',12,'bold')).place(x=90,y=150,anchor=tkinter.NW)
    eb3=CTkEntry(top,textvariable=sname,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=200,y=150,anchor=tkinter.NW)
    lb4 = CTkLabel(top,text="CLASS :",text_color='red',font=('arial black',12,'bold')).place(x=450,y=150,anchor=tkinter.NW)
    eb4=CTkEntry(top,textvariable=sclass,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=550,y=150,anchor=tkinter.NW)  
    lb5 = CTkLabel(top,text="DATE OF RETURN:",text_color='red',font=('arial black',12,'bold')).place(x=90,y=200,anchor=tkinter.NW)
    f2 = CTkFrame(master=top,width=1100,height=400,fg_color="white")
    f2.place(x =0,y=300,anchor=tkinter.NW)
    d1 = tkcalendar.DateEntry(top,selectmode ="day")
    d1.place(x=240,y=200,anchor=tkinter.NW)
    b4= CTkButton(top,text='ADD RECORD',text_color='white',width=150,command=add_data1,hover_color=r'#72ff98',corner_radius=20,fg_color=r'#3FCBFF').place(x=400,y=200,anchor=tkinter.NW)
    b5= CTkButton(top,text='DELETE RECORD',text_color='white',width=150,command=delete,hover_color=r'#72ff98',corner_radius=20,fg_color=r'#3FCBFF').place(x=600,y=200,anchor=tkinter.NW)
    t2 = ttk.Treeview(f2,columns=(1,2,3,4,5,6))
    t2.heading("1", text="BOOK ID")
    t2.column("1",width=100)
    t2.heading("2", text="STUDENT ID")
    t2.heading("3", text="STUD NAME")
    t2.heading("4", text="CLASS")
    t2.heading("5", text="DATE ON BORROWED")
    t2.heading("6", text="DATE OF RETURN")
    t2.place(x=0,y=0,anchor=tkinter.NW)
    t2["show"] = "headings"
    t2.delete(*t2.get_children())
    for row in fetch1():
        t2.insert("",END,values=row)

    

def fetch():
    cur.execute("select * from library")
    rows = cur.fetchall()
    return rows
def getdata(event):
    srow = tree.focus()
    data = tree.item(srow)
    global row
    row = data["values"]
    Id.set(row[0])
    Name.set(row[1])
    Author.set(row[2])
    Pages.set(row[3])
    Price.set(row[4])

def display():
    tree.delete(*tree.get_children())
    for row in fetch():
        tree.insert("",END,values=row)
def update(id,name,author,page,price):
    cur.execute(f"update library set NAME ='{name}',AUTHOR='{author}',PAGES={page},PRICE={price} where ID = {id}")
    con.commit()
def clear():
    Id.set("")
    Name.set("")
    Author.set("")
    Pages.set("")
    Price.set("")
def insert(id,name,author,page,price):
    cur.execute(f"insert into library values({id},'{name}','{author}',{page},{price})")
    con.commit()
def add_data():
    id=int(Id.get())
    page=int(Pages.get())
    price = int(Price.get())
    name =Name.get()
    author = Author.get()
    if id == 0 or name == '' or author == "" or page == 0 or price == 0:
        messagebox.showerror('INPUT ERROR','ENTER ALL DETAILS')
        return
    insert(id,Name.get(),Author.get(),page,price)
    clear()
    display()
def update_data():
    id=int(Id.get())
    page=int(Pages.get())
    price = int(Price.get())
    name =Name.get()
    author = Author.get()
    if id == 0 or name == '' or author == "" or page == 0 or price == 0:
        messagebox.showerror('INPUT ERROR','ENTER ALL DETAILS')
        return
    update(id,Name.get(),Author.get(),page,price)
    clear()
    display()
def remove(id):
    cur.execute(f"delete from library where Id={id}")
    con.commit()
def delete_data():
    remove(row[0])
    clear()
    display()

root=CTk()
set_appearance_mode("Dark-Blue")
root.geometry("1366x768")
root.title("LIBRARY MANAGEMENT SYSTEM")
Id=StringVar()
Name=StringVar()
Author=StringVar()
Pages=StringVar()
Price=StringVar()
frm = CTkFrame(master=root,width=1366,height=50,fg_color='grey',border_width=2,border_color=r"#00BEFF").place(relx=0,rely=0,anchor=tkinter.NW)
lt = CTkLabel(frm,text="Library Management System",text_color=r"#bfcdb4",bg_color='grey',font=('arial black',16,'bold'))
lt.pack(pady=10)
l1=CTkLabel(root,text="BOOK ID:",text_color='white',font=('arial black',12,'bold')).place(x=90,y=100,anchor=tkinter.NW)
e1=CTkEntry(root,textvariable=Id,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=200,y=100,anchor=tkinter.NW)
l2=CTkLabel(root,text="BOOK NAME:",text_color='white',font=('arial black',12,'bold')).place(x=90,y=160,anchor=tkinter.NW)
e2=CTkEntry(root,textvariable=Name,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(y=160,x=200,anchor=tkinter.NW)
l3=CTkLabel(root,text="BOOK AUTHOR:",text_color='white',font=('arial black',12,'bold')).place(x=90,y=220,anchor=tkinter.NW)
e3=CTkEntry(root,textvariable=Author,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(y=220,x=200,anchor=tkinter.NW)
l4=CTkLabel(root,text="BOOK PAGES:",text_color='white',font=('arial black',12,'bold')).place(x=90,y=280,anchor=tkinter.NW)
e4=CTkEntry(root,textvariable=Pages,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(y=280,x=200,anchor=tkinter.NW)
l5=CTkLabel(root,text="BOOK PRICE:",text_color='white',font=('arial black',12,'bold')).place(x=90,y=340,anchor=tkinter.NW)
e5=CTkEntry(root,textvariable=Price,font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(y=340,x=200,anchor=tkinter.NW)
b1= CTkButton(root,text='ADD DATA',text_color='white',command=add_data,corner_radius=20,fg_color=r'#3FCBFF').place(x=90,y=390,anchor=tkinter.NW)
b2= CTkButton(root,text='DELETE DATA',text_color='white',command=delete_data,corner_radius=20,fg_color=r'#3FCBFF',hover_color=r'#9872ff').place(x=260,y=390,anchor=tkinter.NW)
b3= CTkButton(root,text='UPDATE DATA',text_color='white',command=update_data,corner_radius=20,hover_color=r'#FF9872',fg_color=r'#3FCBFF').place(x=90,y=460,anchor=tkinter.NW)
b4= CTkButton(root,text='CLEAR DATA',text_color='white',command=clear,hover_color=r'#72ff98',corner_radius=20,fg_color=r'#3FCBFF').place(x=260,y=460,anchor=tkinter.NW)
b4= CTkButton(root,text='BOOK BORROWED',text_color='white',width=300,command=branch,hover_color=r'#72ff98',corner_radius=20,fg_color=r'#3FCBFF').place(x=90,y=520,anchor=tkinter.NW)

tfrm= CTkScrollableFrame(master=root,width=820,height=600,fg_color=r'#FFFDD0').place(relx=0.35,rely=0.1)

st = ttk.Style()
st.configure("myst.Treeview",font =('calibri',10,'bold'),rowheight=40)
tree = ttk.Treeview(tfrm,columns=(1,2,3,4,5),style="myst.Treeview")
tree.heading('1',text='ID')
tree.column('1',width=130)
tree.heading('2',text='BOOK NAME')
tree.heading('3',text='BOOK AUTHOR')
tree.heading('4',text='BOOK PAGES')
tree.column('4',width=150)
tree.heading('5',text='BOOK PRICE')
tree.column('5',width=150)
tree['show']= 'headings'
tree.bind("<ButtonRelease-1>",getdata)
tree.place(relx=0.35,rely=0.1)
display()
root.mainloop()
