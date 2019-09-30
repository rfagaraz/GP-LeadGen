#! Python3
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter.ttk import *
from os import path

window = Tk()

window.title("GUI Project")
window.geometry('525x300')

lbl = Label(window, text="HACKERBOT v4.20")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "Well, you clicked it." + txt.get()
    lbl.configure(text=res)

txt.focus()

stxt = scrolledtext.ScrolledText(window,width=20,height=10)


combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Garrosh did nothing wrong")
combo.current(0) #set the selected item
combo.grid(column=0, row=1)


chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state.set(1) #check
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=3)

selected = IntVar()

rad1 = Radiobutton(window, text='Terran', value=1, variable=selected)
rad2 = Radiobutton(window, text='Zerg', value=2, variable=selected)
rad3 = Radiobutton(window, text='Protoss', value=3, variable=selected)

def clicked():
    messagebox.showinfo('Seriously?', 'I can\'t believe you clicked')
    filedialog.askdirectory()
#    print(selected.get())
#    stxt.insert(INSERT, selected.get())

btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=2, row=4)
rad2.grid(column=3, row=4)
rad3.grid(column=4, row=4)
stxt.grid(column=0, row=5)
btn.grid(column=2, row=0)

style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", background='green')

bar = Progressbar(window, length=200, style='green.Horizontal.TProgressbar')
bar.grid(column=0, row=6)




bar['value'] = 0
res = messagebox.askquestion('Question', 'Press CANCEL to stop the popups, YES or NO to continue')
bar['value'] = 20
res = messagebox.askyesno('YES or NO', 'Calculate 2+2 to confirm you\'re not a bot')
bar['value'] = 40
res = messagebox.askyesnocancel('Yes or NO or CANCEL', 'How many fingers am I holding?')
bar['value'] = 60
res = messagebox.askokcancel('OK CANCEL', 'It\'s a simples YES or NO question!')
bar['value'] = 80
res = messagebox.askretrycancel('RETRY CANCEL', 'Fine, just press OK and we\'ll be done with the pop-ups.')
bar['value'] = 100





window.mainloop()

