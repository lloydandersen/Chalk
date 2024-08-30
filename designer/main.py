import tkinter as tk
from tkinter import ttk
import re
from tkinter.filedialog import FileDialog

root = tk.Tk()
root.title("Designer")
app_font = ("Times New Roman", 16)
app_background_color = "white"
app_theme_color = "#E6ECF5"
app_foreground_color = "black"
app_alternative_foreground_color = "black"
root.configure(background=app_theme_color)
app_entry_box_width = 40
app_label_box_x_spacing = (0, 5)
app_entry_box_x_spacing = (0, 2)
values_list = []
app_label_box_y_spacing = (5, 0)
app_entry_box_y_spacing = (5, 0)


lesson_name_var = tk.StringVar()
question_var = tk.StringVar()
equation_var = tk.StringVar()
answer_1_var = tk.StringVar()
answer_2_var = tk.StringVar()
answer_3_var = tk.StringVar()
answer_4_var = tk.StringVar()
variables_var = tk.StringVar()
hint_var = tk.StringVar()
media_var = tk.StringVar()

problem_name_var = tk.StringVar()
problem_count_var = tk.IntVar()
current_problem_iid_var = tk.StringVar()
file_name_var = tk.StringVar()
problem_count_var.set(-1)

# test setup
lesson_name_var.set("Problem Set 1")
problem_name_var.set("")

def rename_lesson():
    top = tk.Toplevel(root)
    rename_label = tk.Label(top, text="Rename Lesson")
    rename_label.pack()

    rename_entry = tk.Entry(top, textvariable=lesson_name_var)
    rename_entry.pack()

    rename_button = tk.Button(top, text="Rename", command=lambda: top.destroy())
    rename_button.pack()


main_page = tk.Frame(root, background=app_background_color)
main_page.pack(side="top", fill="both", padx=3, pady=3, ipadx=10, ipady=10)

title_frame = tk.Frame(main_page, background=app_background_color)
title_frame.grid(row=0, column=0, columnspan=3, pady=(0, 5), sticky="w")

save_frame = tk.Frame(main_page, background=app_background_color)
save_frame.grid(row=0, column=0, columnspan=3, pady=(0, 5), sticky="e")

lesson_name_label = tk.Label(title_frame, font=app_font, textvariable=lesson_name_var, background=app_background_color,
                             foreground=app_foreground_color)
lesson_name_label.grid(row=0, column=0, ipadx=10, ipady=10, padx=(0, 5))
lesson_name_label.bind("<Button-3>", lambda e: rename_lesson())

problem_name_label = tk.Label(title_frame, font=app_font, textvariable=problem_name_var, background=app_background_color,
                              foreground=app_foreground_color)
problem_name_label.grid(row=0, column=1, ipadx=10, ipady=10, padx=(0, 5))


problem_tree = ttk.Treeview(main_page)
problem_tree.grid(row=1, column=2, rowspan=9, sticky="swen")
problem_tree.heading("#0", text="Problems")

