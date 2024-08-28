import tkinter as tk
from tkinter import ttk
import pdfplumber
from tkinter.filedialog import FileDialog

root = tk.Tk()
root.title("Reader")
root.configure(background="#222222")
# variables
page_count_var = tk.IntVar()
current_page_count_var = tk.IntVar()
current_page_text_var = tk.StringVar()
modes = ['Info', 'Section', "Reader", "Translate", "Calculate"]
file_name_var = tk.StringVar()
current_pdf_var = tk.BooleanVar()
mode_var = tk.StringVar()
text_title_var = tk.StringVar()
text_authors_var = tk.StringVar()
end_page_var = tk.IntVar()

current_pdf_var.set(False)
text_title_var.set("Open")
mode_var.set("Info")
file_name_var.set("Calculus_Volume_1_OpenStax.pdf")
current_page_count_var.set(0)
end_page_var.set(0)



# Frames and Widgets
control_panel_frame = tk.Frame(root)
main_panel_frame = tk.Frame(root)
edit_panel_frame = tk.Frame(root)
statistical_frame = tk.Frame(root)
info_frame = tk.Frame(root)
section_tree = ttk.Treeview()
reader_tree = ttk.Treeview()
text_box = tk.Text(main_panel_frame)


def update_highest_page():
    if current_page_count_var.get() > end_page_var.get():
        new_high = current_page_count_var.get()
        end_page_var.set(new_high)




def clear_root_frame():
    for child in root.winfo_children():
        child.grid_forget()



def configure_app():
    pass


def back_a_page():
    current_page_number = current_page_count_var.get()
    current_page_number -= 1
    current_page_count_var.set(current_page_number)
    text_box.delete("1.0", "end")
    pdf_parser()
    page_text = current_page_text_var.get()
    text_box.insert(tk.END, page_text)
    update_highest_page()


def forward_a_page():
    current_page_number = current_page_count_var.get()
    current_page_number += 1
    current_page_count_var.set(current_page_number)
    text_box.delete("1.0", "end")
    pdf_parser()
    page_text = current_page_text_var.get()
    text_box.insert(tk.END, page_text)
    update_highest_page()


def get_page_text():
    pass


def pdf_parser():
    file_handle = pdfplumber.open(f"{file_name_var.get()}")


    # statistics
    # set page counts
    page_count = len(file_handle.pages)
    page_count_var.set(page_count)

    text_string = file_handle.pages[current_page_count_var.get()].extract_text()
    current_page_text_var.set(text_string)


    file_handle.close()


def open_pdf(*args):
    if current_pdf_var.get() is False:
        file_name = tk.filedialog.askopenfilename()
        file_name_var.set(file_name)
        current_pdf_var.set(True)

        build_info_panel()
        pdf_parser()
    else:
        pass


def build_info_panel():
    info_frame.grid(row=1, column=1, columnspan=1, sticky="n")
    text_title_label = tk.Label(info_frame, text="Title")
    text_title_label.grid(row=0, column=0)

    text_title_entry = tk.Entry(info_frame, textvariable=text_title_var, width=30, justify="center")
    text_title_entry.grid(row=0, column=1)

    text_authors_label = tk.Label(info_frame, text="Author")
    text_authors_label.grid(row=1, column=0)

    text_authors_entry = tk.Entry(info_frame, textvariable=text_authors_var, width=30)
    text_authors_entry.grid(row=1, column=1)

    text_page_count_label = tk.Label(info_frame, text="Page Count")
    text_page_count_label.grid(row=2, column=0)

    text_page_count_entry = tk.Entry(info_frame, textvariable=page_count_var, width=30, justify="center")
    text_page_count_entry.grid(row=2, column=1)

    file_name_label = tk.Label(info_frame, text="File")
    file_name_label.grid(row=3, column=0)

    file_name_entry = tk.Entry(info_frame, textvariable=file_name_var, justify="left", width=30)
    file_name_entry.grid(row=3, column=1)

    highest_page_label = tk.Label(info_frame, text="Highest Page")
    highest_page_label.grid(row=4, column=0)

    highest_page_entry = tk.Entry(info_frame, textvariable=end_page_var, justify="left", width=30)
    highest_page_entry.grid(row=4, column=1)

    build_text_box()


def build_control_panel():
    control_panel_frame.grid(row=0, column=0, columnspan=3, sticky="swen")
    name_label = tk.Label(control_panel_frame, textvariable=text_title_var)
    name_label.grid(row=0, column=0, ipadx=10)
    name_label.bind("<Button-1>", lambda e: open_pdf())

    mode_entry_box = ttk.Combobox(control_panel_frame, textvariable=mode_var, values=modes, state="readonly")
    mode_entry_box.grid(row=0, column=1)


    page_number_label = tk.Label(control_panel_frame, textvariable=current_page_count_var)
    page_number_label.grid(row=0, column=2)

    back_button = tk.Button(control_panel_frame, text="back", command=back_a_page)
    back_button.grid(row=0, column=3)

    forward_button = tk.Button(control_panel_frame, text="forward", command=forward_a_page)
    forward_button.grid(row=0, column=4)

    save_button = tk.Button(control_panel_frame, text="Save")
    save_button.grid(row=0, column=5)


def build_text_box():
    main_panel_frame.grid(row=1, column=0, sticky="swen")
    text_box.configure(height=45)
    text_box.configure(width=120)
    text_box.grid(row=0, column=0, sticky="swen")




def main():
    configure_app()
    pdf_parser()
    build_control_panel()



# button = tk.Button(root, text="Click me", command=pdf_parser)
# button.pack()
#

#
# text_box = tk.Text(root)
# text_box.pack()
#
# view_tree = ttk.Treeview(root)
# view_tree.pack(side="right")
#
# mode_selector = ttk.Combobox(root, values=modes)
# mode_selector.pack(side="left")
#
# statistics_frame = tk.Frame(root)
# statistics_frame.pack()

main()



root.mainloop()

