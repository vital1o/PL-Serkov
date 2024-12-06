import requests
from pprint import pprint
from tkinter import *
from tkinter.filedialog import askopenfile

def inf():
    global entr
    url = f"https://api.github.com/users/{entr.get()}"
    user_data = requests.get(url).json()
    print(user_data)

    f = askopenfile("w")
    f.write(str(user_data))


window = Tk()
window.title("Серков Виталий Дмитриевич")
window.geometry("400x100")

entr=IntVar()
entr = Entry(window, width=30)
entr.grid(column=0,row=0)
btn = Button(window, text='получить информацию', command=inf)
btn.grid(column=1,row=0)


window.mainloop()