import tkinter as tk
expression = ''
#function binding text
def press(num):
    global expression
    expression = expression + str(num) 
    v.set(str(expression))

def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        v.set(total) 
        expression = "" 
    except: 
        v.set(" error ") 
        expression = "" 

#function clear
def clear(): 
    global expression 
    expression = "" 
    v.set("") 

    
frm = tk.Tk()
frm.geometry("245x300")
frm.title('Calculator')
frm.configure(background='#34495e')

lbl =tk.Label(frm, text = '>')
lbl.place(x = 10,y = 10,width=60,height=40)


v = tk.StringVar()
txt = tk.Entry(frm,justify='right',textvariable=v)
txt.place(x = 60,y = 10,width=175,height=40)

btn7 = tk.Button(frm,text = '7', command=lambda: press(7), cursor="hand2")
btn7.place(x = 10,y = 60,width=40,height=40)
btn4 = tk.Button(frm,text = '4', command=lambda: press(4), cursor="hand2")
btn4.place(x = 10,y = 105,width=40,height=40)
btn1 = tk.Button(frm,text = '1', command=lambda: press(1), cursor="hand2")
btn1.place(x = 10,y = 150,width=40,height=40)
btndot = tk.Button(frm,text = '.', command=lambda: press("."), cursor="hand2")
btndot.place(x = 10,y = 195,width=40,height=40)

btn8 = tk.Button(frm,text = '8', command=lambda: press(8), cursor="hand2")
btn8.place(x = 55,y = 60,width=40,height=40)
btn5 = tk.Button(frm,text = '5', command=lambda: press(5), cursor="hand2")
btn5.place(x = 55,y = 105,width=40,height=40)
btn2 = tk.Button(frm,text = '2', command=lambda: press(2), cursor="hand2")
btn2.place(x = 55,y = 150,width=40,height=40)
btnzero = tk.Button(frm,text = '0', command=lambda: press(0), cursor="hand2")
btnzero.place(x = 55,y = 195,width=85,height=40)

btn9 = tk.Button(frm,text = '9', command=lambda: press(9), cursor="hand2")
btn9.place(x = 100,y = 60,width=40,height=40)
btn6 = tk.Button(frm,text = '6', command=lambda: press(6), cursor="hand2")
btn6.place(x = 100,y = 105,width=40,height=40)
btn3 = tk.Button(frm,text = '3', command=lambda: press(3), cursor="hand2")
btn3.place(x = 100,y = 150,width=40,height=40)

time = tk.Button(frm,text = '*', bg='#f39c12',fg='#fff',command=lambda: press("*"))
time.place(x = 150,y = 60,width=40,height=40)
similar = tk.Button(frm,text = '/', bg='#f39c12',fg='#fff',command=lambda: press("/"))
similar.place(x = 150,y = 105,width=40,height=40)

percent = tk.Button(frm,text = '%', bg='#f39c12',fg='#fff',command=lambda: press("%"))
percent.place(x = 150,y = 150,width=40,height=40)
minit = tk.Button(frm,text = '-', bg='#f39c12',fg='#fff',command=lambda: press("+"))
minit.place(x = 195,y = 150,width=40,height=40)

sqroot = tk.Button(frm,text = 'R', bg='#f39c12',fg='#fff',command=lambda: press("+"))
sqroot.place(x = 150,y = 195,width=40,height=40)
pam = tk.Button(frm,text = '+/-', bg='#f39c12',fg='#fff',command=lambda: press(""))
pam.place(x = 195,y = 195,width=40,height=40)




plussy = tk.Button(frm,text = '+', bg='#e67e22',fg='#fff',command=lambda: press("+"))
plussy.place(x = 195,y = 60 ,width=40,height=85)



entereq = tk.Button(frm,text = '=', bg='#16a085',fg='#fff',command=equalpress)
entereq.place(x = 160,y = 245,width=75,height=40)


sqroot = tk.Button(frm,text = '(', bg='#f39c12',fg='#fff',command=lambda: press("("))
sqroot.place(x = 10,y = 245,width=40,height=40)


pam = tk.Button(frm,text = ')', bg='#f39c12',fg='#fff',command=lambda: press(")"))
pam.place(x = 55,y = 245,width=40,height=40)



btnclear = tk.Button(frm,text = 'C' ,bg='#e74c3c',fg='#fff',command=clear)
btnclear.place(x = 100,y = 245,width=55,height=40)


frm.mainloop()