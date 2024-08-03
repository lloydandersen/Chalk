import tkinter as tk
from tkinter import ttk
import chalk


root = tk.Tk()
root.title("Board")
menubar = tk.Menu(root)
file_name_var = tk.StringVar()


def new_file():
    file = open(f"{file_name_var.get()}.txt", "w")
    contents = write_box.get(1., "end-1c")
    file.write(contents)
    file.close()
    count = 0
    for child in root.winfo_children():
        if count == 3:
            child.destroy()
        else:
            count += 1


def create_new_file():
    top = tk.Toplevel(root)
    file_name_label = tk.Label(top, text="Enter File Name")
    file_name_label.grid(row=0, column=0)

    file_name_entry = tk.Entry(top, textvariable=file_name_var)
    file_name_entry.grid(row=0, column=1)

    file_name_create = tk.Button(top, text="Create", command=new_file)
    file_name_create.grid(row=1, column=0, columnspan=2)


def open_file():
    pass


def run_program():
    chalk.run("Lloyds.txt")


filemenu = tk.Menu(menubar, tearoff=0)
runmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=filemenu, label="File")
filemenu.add_command(label="New", command=create_new_file)
filemenu.add_command(label="Open", command=open_file)
menubar.add_cascade(menu=runmenu, label="Run")
runmenu.add_command(label="Run", command=run_program)

root.config(menu=menubar)

write_box = tk.Text(root)
write_box.grid(row=0, column=0)


run_box = tk.Text(root)
run_box.grid(row=1, column=0)
root.mainloop()
