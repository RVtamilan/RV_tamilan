from customtkinter import *
from tkcalendar import DateEntry
import tkinter
from tkinter import ttk,messagebox
from pymysql import *
con = connect(host="localhost",user= "hackereye",passwd="omega7lamda1024",database="tamilan")
cur = con.cursor()

def branch1():
     pid = StringVar()
     name = StringVar()
     price = StringVar()
     def clear():
          pid.set("")
          name.set("")
          price.set('')
     def display3():
          cur.execute("select * from items")
          rows = cur.fetchall()
          t0.delete(*t0.get_children())
          for r in rows:
               t0.insert("",END,values=r)
     
     
     def delete():
          Pid = pid.get()
          cur.execute(f"delete from items where ID={Pid}")
          con.commit()
          display3()
          clear()
     
     def update():

          Pid = pid.get()
          Name = name.get()
          Price = price.get()
          pd = d1.get_date()
          Pd = pd.strftime(f"%d-%m-%Y")
          ed = d2.get_date()
          Ed = ed.strftime(f"%d-%m-%Y")
          cur.execute(f"update items set NAME='{Name}',PRICE='{Price}',P_DATE='{Pd}',E_DATE='{Ed}' where ID = {Pid}")
          con.commit()
          display3()
          clear()

     def getdata(dark):
          srow = t0.focus()
          data = t0.item(srow)
          global row 
          row = data['values']
          pid.set(row[0])
          name.set(row[1])
          price.set(row[2])
          d1.set_date(row[3])
          d2.set_date(row[4])

     def add_date():
          Pid = pid.get()
          Name = name.get()
          Price = price.get()
          pkd = d1.get_date()
          Pkd = pkd.strftime(f"%d-%m-%Y")
          exd = d2.get_date()
          Exd = exd.strftime(f"%d-%m-%Y")

          if Pid =="" or Name =="" or Price =="" or Pkd==Exd :
               messagebox.showerror("INPUT ERROR","ENTER APPROPRIATE INFROMATIONS")
               return
          cur.execute(f"insert into items values('{Pid}','{Name}','{Price}','{Pkd}','{Exd}')")
          con.commit()
          display3()
          clear()
          
     
     root = CTkToplevel()
     root.geometry("1000x700")
     f0 =CTkFrame(root,width=990,height=60,fg_color='white',border_color='cyan',border_width=3)
     f0.place(x=0,y=2,anchor=tkinter.NW)
     l0 =CTkLabel(f0,text="DATA ENTRY ",text_color="black",font=("arial black",26,"italic",'bold'))
     l0.place(x=450,y=20,anchor=tkinter.NW)
     f1 = CTkFrame(root,width=400,height=500,border_color='white',border_width=3)
     f1.place(x=20,y=100)
     l1 = CTkLabel(f1,text="Product ID:",text_color="white",font=("arial black",16,"italic",'bold')).place(x=10,y=50,anchor=tkinter.NW)
     e1 = CTkEntry(f1,textvariable=pid,width=150,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=150,y=50,anchor=tkinter.NW)
     l2 =CTkLabel(f1,text='Product Name:',text_color='white',font=('arial black',16,'italic','bold')).place(x=10,y=100,anchor=tkinter.NW)
     e2 = CTkEntry(f1,textvariable=name,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=150,y=100,anchor=tkinter.NW)
     l3 =CTkLabel(f1,text='Price:',text_color='white',font=('arial black',16,'italic','bold')).place(x=10,y=150,anchor=tkinter.NW)
     e3 = CTkEntry(f1,textvariable=price,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=150,y=150,anchor=tkinter.NW)
     
     l4 =CTkLabel(f1,text='Packed Date:',text_color='white',font=('arial black',16,'italic','bold')).place(x=10,y=200,anchor=tkinter.NW)
     d1 = DateEntry(f1,selectmode = 'day',date_pattern='dd/MM/yyyy')
     d1.place(x=150,y=200,anchor=tkinter.NW)
     #e4 = CTkEntry(f1,textvariable=pkd,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=150,y=200,anchor=tkinter.NW)
     l5 =CTkLabel(f1,text='Expiry Date:',text_color='white',font=('arial black',16,'italic','bold')).place(x=10,y=250,anchor=tkinter.NW)
     d2 = DateEntry(f1,selectmode = 'day',date_pattern='dd/MM/yyyy')
     d2.place(x=150,y=250,anchor=tkinter.NW)
     #e5 = CTkEntry(f1,textvariable=exd,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=150,y=250,anchor=tkinter.NW)
     b1= CTkButton(f1,text='ADD DATA',fg_color="cyan",width=120,height=30,hover_color="#00FF00",corner_radius=10,font=('arial black',16,'bold'),command=add_date).place(x=10,y=320,anchor=tkinter.NW)
     b2= CTkButton(f1,text='DELETE DATA',fg_color="cyan",width=120,height=30,hover_color="#00FF00",corner_radius=10,font=('arial black',16,'bold'),command=delete).place(x=200,y=320,anchor=tkinter.NW)
     b3= CTkButton(f1,text='UPDATE DATA',fg_color="cyan",width=120,height=30,hover_color="#00FF00",corner_radius=10,font=('arial black',16,'bold'),command=update).place(x=10,y=400,anchor=tkinter.NW)
     b4= CTkButton(f1,text='CLEAR DATA',fg_color="cyan",width=120,height=30,hover_color="#00FF00",corner_radius=10,font=('arial black',16,'bold')).place(x=200,y=400,anchor=tkinter.NW)
     f2 =CTkScrollableFrame(root,width=500,height=550,border_color='cyan',fg_color='white',border_width=3)
     f2.place(x=450,y=100,anchor=tkinter.NW)
     t0 =ttk.Treeview(f2,columns=(1,2,3,4,5))
     t0.heading('1',text='Product ID')
     t0.heading('2',text='Product Name')
     t0.heading('3',text='Price')
     t0.heading('4',text='Packed Date')
     t0.heading('5',text='Expiry Date')
     t0['show']='headings'
     t0.pack(expand=True,fill='both')
     t0.bind('<ButtonRelease-1>',getdata)
     display3()

