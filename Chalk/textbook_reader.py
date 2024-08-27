import tkinter as tk
from tkinter.filedialog import FileDialog
from tkinter import ttk

root = tk.Tk()
root.title("Chalk Reader")
root.configure(background="#222222")

file_name_var = tk.StringVar()
question_var = tk.StringVar()
pdf_location = tk.StringVar()
section_list = []
selected_string = tk.StringVar()
selected_section = tk.StringVar()

selected_section.set("test section")

# functions


def open_get_pdf():
    location = tk.filedialog.askopenfilename(title="Select a file", filetypes=(("carbon files", "*.carb"),
                                                                               ("all files", "*.*")))

    pdf_location.set(location)


def print_the_copy(*args):
    selected_string.set(f"{reading_box.selection_get()}")
    view_tree.insert("", tk.END, text=selected_string.get(), values=(selected_section.get()))




def read_page():
    file_frame.pack_forget()
    read_frame.pack(side='top', fill='both', padx=50, pady=50)

    get_pdf_button = tk.Button(read_frame, text="Open Pdf", command=open_get_pdf, background="white")
    get_pdf_button.grid(row=0, column=1, sticky="swn", ipadx=160)


    reading_box.grid(row=1, column=1, columnspan=2)
    reading_box.insert(tk.END, 'This is just a test.')
    reading_box.bind("<Button-3>", lambda e: print_the_copy())



    view_tree.grid(row=0, column=2, rowspan=2, sticky="swen", ipadx=1)
    view_tree.heading("#0", text="Problems")
    view_tree.column("#0", width=1)
    view_tree.bind("<Button-3>", lambda e: print(selected_section.get()))

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
file_frame.pack(side='top', fill='both', padx=50, pady=50)

read_frame = tk.Frame(root, background="#222222")
reading_box = tk.Text(read_frame)
view_tree = ttk.Treeview(read_frame)

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