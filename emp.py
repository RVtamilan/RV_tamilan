from customtkinter import *
from tkinter import ttk,messagebox
from PIL import Image
import tkinter
import tkcalendar
from pymysql import *

root = CTk()
root.geometry("1100x650")
root._set_appearance_mode('Dark-Green')
root.resizable(False,False)
frm = CTkFrame(master=root,width=1366,height=50,fg_color='grey',border_width=2,border_color=r"#00BEFF").place(relx=0,rely=0,anchor=tkinter.NW)
lt = CTkLabel(frm,text="Employees Management System",text_color=r"white",bg_color='grey',font=('arial black',16,'bold'))
lt.pack(pady=10)
Ig = Image.open('emp3.png')
IG = CTkImage(Ig,size=(200,250))
lo = CTkLabel(root,text='',image=IG).place(x=900,y=120,anchor=tkinter.NW )
Ig1 = Image.open('emp4.png')
IG1 = CTkImage(Ig1,size=(180,220))
l1 = CTkLabel(root,text='',image=IG1).place(x=0,y=180,anchor=tkinter.NW )

lb1 = CTkLabel(root,text="Employee ID:",text_color='cyan',font=('arial black',14,'bold')).place(x=85,y=100,anchor=tkinter.NW)
eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=200,y=100,anchor=tkinter.NW)
lb1 = CTkLabel(root,text="Employee Name:",text_color='cyan',font=('arial black',14,'bold')).place(x=420,y=100,anchor=tkinter.NW)
eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=560,y=100,anchor=tkinter.NW)   
lb1 = CTkLabel(root,text="Age:",text_color='cyan',font=('arial black',14,'bold')).place(x=770,y=100,anchor=tkinter.NW)
eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=100,border_color=r'#00BEFF').place(x=820,y=100,anchor=tkinter.NW)
lb1 = CTkLabel(root,text="D. O. J :",text_color='cyan',font=('arial black',14,'bold')).place(x=85,y=170,anchor=tkinter.NW)
#eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=180,y=170,anchor=tkinter.NW) 
d1 = tkcalendar.DateEntry(root,selectmode='day')
d1.place(x=180,y=170,anchor=tkinter.NW)
lb1 = CTkLabel(root,text="Gender :",text_color='cyan',font=('arial black',14,'bold')).place(x=340,y=170,anchor=tkinter.NW)
#eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=450,y=170,anchor=tkinter.NW) 
c1 =CTkComboBox(root,values=['Male',"Female","other"],width=120,border_color='cyan',corner_radius=20).place(x=450,y=170,anchor=tkinter.NW)
lb1 = CTkLabel(root,text="Email Id:",text_color='cyan',font=('arial black',14,'bold')).place(x=580,y=170,anchor=tkinter.NW)
eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=680,y=170,anchor=tkinter.NW) 
lb1 = CTkLabel(root,text="Contact:",text_color='cyan',font=('arial black',14,'bold')).place(x=150,y=240,anchor=tkinter.NW)
eb1=CTkEntry(root,textvariable='',font=('arial black',12,'bold'),width=200,border_color=r'#00BEFF').place(x=250,y=240,anchor=tkinter.NW) 
lb1 = CTkLabel(root,text="Address:",text_color='cyan',font=('arial black',14,'bold')).place(x=480,y=240,anchor=tkinter.NW)
eb1=CTkTextbox(root,font=('arial black',12,'bold'),text_color='black',width=230,height=60,fg_color='white',border_width=3,border_color=r'white').place(x=580,y=240,anchor=tkinter.NW) 

bt1 = CTkButton(root,text="Add Data",fg_color="cyan",text_color='black',width=140,height=20,hover_color="#00FF00",corner_radius=20,border_color='white',border_width=2,font=('arial black',16,'bold')).place(x=120,y=350,anchor=tkinter.NW)
bt1 = CTkButton(root,text="Update Data",fg_color="cyan",text_color='black',width=140,height=20,hover_color="#00FF00",corner_radius=20,border_color='white',border_width=2,font=('arial black',16,'bold')).place(x=320,y=350,anchor=tkinter.NW)
bt1 = CTkButton(root,text="Remove Data",fg_color="cyan",text_color='black',width=140,height=20,hover_color="#00FF00",corner_radius=20,border_color='white',border_width=2,font=('arial black',16,'bold')).place(x=520,y=350,anchor=tkinter.NW)
bt1 = CTkButton(root,text="Clear Data",fg_color="cyan",text_color='black',width=140,height=20,hover_color="#00FF00",corner_radius=20,border_color='white',border_width=2,font=('arial black',16,'bold')).place(x=720,y=350,anchor=tkinter.NW)

tfrm= CTkScrollableFrame(master=root,width=1070,height=200,fg_color=r'#FFFDD0')
tfrm.place(x=0,y=400,anchor=tkinter.NW)

st = ttk.Style()
st.configure("myst.Treeview",font =('calibri',10,'bold'),rowheight=40)
tree = ttk.Treeview(tfrm,columns=(1,2,3,4,5,6,7,8),style="myst.Treeview")
tree.heading('1',text='EmpID')
tree.column('1',width=100)
tree.heading('2',text='Emp NAME')
tree.heading('3',text='AGE')
tree.column('3',width=70)
tree.heading('4',text='D O J')
tree.column('4',width=60)
tree.heading('5',text='Gender')
tree.column('5',width=90)
tree.heading('6',text='Email')
tree.heading('7',text='Contace')
tree.heading('8',text='Address')
tree['show']= 'headings'
tree.pack(side = 'left',fill='y')


root.mainloop()