def branch2():
     cur.execute("select * from HISTORY")
     row  = cur.fetchall()
     root = CTkToplevel()
     root.geometry("400x500")
     root.resizable(False,False)
     f0 =CTkFrame(root,width=400,height=40,fg_color='white',border_color='cyan',border_width=3)
     f0.place(x=0,y=2,anchor=tkinter.NW)
     l0 =CTkLabel(f0,text="DATA HISTORY",text_color="black",font=("arial black",16,"italic",'bold'))
     l0.place(x=150,y=10,anchor=tkinter.NW)
     fr = CTkScrollableFrame(root,width=390,height=450,fg_color='white',border_color='cyan',border_width=3)
     fr.pack(side = 'left', pady = 50)
     st = ttk.Style()
     st.configure("myst.Treeview",font =('calibri',10,'bold'),rowheight=40)
     tree = ttk.Treeview(fr,columns=(1,2,3,4),style='myst.Treeview')
     tree.heading('1',text='NAME')
     tree.column('1',width=100)
     tree.heading('2',text='PRICE')
     tree.column('2',width=100)
     tree.heading('3',text='QUANTITY')
     tree.column('3',width=100)
     tree.heading('4',text='TOTAL PRICE')
     tree.column('4',width=100)
     tree.pack(side='left')
     tree['show'] = 'headings'
     tree.delete(*tree.get_children())
     for r in row:
          tree.insert("",END,values=r)

def branch3():
     root = CTkToplevel()
     root.geometry("500x650")
     L = CTkLabel(root,text="ABD SUPER MARKET,KUNDRATHUR,CHENNAI-69",bg_color='grey',text_color='white',font=('arial black',18.5,'bold'))
     L.pack()
     
     cur.execute("select * from bill")
     data = cur.fetchall()
     fr1 = CTkScrollableFrame(root,width=490,height=500,fg_color='black',border_color='cyan',border_width=3)
     fr1.pack(side = 'left')
     st1 = ttk.Style()
     st1.configure("myst1.Treeview",foreground='white',background='black',fieldbackground='black',font =('calibri',10,'bold'),rowheight=60,borderwidth=0)
     tree1 = ttk.Treeview(fr1,columns=(1,2,3,4),style='myst1.Treeview')
     tree1.heading('1',text='NAME')
     tree1.column('1',width=120)
     tree1.heading('2',text='PRICE')
     tree1.column('2',width=120)
     tree1.heading('3',text='QUANTITY')
     tree1.column('3',width=120)
     tree1.heading('4',text='TOTAL PRICE')
     tree1.column('4',width=120)
     tree1.pack(side='left')
     tree1['show'] = 'headings'
     tree1.delete(*tree1.get_children())
     for r in data:
          tree1.insert("",END,values=r)
     cur.execute("select sum(t_price) as total from bill")
     t = cur.fetchone()
     L1 = CTkLabel(root,text=f"THE TOTAL AMOUNT IS :{t[0]}",text_color='white',font=("arial",18,'bold'))
     L1.place(x=200,y=600,anchor=tkinter.NW)
     cur.execute("delete from bill")
     con.commit()
     display2()
     


def fetch():
	cur.execute("select * from items")
	rows = cur.fetchall()
	return rows
def display():
    t1.delete(*t1.get_children())
    for row in fetch():
        t1.insert("",END,values=row)
def display2():
     cur.execute("select * from bill")
     rows = cur.fetchall()
     t2.delete(*t2.get_children())
     for r in rows:
          t2.insert("",END,values=r)

def cls():
     ID.set("")
     QT.set("")

