from tkinter import *
from tkinter import messagebox
from math import *
scr=Tk(className="calculator")
e=Entry(scr,width=22,font=("consolas",20),bg="steel blue")
e.grid(row=1,column=0,columnspan=5)
l=Label(scr,width=22,font=("consolas",20),anchor="e",text="SCINTIFIC")
l.grid(row=0,column=0,columnspan=5)

Π=pi
class Etr:
    def __init__(self,func):
        self.fun = func
        
    def __call__(self,x=1):
        self.s = self.fun(x)
        if self.s is None:
            return
        l.config(text=e.get())
        e.delete(0,e.index(100000))
        e.insert(0,str(self.s))

def absolute(x):
    return(abs(float(e.get())))
@Etr
def pw(n):
    x=float(e.get())
    return(x**n)

@Etr
def fact(x):
    return(factorial(int(e.get())))
@Etr
def logrithm(x):
    return(log(float(e.get()),10))
 
@Etr
def eq(x):
    try:
        return(eval(e.get()))
    except :
        messagebox.showinfo("Error","Please provide correct expression")

def fun(y):
    e.insert(END,y)
  
b= Button(scr,width=8,height=2,relief="ridge",text="x²",command=lambda :pw(2))
b.grid(row=2,column=0)
b1=Button(scr,width=8,height=2,relief="ridge",text="x³",command=lambda :pw(3))
b1.grid(row=2,column=1)
b2=Button(scr,width=8,height=2,relief="ridge",text="Del",command=lambda :e.delete(len(e.get())-1))
b2.grid(row=2,column=3)
b3=Button(scr,width=8,height=2,relief="ridge",text="AC",command=lambda :e.delete(0,e.index(1000000)))
b3.grid(row=2,column=4)
b4=Button(scr,width=8,height=2,relief="ridge",text="log",command=logrithm)
b4.grid(row=2,column=2)

b5=Button(scr,width=8,height=2,relief="ridge",text="²√",command=lambda :pw(1/2))
b5.grid(row=3,column=0)
b6=Button(scr,width=8,height=2,relief="ridge",text="³√",command=lambda :pw(1/3))
b6.grid(row=3,column=1)
b7=Button(scr,width=8,height=2,relief="ridge",text="sin",command=lambda :fun("sin("))
b7.grid(row=3,column=2)
b8=Button(scr,width=8,height=2,relief="ridge",text="x",command=lambda :fun("*"))
b8.grid(row=3,column=3)
b9=Button(scr,width=8,height=2,relief="ridge",text="/",command=lambda :fun("/"))
b9.grid(row=3,column=4)

b10=Button(scr,width=8,height=2,relief="ridge",text="Π",command=lambda :fun("Π"))
b10.grid(row=4,column=0)
b11=Button(scr,width=8,height=2,relief="ridge",text="tan",command=lambda :fun("tan("))
b11.grid(row=4,column=1)
b12=Button(scr,width=8,height=2,relief="ridge",text="cos",command=lambda :fun("cos("))
b12.grid(row=4,column=2)
b13=Button(scr,width=8,height=2,relief="ridge",text="+",command=lambda :fun("+"))
b13.grid(row=4,column=3)
b14=Button(scr,width=8,height=2,relief="ridge",text="-",command=lambda :fun("-"))
b14.grid(row=4,column=4)

b15=Button(scr,width=8,height=2,relief="ridge",text="(",command=lambda :fun("("))
b15.grid(row=5,column=0)
b16=Button(scr,width=8,height=2,relief="ridge",text=")",command=lambda :fun(")"))
b16.grid(row=5,column=1)
b17=Button(scr,width=8,height=2,relief="ridge",text="9",font=("consolas bold",10),bg="light blue",command=lambda :fun("9"))
b17.grid(row=5,column=2)
b18=Button(scr,width=8,height=2,relief="ridge",text="8",font=("consolas bold",10),bg="light blue",command=lambda :fun("8"))
b18.grid(row=5,column=3)
b19=Button(scr,width=8,height=2,relief="ridge",text="7",font=("consolas bold",10),bg="light blue",command=lambda :fun("9"))
b19.grid(row=5,column=4)

b20=Button(scr,width=8,height=2,relief="ridge",text="nPr",command=lambda :fun("c"))
b20.grid(row=6,column=0)
b21=Button(scr,width=8,height=2,relief="ridge",text="nCr",command=lambda :fun(" "))
b21.grid(row=6,column=1)
b22=Button(scr,width=8,height=2,relief="ridge",text="6",font=("consolas bold",10),bg="light blue",command=lambda :fun("6"))
b22.grid(row=6,column=2)
b23=Button(scr,width=8,height=2,relief="ridge",text="5",font=("consolas bold",10),bg="light blue",command=lambda :fun("7"))
b23.grid(row=6,column=3)
b24=Button(scr,width=8,height=2,relief="ridge",text="4",font=("consolas bold",10),bg="light blue",command=lambda :fun("4"))
b24.grid(row=6,column=4)

b25=Button(scr,width=8,height=2,relief="ridge",text="abs",command=absolute)
b25.grid(row=7,column=0)
b26=Button(scr,width=8,height=2,relief="ridge",text="n!",command=fact)
b26.grid(row=7,column=1)
b27=Button(scr,width=8,height=2,relief="ridge",text="3",font=("consolas bold",10),bg="light blue",command=lambda :fun("3"))
b27.grid(row=7,column=2)
b28=Button(scr,width=8,height=2,relief="ridge",text="2",font=("consolas bold",10),bg="light blue",command=lambda :fun("2"))
b28.grid(row=7,column=3)
b29=Button(scr,width=8,height=2,relief="ridge",text="1",font=("consolas bold",10),bg="light blue",command=lambda :fun("1"))
b29.grid(row=7,column=4)

b30=Button(scr,width=8,height=2,relief="ridge",text=".",command=lambda :fun("."))
b30.grid(row=8,column=0)
b31=Button(scr,width=8,height=2,relief="ridge",text="%",command=lambda :fun("%"))
b31.grid(row=8,column=1)
b32=Button(scr,width=8,height=2,relief="ridge",text="0",font=("consolas bold",10),bg="light blue",command=lambda :fun("0"))
b32.grid(row=8,column=2)
b33=Button(scr,width=18,height=2,text="=",command=eq)
b33.grid(row=8,column=3,columnspan=2)

scr.mainloop()
