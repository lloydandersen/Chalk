import tkinter as tk
from tkinter import ttk
import chalk


root = tk.Tk()
root.title("Board")
menubar = tk.Menu(root)
file_name_var = tk.StringVar()


def new_file():
    file = open(f"{file_name_var.get()}.carb", "w")
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
    chalk.run("ddd.carb")


def add_lesson_text():
    write_box.insert(tk.END, "L[]\n")


def add_question_text():
    write_box.insert(tk.END, "Q[]\n")


def add_answer_text():
    write_box.insert(tk.END, "A[]\n")


def add_correct_text():
    write_box.insert(tk.END, "C[]\n")


filemenu = tk.Menu(menubar, tearoff=0)
runmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=filemenu, label="File")
filemenu.add_command(label="Save", command=create_new_file)
filemenu.add_command(label="Open", command=open_file)
menubar.add_cascade(menu=runmenu, label="Run")
runmenu.add_command(label="Run", command=run_program)

root.config(menu=menubar)

write_box = tk.Text(root)
write_box.grid(row=0, column=1)


run_box = tk.Text(root)
run_box.grid(row=1, column=1)

cheat_frame = tk.Frame(root)
cheat_frame.grid(row=0, column=0, rowspan=2, sticky="swen")

cheat_frame_title = tk.Label(cheat_frame, text="Commands", font=("roboto", 16))
cheat_frame_title.grid(row=0, column=0)

add_lesson_button = ttk.Button(cheat_frame, text="Lesson", command=add_lesson_text)
add_lesson_button.grid(row=1, column=0)

add_question_button = ttk.Button(cheat_frame, text="Question", command=add_question_text)
add_question_button.grid(row=2, column=0)

add_answer_button = ttk.Button(cheat_frame, text="Answer", command=add_answer_text)
add_answer_button.grid(row=3, column=0)

add_correct_button = ttk.Button(cheat_frame, text="Correct", command=add_correct_text)
add_correct_button.grid(row=4, column=0)

root.mainloop()
