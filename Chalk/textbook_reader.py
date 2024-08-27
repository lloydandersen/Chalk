import tkinter as tk
from tkinter.filedialog import FileDialog
from tkinter import ttk
from deep_translator import GoogleTranslator

root = tk.Tk()
root.title("Chalk Reader")
root.configure(background="#222222")

file_name_var = tk.StringVar()
question_var = tk.StringVar()
pdf_location = tk.StringVar()
section_list = []
selected_string = tk.StringVar()
selected_section = tk.StringVar()
types_list = ["Note", "Notecard", "Translate", "Multichoice", "PyScript", "PyCalc"]
from_language = "English"
to_language = "Spanish"


# set up value keys
# values = [type, val_1, val_2, val_3, val_4]
name_var = tk.StringVar()
type_key_var = tk.StringVar()

val_1 = tk.StringVar()
val_2 = tk.StringVar()
val_3 = tk.StringVar()
val_4 = tk.StringVar()
current_iid = tk.StringVar()

# functions

def quick_translate():
    to_translater = val_1.get()
    from_language = val_2.get()
    to_language = val_3.get()
    translated_text = GoogleTranslator(source=from_language, target=to_language).translate(to_translater)
    val_1.set(translated_text)
    print(translated_text)


def open_get_pdf():
    location = tk.filedialog.askopenfilename(title="Select a file", filetypes=(("carbon files", "*.carb"),
                                                                               ("all files", "*.*")))

    pdf_location.set(location)


def print_the_copy(*args):
    try:
        selected_string.set(f"{reading_box.selection_get()}")
        view_tree.insert("", tk.END, text=selected_string.get(), values=["Note", None, None, None, None])
    except tk.TclError:
        pass


def system_translate_settings():
    pass

def edit_special_panel(*args):
    special_edit_frame.focus_set()
    for children in special_edit_frame.winfo_children():
        children.grid_forget()


    if type_key_var.get() == "Multichoice":
        item_answer_label = tk.Label(special_edit_frame, text="Answer", background="white")
        item_answer_label.grid(row=2, column=0, ipady=5, padx=5)

        item_answer_entry = tk.Entry(special_edit_frame, textvariable=val_1, background="white", width=40)
        item_answer_entry.grid(row=2, column=1)

        item_answer_1_label = tk.Label(special_edit_frame, text="Answer", background="white")
        item_answer_1_label.grid(row=3, column=0, ipady=5, padx=5)

        item_answer_1_entry = tk.Entry(special_edit_frame, textvariable=val_2, background="white", width=40)
        item_answer_1_entry.grid(row=3, column=1)


        item_answer_2_label = tk.Label(special_edit_frame, text="Answer", background="white")
        item_answer_2_label.grid(row=4, column=0, ipady=5, padx=5)

        item_answer_2_entry = tk.Entry(special_edit_frame, textvariable=val_3, background="white", width=40)
        item_answer_2_entry.grid(row=4, column=1)

        item_answer_3_label = tk.Label(special_edit_frame, text="Answer", background="white")
        item_answer_3_label.grid(row=5, column=0, ipady=5, padx=5)

        item_answer_3_entry = tk.Entry(special_edit_frame, textvariable=val_4, background="white", width=40)
        item_answer_3_entry.grid(row=5, column=1)


    elif type_key_var.get() == "Translate":

        item_answer_label = tk.Label(special_edit_frame, text="Translation", background="white")
        item_answer_label.grid(row=2, column=0, ipady=5, padx=5)

        item_answer_entry = tk.Entry(special_edit_frame, textvariable=val_1, background="white", width=40)
        item_answer_entry.grid(row=2, column=1)

        item_langauge_label = tk.Label(special_edit_frame, text="Language From", background="white")
        item_langauge_label.grid(row=3, column=0, ipady=5, padx=5)

        item_langauge_entry = tk.Entry(special_edit_frame, textvariable=val_2, background="white", width=40)
        item_langauge_entry.grid(row=3, column=1)

        item_langauge_label = tk.Label(special_edit_frame, text="Language To", background="white")
        item_langauge_label.grid(row=4, column=0, ipady=5, padx=5)

        item_langauge_entry = tk.Entry(special_edit_frame, textvariable=val_3, background="white", width=40)
        item_langauge_entry.grid(row=4, column=1)

        item_note_label = tk.Label(special_edit_frame, text="Note", background="white")
        item_note_label.grid(row=5, column=0, ipady=5, padx=5)

        item_note_entry = tk.Entry(special_edit_frame, textvariable=val_4, background="white", width=40)
        item_note_entry.grid(row=5, column=1)

        translate_button = tk.Button(special_edit_frame, text="Translate", command=quick_translate)
        translate_button.grid(row=6, column=0, columnspan=2, sticky="swen")


    elif type_key_var.get() == "Note":
        item_answer_label = tk.Label(special_edit_frame, text="Additional Info", background="white")
        item_answer_label.grid(row=2, column=0, ipady=5, padx=5)

        item_answer_entry = tk.Entry(special_edit_frame, textvariable=val_1, background="white", width=40)
        item_answer_entry.grid(row=2, column=1)



    else:
        item_answer_label = tk.Label(special_edit_frame, text="Reverse Side", background="white")
        item_answer_label.grid(row=2, column=0, ipady=5, padx=5)

        item_answer_entry = tk.Entry(special_edit_frame, textvariable=val_1, background="white", width=40)
        item_answer_entry.grid(row=2, column=1)



