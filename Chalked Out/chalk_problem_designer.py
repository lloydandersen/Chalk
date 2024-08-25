import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Chalk Problem Designer")
root.configure(background="#222222")
carb_file_name = tk.StringVar()
parsed_carb_list = []
problem_number = 0


class ChalkLesson:
    def __init__(self):
        pass

    def create_chalk_problems(self):
        pass


class ChalkProblem:
    def __init__(self, question, equation, variables, answers, description, hints):
        self.question = question
        self.equation = equation
        self.variables = variables
        self.answers = answers
        self.description = description
        self.hints = hints


def create_new_carbon_file():
    file = open(f"{carb_file_name.get()}.carb", 'w')
    file.close()


def open_carbon_file():
    file = open(f"{carb_file_name.get()}.carb", "r")
    print(1)
    file.close()


def save_carbon_file():
    file = open(f"{carb_file_name.get()}.carb", "w")
    file.close()


def load_next_problem():
    pass


def create_file_name_dialog():
    pop_box = tk.Toplevel(root)
    file_name_label = tk.Label(pop_box, text="File Name")
    file_name_label.grid(row=0, column=0)
    file_name_entry = tk.Entry(pop_box, textvariable=carb_file_name)
    file_name_entry.grid(row=0, column=1)

    create_carb_file_button = tk.Button(pop_box, text="Create", command=create_new_carbon_file)
    create_carb_file_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def open_file_name_dialog():
    pop_box = tk.Toplevel(root)
    file_name_label = tk.Label(pop_box, text="File Name")
    file_name_label.grid(row=0, column=0)
    file_name_entry = tk.Entry(pop_box, textvariable=carb_file_name)
    file_name_entry.grid(row=0, column=1)

    open_carb_file_button = tk.Button(pop_box, text="Open", command=open_carbon_file)
    open_carb_file_button.grid(row=1, column=0, columnspan=2, sticky="swen")


home_page_frame = tk.Frame(root, background="#222222")
home_page_frame.pack(fill="both", side="top", padx=60, pady=60)


create_carb_button = tk.Button(home_page_frame, text="Create", command=create_file_name_dialog)
create_carb_button.grid(row=0, column=0, ipadx=30, ipady=5, sticky="swen")

open_carb_button = tk.Button(home_page_frame, text="Open", command=open_file_name_dialog)
open_carb_button.grid(row=1, column=0, ipadx=30, ipady=5, sticky="swen")


problem_page_frame = tk.Frame(root, background="#222222")
# problem_page_frame.pack(fill="both", side="top", padx=20, pady=20)

problem_label = tk.Label(problem_page_frame, text="Problem", background="#222222", foreground="white")
problem_label.grid(row=0, column=0)

problem_box = tk.Text(problem_page_frame, background="#222222", foreground="white", width=30, height=4)
problem_box.grid(row=0, column=1, columnspan=2, sticky="swen", ipadx=10, ipady=10)
problem_box.insert(tk.END, 'What is [test1] + [test50]?')
problem_box.configure(font=("Times New Roman", 30))
problem_box.configure(insertbackground="white")

equation_label = tk.Label(problem_page_frame, text="Equation", background="#222222", foreground="white")
equation_label.grid(row=1, column=0)


# correct is special word.
equation_box = tk.Text(problem_page_frame, background="#222222", foreground="white", width=30, height=1)
equation_box.grid(row=1, column=1, columnspan=2, sticky="swen", ipadx=10, ipady=10)
equation_box.insert(tk.END, 'test1  + test50 = correct')
equation_box.configure(font=("Times New Roman", 30))
equation_box.configure(insertbackground="white")

variables_label = tk.Label(problem_page_frame, text="Variables", background="#222222", foreground="white")
variables_label.grid(row=2, column=0)


variables_box = tk.Text(problem_page_frame, background="#222222", foreground="white", width=30, height=4)
variables_box.grid(row=2, column=1, columnspan=2, sticky="swen", ipadx=10, ipady=10)
variables_box.insert(tk.END, 'test1: int, [0, 50]\ntest50: int, [0, 50]')
variables_box.configure(font=("Times New Roman", 30))
variables_box.configure(insertbackground="white")


next_problem_button = tk.Button(problem_page_frame, text="Next")
next_problem_button.grid(row=3, column=1, ipadx=30, ipady=5, sticky='w')

back_problem_button = tk.Button(problem_page_frame, text="Back")
back_problem_button.grid(row=3, column=0, ipadx=30, ipady=5)

save_problem_button = tk.Button(problem_page_frame, text="Save")
save_problem_button.grid(row=3, column=2, ipadx=30, ipady=5, sticky="e")


root.mainloop()