question_label = tk.Label(main_page, text="Question", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
question_label.grid(row=1, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

question_entry = tk.Entry(main_page, textvariable=question_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
question_entry.grid(row=1, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


equation_label = tk.Label(main_page, text="Equation", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
equation_label.grid(row=2, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

equation_entry = tk.Entry(main_page, textvariable=equation_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
equation_entry.grid(row=2, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


answer_1_label = tk.Label(main_page, text="Answer 1", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
answer_1_label.grid(row=3, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

answer_1_entry = tk.Entry(main_page, textvariable=answer_1_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
answer_1_entry.grid(row=3, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


answer_2_label = tk.Label(main_page, text="Answer 2", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
answer_2_label.grid(row=4, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

answer_2_entry = tk.Entry(main_page, textvariable=answer_2_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
answer_2_entry.grid(row=4, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


answer_3_label = tk.Label(main_page, text="Answer 3", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
answer_3_label.grid(row=5, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

answer_3_entry = tk.Entry(main_page, textvariable=answer_3_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
answer_3_entry.grid(row=5, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


answer_4_label = tk.Label(main_page, text="Answer 4", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
answer_4_label.grid(row=6, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

answer_4_entry = tk.Entry(main_page, textvariable=answer_4_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
answer_4_entry.grid(row=6, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


variables_label = tk.Label(main_page, text="Variables", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
variables_label.grid(row=7, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

variables_entry = tk.Entry(main_page, textvariable=variables_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
variables_entry.grid(row=7, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


hint_label = tk.Label(main_page, text="Hint", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
hint_label.grid(row=8, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

hint_entry = tk.Entry(main_page, textvariable=hint_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
hint_entry.grid(row=8, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)


media_label = tk.Label(main_page, text="Media", font=app_font, background=app_background_color,
                          foreground=app_foreground_color)
media_label.grid(row=9, column=0, padx=app_label_box_x_spacing, pady=app_label_box_y_spacing)

media_entry = tk.Entry(main_page, textvariable=media_var, font=app_font, background=app_theme_color,
                          foreground=app_alternative_foreground_color, width=app_entry_box_width)
media_entry.grid(row=9, column=1, padx=app_entry_box_x_spacing, pady=app_entry_box_y_spacing)

def add_new_problem():
    new_number = problem_count_var.get()
    new_number += 1
    problem_count_var.set(new_number)
    value_list = ["", "", "", "", "", "", "", "", ""]
    problem_tree.insert("", tk.END, text=f"problem_{problem_count_var.get()}", values=value_list)


def delete_problem():
    item_handle = problem_tree.selection()[0]
    item_selected = problem_tree.delete(item_handle)

def clear_all_entries():
    question_var.set("")
    equation_var.set("")
    answer_1_var.set("")
    answer_2_var.set("")
    answer_3_var.set("")
    answer_4_var.set("")
    variables_var.set("")
    hint_var.set("")
    media_var.set("")


def duplicate_problem():
    new_number = problem_count_var.get()
    new_number += 1
    problem_count_var.set(new_number)
    item_handle = problem_tree.selection()[0]
    item_selected = problem_tree.item(item_handle)
    problem_tree.insert("", tk.END, text=f"problem_{problem_count_var.get()}", values=item_selected['values'])




control_frame = tk.Frame(main_page, background=app_background_color)
control_frame.grid(row=10, column=2, sticky="e", pady=(5, 5))

duplicate_button = tk.Button(control_frame, text="Duplicate", font=app_font, background=app_background_color, foreground=app_foreground_color, command=duplicate_problem)
duplicate_button.grid(row=0, column=1)

add_button = tk.Button(control_frame, text="Add", font=app_font, background=app_background_color, foreground=app_foreground_color, command=add_new_problem)
add_button.grid(row=0, column=0)

delete_button = tk.Button(control_frame, text="Delete", font=app_font, background=app_background_color, foreground=app_foreground_color, command=delete_problem)
delete_button.grid(row=0, column=2)


clear_frame = tk.Frame(main_page, background=app_background_color)
clear_frame.grid(row=10, column=1, sticky="n", pady=(5, 5))

clear_button = tk.Button(clear_frame, text="Clear", font=app_font, background=app_background_color, foreground=app_foreground_color)
clear_button.grid(row=0, column=1)
clear_button.bind("<Double-1>", lambda e: clear_all_entries())






def save_problem_to_tree(*args):
    try:
        item_handle = current_problem_iid_var.get()

        value_list = [question_var.get(),
                      equation_var.get(),
                      answer_1_var.get(),
                      answer_2_var.get(),
                      answer_3_var.get(),
                      answer_4_var.get(),
                      variables_var.get(),
                      hint_var.get(),
                      media_var.get()]
        problem_tree.item(item_handle, values=value_list)
        root.focus_set()

    except IndexError:
        pass

    except tk.TclError:
        pass


clear_button = tk.Button(clear_frame, text="Update", font=app_font, background=app_background_color, foreground=app_foreground_color, command=save_problem_to_tree)
clear_button.grid(row=0, column=0)

def open_problem_from_tree(*args):
    try:
        item_hand = problem_tree.selection()[0]
        current_problem_iid_var.set(item_hand)

        item_handle = current_problem_iid_var.get()

        problem_name_var.set(problem_tree.item(item_handle)['text'])

        values_list = problem_tree.item(item_handle)['values']

        question_var.set(values_list[0])
        equation_var.set(values_list[1])
        answer_1_var.set(values_list[2])
        answer_2_var.set(values_list[3])
        answer_3_var.set(values_list[4])
        answer_4_var.set(values_list[5])
        variables_var.set(values_list[6])
        hint_var.set(values_list[7])
        media_var.set(values_list[8])
    except IndexError:
        pass



def open_to_tree():
    global values_list
    file_location = tk.filedialog.askopenfilename(filetypes=[('Carbonate Files', '*.carb')])
    open_button.configure(state="disabled")
    file_name_var.set(file_location[:-5])

    iid_count = 0
    values_list = []
    test_bool = True

    handle = open(f"{file_location}", "r")

    for line in handle:
        if line[0] == "L":      # lesson name
            lesson_name = line[2:]
            lesson_name = lesson_name[:-2]
            lesson_name_var.set(lesson_name)

        elif line[0] == "Q":
            values_list.clear()
            question = line[2:]
            question = question[:-2]
            values_list.append(question)
            iid_count += 1
            problem_tree.insert("", tk.END, iid=iid_count, text=f"problem_{iid_count}", values=values_list)


            problem_count_var.set(iid_count)

        elif line[0] == "E":
            equation = line[2:]
            equation = equation[:-2]
            values_list.append(equation)


        elif line[0] == "A":
            answer = line[2:]
            answer = answer[:-2]
            values_list.append(answer)


        elif line[0] == "A":
            answer = line[2:]
            answer = answer[:-2]
            values_list.append(answer)


        elif line[0] == "A":
            answer = line[2:]
            answer = answer[:-2]
            values_list.append(answer)


        elif line[0] == "A":
            answer = line[2:]
            answer = answer[:-2]
            values_list.append(answer)


        elif line[0] == "V":
            variables = line[2:]
            variables = variables[:-2]
            values_list.append(variables)


        elif line[0] == "H":
            hint = line[2:]
            hint = hint[:-2]
            values_list.append(hint)


        elif line[0] == "M":
            media = line[2:]
            media = media[:-2]
            values_list.append(media)

        else:
            try:
                problem_tree.item(iid_count, values=values_list)
            except tk.TclError:
                pass








    handle.close()




def save_to_carb():

    carb_handle = open(f"{file_name_var.get()}.carb", "w")

    lesson_name = lesson_name_var.get()
    carb_handle.write(f"L[{lesson_name}]\n")


    for child in problem_tree.get_children():
        carb_handle.write("\n")
        child_item = problem_tree.item(child)
        carb_handle.write(f"Q[{child_item['values'][0]}]\n")
        carb_handle.write(f"E[{child_item['values'][1]}]\n")
        carb_handle.write(f"A[{child_item['values'][2]}]\n")
        carb_handle.write(f"A[{child_item['values'][3]}]\n")
        carb_handle.write(f"A[{child_item['values'][4]}]\n")
        carb_handle.write(f"A[{child_item['values'][5]}]\n")
        carb_handle.write(f"V[{child_item['values'][6]}]\n")
        carb_handle.write(f"H[{child_item['values'][7]}]\n")
        carb_handle.write(f"M[{child_item['values'][8]}]\n\n")

    carb_handle.close()

    root.destroy()



def save_popup():
    top = tk.Toplevel(root)
    carb_file_name_label = tk.Label(top, text="Carb File Name", font=app_font)
    carb_file_name_label.grid(row=0, column=0, padx=(0, 5))

    carb_file_name_extension_label = tk.Label(top, text=".carb", font=app_font)
    carb_file_name_extension_label.grid(row=0, column=2)

    carb_file_name_entry = tk.Entry(top, textvariable=file_name_var, font=app_font, width=20)
    carb_file_name_entry.grid(row=0, column=1)

    carb_file_name_button = tk.Button(top, text="Save", font=app_font, command=save_to_carb)
    carb_file_name_button.grid(row=1, column=0, columnspan=3, pady=(5, 5))


save_button = tk.Button(save_frame, text="Save", font=app_font, background=app_foreground_color, foreground=app_background_color,width=15, command=save_popup)
save_button.grid(row=0, column=0, padx=(0, 5), sticky="e")

open_button = tk.Button(save_frame, text="Open", font=app_font, background=app_foreground_color, foreground=app_background_color,width=15, command=open_to_tree)
open_button.grid(row=0, column=1, sticky="e")



problem_tree.bind("<Double-1>", lambda e: open_problem_from_tree())
root.bind("<Return>", lambda e: save_problem_to_tree())


root.mainloop()