type_key_var.trace('w', edit_special_panel)


def create_edit_frame():
    edit_frame.grid(row=0, column=3, rowspan=2, sticky="swen")
    special_edit_frame.grid(row=2, column=0, sticky="swen", columnspan=2)
    try:
        item_iid = view_tree.selection()[0]
        item_vals = view_tree.item(item_iid)
        item_name = item_vals['text']
        item_type = item_vals['values'][0]


        variable_1 = item_vals['values'][1]
        variable_2 = item_vals['values'][2]
        variable_3 = item_vals['values'][3]
        variable_4 = item_vals['values'][4]

        val_1.set(variable_1)
        val_2.set(variable_2)
        val_3.set(variable_3)
        val_4.set(variable_4)



        # set the tkinter vars
        type_key_var.set(item_type)
        name_var.set(item_name)
        current_iid.set(item_iid)
        edit_special_panel()
        item_name_label = tk.Label(edit_frame, text="Problem", background="white")
        item_name_label.grid(row=0, column=0, ipady=5, padx=5)

        item_name_entry = tk.Entry(edit_frame, textvariable=name_var, background="white", width=40)
        item_name_entry.grid(row=0, column=1)

        item_type_label = tk.Label(edit_frame, text="Type", background="white")
        item_type_label.grid(row=1, column=0, ipady=5, padx=5, pady=(5, 0))

        item_type_entry = ttk.Combobox(edit_frame, values=types_list, textvariable=type_key_var, state="readonly")
        item_type_entry.grid(row=1, column=1, pady=(5, 0), sticky="swen")







    except IndexError:
        pass



def save_edit_from_edit_frame(*args):
    item_iid = current_iid.get()
    item_type = type_key_var.get()
    item_name = name_var.get()
    item_val_1 = val_1.get()
    item_val_2 = val_2.get()
    item_val_3 = val_3.get()
    item_val_4 = val_4.get()
    view_tree.item(item_iid, text=item_name, values=[item_type, item_val_1, item_val_2, item_val_3, item_val_4])

    edit_frame.grid_forget()


def read_page():
    file_frame.pack_forget()
    read_frame.pack(side='top', fill='both', padx=50, pady=50)

    get_pdf_button = tk.Button(read_frame, text="Open Pdf", command=open_get_pdf, background="white")
    get_pdf_button.grid(row=0, column=1, sticky="swn", ipadx=160)


    reading_box.grid(row=1, column=1, columnspan=2, sticky="swen")
    reading_box.insert(tk.END, 'This is just a test.')
    reading_box.bind("<ButtonRelease-1>", lambda e: print_the_copy())



    view_tree.grid(row=0, column=2, rowspan=2, sticky="swen", ipadx=1)
    view_tree.heading("#0", text="Problems")
    view_tree.heading("#1", text="Type")
    view_tree.column("#0", width=10)
    view_tree.column("#1", width=10, anchor="center")

    view_tree.bind("<ButtonRelease-1>", lambda e: create_edit_frame())

    section_tree = ttk.Treeview(read_frame)
    section_tree.grid(row=0, column=0, rowspan=2, sticky="swen")
    section_tree.heading("#0", text="Sections")

    font_selection_box = ttk.Combobox(read_frame, values=section_list)
    font_selection_box.grid(row=0, column=1, sticky="ens")

    save_button = tk.Button(read_frame, text="save", background="white")
    save_button.grid(row=2, column=1, columnspan=1, sticky="swen", ipady=10, pady=5)



def start_reading():
    file_name = file_name_var.get()
    file_handle = open(f"{file_name}.carb", "w")
    file_handle.write(f"L[{file_name}]")
    file_handle.close()
    read_page()


file_name_var.set("testvar1")

file_frame = tk.Frame(root, background="#222222")
file_frame.pack(side='top', fill='both', padx=(50, 0), pady=50)



read_frame = tk.Frame(root, background="#222222")
reading_box = tk.Text(read_frame)
view_tree = ttk.Treeview(read_frame, selectmode="browse", columns=("Type"))
edit_frame = tk.Frame(read_frame, background="white")
edit_frame.bind("<Button-3>", lambda e: save_edit_from_edit_frame())
special_edit_frame = tk.Frame(edit_frame, background="white")


reader_title = tk.Label(file_frame, text="Chalk Reader", background="#222222", foreground="white",
                        font=("Poor Richard", 50))
reader_title.grid(row=0, column=0, columnspan=3, sticky="swen", pady=(0, 10))

file_name_label = tk.Label(file_frame, text="File Name", background="#222222", foreground="white", font=("Poor Richard", 16))
file_name_label.grid(row=1, column=0, pady=5, padx=5)

file_name_entry = tk.Entry(file_frame, textvariable=file_name_var, font=("Poor Richard", 16), justify="center", background="white")
file_name_entry.grid(row=1, column=1)

file_name_extension_label = tk.Label(file_frame, text=".carb", background="#222222", foreground="white", font=("Poor Richard", 16))
file_name_extension_label.grid(row=1, column=2)

start_button = tk.Button(file_frame, text="Read", font=("Poor Richard", 30), background="white", command=start_reading)
start_button.grid(row=2, column=0, columnspan=3, ipadx=10, pady=10)


root.mainloop()