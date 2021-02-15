import tkinter as tk
def print_something():
    v = text_box.get("1.0", "end-1c")
    m = v.split()
    cUnit = [
            ['inc','cm','*2.54'],
            ['inc','ft','/12'],
            ['cm','inc','/12'],
            ['cm','ft','*12'],
            ['ft','inc','*30.84'],
            ['py','cy','+543'],
            ['py','cy','-543'],
            ]
    try:
        for s in cUnit:
            if (m[1] == s[0] and m[3] == s[1]):
                revert = eval(m[0]+s[2])   
        label.config(text=revert)   
    except:
        try: 
            total = str(eval(v)) 
            label.config(text=total)
        except:
            label.config(text=m)

root = tk.Tk()
root.geometry("245x300")
root.title('Google')
root.configure(background='#34495e')

btn = tk.Button(root, text="Search", command=print_something)
btn.place(x = 10,y = 60,width=40,height=40)

text_box = tk.Text(root, height=4, width=300)
text_box.pack()

label = tk.Label(root)
label.pack()
root.mainloop()