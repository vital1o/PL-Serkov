
import requests
import json
import tkinter as tk
from tkinter import Entry, Button, scrolledtext, messagebox
from tkinter import filedialog

def get_user_info():
    username = us_entry.get()
    repo_name = repo_entry.get()

   
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    response.raise_for_status()
    user_data = response.json()

    info = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),
        }

    username_entry.delete(1.0, tk.END)
    username_entry.insert(1.0, f'{info}')



def save_file():
    username = us_entry.get()
    repo_name = repo_entry.get()
    if username == 'ionic-team' and repo_name=='ionic-framework':
        url = f"https://api.github.com/repos/ionic-team/ionic-framework"
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()
        info = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(info, f, indent=4)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
    else:
        username_entry.delete(1.0, tk.END)
        username_entry.insert(1.0, 'нечего сохронять')


root = tk.Tk()
root.title('Серков Виталий Дмитриевич')
root.geometry('600x400')
root.resizable(height=False, width=False)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=1, sticky=tk.W)
us_entry = Entry(root,width=30)
us_entry.grid(row=1,column=2,sticky=tk.W)


username_label = tk.Label(root, text="Repositories:")
username_label.grid(row=2, column=1, sticky=tk.W)
repo_entry = Entry(root,width=30)
repo_entry.grid(row=2,column=2,sticky=tk.W)

username_entry = tk.Text(root, width=40, height=15)
username_entry.grid(row=3, column=2)

get_button = tk.Button(root, text="Получить информацию", command=get_user_info)
get_button.grid(row=4, column=2)

save_btn = tk.Button(root,text="Сохранить", command=save_file)
save_btn.grid(row=5,column=2)

root.mainloop()
