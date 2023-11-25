import tkinter as tk
from tkinter import filedialog
from datetime import datetime

from files.pdf_file import PdfFile
from files.text_file import TextFile
from constraints.constraints import extensions


class Manager:
    AVAIBLE_FILE_TYPES = {
        'pdf': PdfFile,
        'txt': TextFile
    }

    @staticmethod
    def create_object(username, company, path: str):
        file_extension = path.split('.')[-1]
        if file_extension in extensions():
            return Manager.AVAIBLE_FILE_TYPES[file_extension](username, company, path)
        return 'The program does not support this extension file!'

    @staticmethod
    def create_billing_info(data_file):
        final_billing_info = f"""Време и дата при извличане на информацията: {datetime.now()}
Здравейте {data_file.username}!
Това е информация относно сумите за плащане на фирма {data_file.company}."""
        final_billing_info += data_file.extract_data()
        return final_billing_info


# a = Manager()
# file_object = a.create_object('doni', 'yettel', r"C:\Users\User\Desktop\1421578.pdf")
# print(a.create_billing_info(file_object))


root = tk.Tk()
root.title('Bills Extractor 2.0')
root.geometry("750x350")


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_var.set(file_path)


def new_window():
    result_window = tk.Toplevel()
    result_window.title("Result")
    result_window.geometry("600x750")
    result_label = tk.Label(result_window, text="RESULTS", font=("Ariel", 20))
    result_label.pack()

    username = username_entry.get()
    company = company_entry.get()
    path_as_str = path_entry.get()

    manager = Manager()
    file_object = manager.create_object(username, company, path_as_str)

    result_text_window = tk.Text(result_window, wrap=tk.WORD, height=30, width=75)
    result_text_window.pack(pady=10)
    result_text_window.delete(1.0, tk.END)
    try:
        result_text_window.insert(tk.END, manager.create_billing_info(file_object))
    except AttributeError:
        result_text_window.insert(tk.END, "There was a problem with the input information, please try again.")


label = tk.Label(root,
                 text="""Hello! This is a program for extracting bill information,
for multiple users from large files!
Please submit a file!""",
                 fg="green",
                 font=("Ariel", 20))
label.pack()

username_label = tk.Label(root, text="Username: ", font=("Ariel", 15))
username_label.pack(side="top")

username_entry = tk.Entry(root, bd=5)
username_entry.pack(side="top")

company_label = tk.Label(root, text="Company: ", font=("Ariel", 15))
company_label.pack(side="top")

company_entry = tk.Entry(root, bd=5)
company_entry.pack(side="top")

path_label = tk.Label(root, text="Path: ", font=("Ariel", 15))
path_label.pack(side="top")

entry_var = tk.StringVar()
path_entry = tk.Entry(root, textvariable=entry_var, bd=5)
path_entry.pack(side="top")

path_select = tk.Button(text="Choose file: ", command=browse_file)
path_select.pack(pady=10)

submit_button = tk.Button(text="Submit", font=("Ariel", 13), command=new_window)
submit_button.pack(side="top")

root.mainloop()
