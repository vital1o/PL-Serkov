from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile

#функция для 1 вкладки
def calculate():
    global btn
    global lbl
    result = 0
    if combo1.get() == '+':
        result = txt1int.get() + txtint.get()
    if combo1.get() == '-':
        result = txtint.get() - txt1int.get()
    if combo1.get() == '/':
        result = txtint.get() / txt1int.get()
    if combo1.get() == '*':
        result = txtint.get() * txt1int.get()
    lbl['text'] = str(result)

#функция для 2 вкладки
def checkbutton_changed():
    if enabled1.get() == 1:
        showinfo(title="Info", message="Вы выбрали вариант 1")
    if enabled2.get() == 1:
        showinfo(title="Info", message="Вы выбрали вариант 2")
    if enabled3.get() == 1:
        showinfo(title="Info", message="Вы выбрали вариант 3")

#функция для 3 вкладки
def OpenFile():
    f = askopenfile()
    result1 = f.readlines()
    lbl3['text']=str(result1)

#создание окна
window = Tk()
window.title("Серков Виталий Дмитриевич")
window.geometry("400x250")
tab_control = ttk.Notebook(window)

#создание 1 вкладки
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.pack(expand=1, fill='both')

#задание с калькулятором
txtint = IntVar()
txt = Entry(tab1, width=5, textvariable=txtint)
txt.grid(column=0, row=0)
combo1 = Combobox(tab1, width=2)
combo1['values'] = ('+', '-', '*', '/')
combo1.current(0)
combo1.grid(column=1, row=0)
txt1int = IntVar()
txt1 = Entry(tab1, width=5, textvariable=txt1int)
txt1.grid(column=2, row=0)
btn = Button(tab1, text='=', command=calculate)
btn.grid(column=3, row=0)
lbl = Label(tab1, text='result')
lbl.grid(column=4, row=0)

#создание 2 вкладки
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Вторая")
tab_control.pack(expand=1, fill='both')

#задание с чекбоксами
enabled1 = IntVar()
enabled2 = IntVar()
enabled3 = IntVar()
check1 = Checkbutton(tab2, text="Первый", variable=enabled1)
check2 = Checkbutton(tab2, text="Второй", variable=enabled2)
check3 = Checkbutton(tab2, text="Третий", variable=enabled3)
btn1 = Button(tab2, text='Тык!', command=checkbutton_changed)
check1.grid(column=0, row=0)
check2.grid(column=1, row=0)
check3.grid(column=2, row=0)
btn1.grid(column=3, row=0)

#создание 3 вкладки
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Третий")
tab_control.pack(expand=1, fill='both')

#задание с импортом файла
file = Button(tab3, text='Файл', command=OpenFile)
file.grid(column=0, row=0)
lbl3 = Label(tab3, text='result')
lbl3.grid(column=0,row=1)


window.mainloop()