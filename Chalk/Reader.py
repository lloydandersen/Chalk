import tkinter as tk
from tkinter import ttk
import pdfplumber

root = tk.Tk()
# variables
page_count_var = tk.IntVar()
current_page_count_var = tk.IntVar()
current_page_text_var = tk.StringVar()
modes = ['Title', 'Sections', "Reader"]


def back_a_page():
    current_page_number = current_page_count_var.get()
    current_page_number -= 1
    current_page_count_var.set(current_page_number)
    text_box.delete("1.0", "end")
    pdf_parser()
    page_text = current_page_text_var.get()
    text_box.insert(tk.END, page_text)


def forward_a_page():
    current_page_number = current_page_count_var.get()
    current_page_number += 1
    current_page_count_var.set(current_page_number)
    text_box.delete("1.0", "end")
    pdf_parser()
    page_text = current_page_text_var.get()
    text_box.insert(tk.END, page_text)


def get_page_text():
    pass


def pdf_parser():
    file_handle = pdfplumber.open("Calculus_Volume_1_OpenStax.pdf")


    # statistics
    # set page counts
    page_count = len(file_handle.pages)
    page_count_var.set(page_count)

    text_string = file_handle.pages[current_page_count_var.get()].extract_text()
    current_page_text_var.set(text_string)


    file_handle.close()



button = tk.Button(root, text="Click me", command=pdf_parser)
button.pack()

button = tk.Button(root, text="back", command=back_a_page)
button.pack()

button = tk.Button(root, text="forward", command=forward_a_page)
button.pack()

text_box = tk.Text(root)
text_box.pack()

view_tree = ttk.Treeview(root)
view_tree.pack(side="right")

mode_selector = ttk.Combobox(root, values=modes)
mode_selector.pack(side="left")

statistics_frame = tk.Frame(root)
statistics_frame.pack()



root.mainloop()

