from tkinter import *
from tkinter.ttk import *
rt=Tk()
rt.geometry("750x250")

l0=Label(rt, text="Caesar Cipher", font=("bold", 30))
l0.place(x=240, y=10)

l1=Label(rt, text="Plain_text", font=(22))
l1.place(x=20, y=100)

l2=Label(rt, text="CaesarCipher_text", font=(22))
l2.place(x=20, y=150)

sc1=StringVar()
sc2=StringVar()

ent1=Entry(rt, font=(22), width=50, textvariable=sc1)
ent1.place(x=170, y=100)

ent2=Entry(rt, font=(22), width=50, textvariable=sc2)
ent2.place(x=170, y=150)

l3=Label(rt, text="Shift", font=(22))
l3.place(x=20,y=200)

shift=()
for i in range(0,26):
    shift+=i,

chk=Combobox(rt, font=(22), width=6)
chk['values']=shift
chk.current(0)
chk.place(x=90, y=200)

def clear1():
    sc1.set("")

btn1=Button(rt, text="Clear", command=clear1())
btn1.place(x=650, y=100)

def clear2():
    sc2.set("")

btn2=Button(rt, text="Clear", command=clear2())
btn2.place(x=650, y=150)

def clearall():
    sc1.set("")
    sc2.set("")

btn3=Button(rt, text="Clear All", command=clearall())
btn3.place(x=250, y=200)

def convert():
    if sc1.get()!="" and sc2.get()=="":
        a=sc1.get()
        b=int(chk.get())
        word=""
        for i in range(0, len(a)):
            if a[i]==" ":
                word+=" "
            else:
                c=a[i]
                d=ord(c)
                e=d+b
                if e>122:
                    f=e-122
                    g=f+64
                    h=chr(g)
                    word+=h
                else:
                    j=chr(e)
                    word+=j
        sc2.set(word)
    elif sc1.get()=="" and sc2.get()!="":
        k=sc2.get()
        l=int(chk.get())
        word2=""
        for m in range(0, len(k)):
            if k[m]==" ":
                word2+=" "
            else:
                n=k[m]
                o=ord(n)
                p=o-l
                if p<97:
                    q=97-p
                    r=123-q
                    s=chr(r)
                    word2+=s
                else:
                    t=chr(p)
                    word2+=t
        sc1.set(word2)


btn=Button(rt, text="Convert", command=convert)
btn.place(x=350, y=200)

rt.mainloop()