def enter(black):
     id = ID.get()
     qt =QT.get()
     cur.execute(f"select NAME,PRICE from items where ID = '{id}'")
     rv = cur.fetchone()
     print(rv)
     name ,price = rv[0],rv[1]
     tprice = (int(price))*(int(qt))
     cur.execute(f"insert into bill (name,n_price,quantity,t_price) values('{name}','{price}','{qt}','{tprice}')")
     con.commit()
     display2()
     cls()
     cur.execute(f"insert into HISTORY values('{name}','{price}','{qt}','{tprice}')")
     con.commit()

         
rv = CTk()
rv.title("SUPER MARKET BILLING SYSTEM")
rv.geometry("1366x768")
rv._set_appearance_mode("Dark-Blue")
ID =StringVar() 
QT =StringVar()
fr0 = CTkFrame(rv,width=1300,height=50,fg_color=r"#ffffcc",border_width=2,border_color=r"cyan").place(x=0,y=0,anchor=tkinter.NW)
l0 = CTkLabel(fr0,text="WELCOME TO  BILLING SYSTEM",text_color= r"#0a0f0f",bg_color=r"#ffffcc",font=('calibri',18,'bold')).place(x=500,y=10,anchor=tkinter.NW)
lf = CTkLabel(rv,text="Billing Section",text_color="white",font=("arial black",20,"italic",'bold')).place(x=100,y=100,anchor=tkinter.NW)
fr1 = CTkFrame(rv,width=870,height=70,border_color="white",border_width=2)
fr1.place(x=0,y=140,anchor=tkinter.NW)
rv.bind("<Return>",enter)
l1 = CTkLabel(fr1,text="product ID :",text_color="white",font=("arial black",16,"italic",'bold')).place(x=20,y=20,anchor=tkinter.NW)
e1 = CTkEntry(fr1,textvariable=ID,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=130,y=20,anchor=tkinter.NW)
l2= CTkLabel(fr1,text="Quantity :",text_color= "white",font=("arial black",16,"italic",'bold')).place(x=350,y=20,anchor=tkinter.NW)
e2 = CTkEntry(fr1,width=100,textvariable=QT,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=450,y=20,anchor=tkinter.NW)
l2= CTkLabel(fr1,text="Price :",text_color= "white",font=("arial black",16,"italic",'bold')).place(x=580,y=20,anchor=tkinter.NW)
e2 = CTkEntry(fr1,width=200,font=("arial black",16,"italic",'bold'),border_color="cyan").place(x=650,y=20,anchor=tkinter.NW)
bt1 = CTkButton(rv,text="Add DATA",text_color='black',fg_color="cyan",width=200,height=30,hover_color="#00FF00",corner_radius=10,font=('arial black',16,'bold'),command=branch1).place(x=50,y=300,anchor=tkinter.NW)
bt2 = CTkButton(rv,text="HISTORY",text_color='black',fg_color='cyan',width=200,height=30,hover_color='#FF00FF',corner_radius=10,font=('arial black',17,'bold'),command=branch2).place(x=320,y=300,anchor=tkinter.NW)
bt2 = CTkButton(rv,text="Generate Bill",text_color='black',fg_color='cyan',width=200,height=30,hover_color='#FF00FF',corner_radius=10,font=('arial black',17,'bold'),command=branch3).place(x=590,y=300,anchor=tkinter.NW)
st = ttk.Style()
st.configure("myst.Treeview",font =('calibri',10,'bold'),rowheight=40)
fr3 = CTkScrollableFrame(master=rv,width=1270,height=200,border_width=5,border_color='cyan')
fr3.place(x=10,y=470,anchor=tkinter.NW)
t1 = ttk.Treeview(fr3,columns=(1,2,3,4,5),style = "myst.Treeview")
t1.heading('1',text ="Product ID")
t1.heading('2',text ="Product Name")
t1.heading('3',text ='Price')
t1.heading('4',text ='Packed Date')
t1.heading('5',text ='Expire Date')
t1.column('1',width=250)
t1.column('2',width=250)
t1.column('3',width=250)
t1.column('4',width=250)
t1.column('5',width=250)
t1['show'] = 'headings'
t1.pack(side = 'left',padx=5,pady=5)
#sb1 = CTkScrollbar(fr3,orientation= 'vertical',command=t1.yview).pack(side = 'right',fill = 'y')
#t1.configure(yscrollcommand=sb1.set)
display()
fr2= CTkScrollableFrame(rv,width=380,height=370,fg_color="white",border_color="cyan",border_width=5)
fr2.place(x=1300,y= 70,anchor = tkinter.NE)
#sb2 = CTkScrollbar(fr2,orientation='horizontal').pack()
t2 = ttk.Treeview(fr2,columns=(1,2,3,4))
t2.heading('1',text ='Product')
t2.heading('2',text ='Price')
t2.heading('3',text ='Quantity')
t2.heading('4',text ='T Price')
t2['show']='headings'
t2.pack(side='left')
display2()
rv.mainloop()