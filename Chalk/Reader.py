import tkinter as tk
from tkinter import ttk
import pdfplumber
from tkinter.filedialog import FileDialog
from tkinter import messagebox
import toml as tml

root = tk.Tk()
root.update_idletasks()

root.title("Reader")
root.configure(background="#222222")
# variables
page_count_var = tk.IntVar()
current_page_count_var = tk.IntVar()
current_page_text_var = tk.StringVar()
modes = ['Info', 'Section', "Reader", "Translate", "Calculate", "Speedread", "Fastread"]
note_types = ['Note', 'NoteCard', 'MultipleChoice', 'Translator', 'MathProblem']
file_name_var = tk.StringVar()
current_pdf_var = tk.BooleanVar()
mode_var = tk.StringVar()
text_title_var = tk.StringVar()
text_authors_var = tk.StringVar()
end_page_var = tk.IntVar()
publisher_name_var = tk.StringVar()
publisher_location_var = tk.StringVar()
publishing_date_var = tk.StringVar()



# Config Styles
# Text config
text_font_family_var = tk.StringVar()
text_size_var = tk.IntVar()
text_weight_var = tk.StringVar()
text_box_background_color_var = tk.StringVar()
text_box_foreground_color_var = tk.StringVar()


# Translator Settings
translator_service_var = tk.StringVar()
translate_from_var = tk.StringVar()
translate_to_var = tk.StringVar()

# Reader Settings
default_note_type_var = tk.StringVar()
default_page_number_var = tk.IntVar()
default_text_to_speech_speed_var = tk.IntVar()
default_text_highlight_color_var = tk.StringVar()

# Speedread Settings
speed_read_wpm_var = tk.IntVar()


# App settings
auto_definition_toggle_var = tk.StringVar()
auto_translation_toggle_var = tk.StringVar()
reader_dark_mode_var = tk.StringVar()

# set up
current_pdf_var.set(False)
text_title_var.set("open")
mode_var.set("Info")
current_page_count_var.set(default_page_number_var.get())
end_page_var.set(0)

# Frames and Widgets
control_panel_frame = tk.Frame(root)
main_panel_frame = tk.Frame(root)
edit_panel_frame = tk.Frame(root)
statistical_frame = tk.Frame(root)
info_frame = tk.Frame(root)
trandict_frame = tk.Frame(root)
section_tree = ttk.Treeview()
reader_tree = ttk.Treeview()
text_box = tk.Text(main_panel_frame, state="normal")


def update_highest_page():
    if current_page_count_var.get() > end_page_var.get():
        new_high = current_page_count_var.get()
        end_page_var.set(new_high)


def copy_to_title(*args):
    content = text_box.selection_get()
    text_title_var.set(content)
    main_panel_frame.focus_set()

def copy_to_author(*args):
    content = text_box.selection_get()
    text_authors_var.set(content)
    main_panel_frame.focus_set()


def copy_to_publisher(*args):
    content = text_box.selection_get()
    publisher_name_var.set(content)
    main_panel_frame.focus_set()


def copy_to_publisher_location(*args):
    content = text_box.selection_get()
    publisher_location_var.set(content)
    main_panel_frame.focus_set()


def copy_to_publishing_date(*args):
    content = text_box.selection_get()
    publishing_date_var.set(content)
    main_panel_frame.focus_set()


def clear_root_frame():
    for child in root.winfo_children():
        child.grid_forget()



def configure_app():
    try:
        toml_handle = open("reader_config.toml", "r")
        toml_dictionary = tml.load(toml_handle)

        # text config
        text_config_dict = toml_dictionary['text_config']
        text_font_family_var.set(f"{text_config_dict['text_font_family']}")
        text_size_var.set(f"{text_config_dict['text_size']}")
        text_weight_var.set(f"{text_config_dict['text_weight']}")
        text_box_background_color_var.set(f"{text_config_dict['text_box_background_color']}")
        text_box_foreground_color_var.set(f"{text_config_dict['text_box_foreground_color']}")

        # translator config
        translator_config_dict = toml_dictionary['translator_config']
        translator_service_var.set(f"{translator_config_dict['translator_service']}")
        translate_from_var.set(f"{translator_config_dict['translate_from']}")
        translate_to_var.set(f"{translator_config_dict['translate_to']}")


        # reader config
        reader_config_dict = toml_dictionary['reader_config']
        default_note_type_var.set(f"{reader_config_dict['default_note_type']}")
        default_page_number_var.set(f"{reader_config_dict['default_page_number']}")
        current_page_count_var.set(default_page_number_var.get())


        # speedread config
        speedread_config_dict = toml_dictionary['speedread_config']
        speed_read_wpm_var.set(f"{speedread_config_dict['speed_read_wpm']}")

        # app config
        app_config_dict = toml_dictionary['app_config']
        auto_definition_toggle_var.set(f"{app_config_dict['auto_definition_toggle']}")
        auto_translation_toggle_var.set(f"{app_config_dict['auto_translation_toggle']}")
        reader_dark_mode_var.set(f"{app_config_dict['dark_mode_toggle']}")
        default_text_to_speech_speed_var.set(f"{app_config_dict['text_to_speech_speed']}")
        default_text_highlight_color_var.set(f"{app_config_dict['highlight_color']}")

        toml_handle.close()

    except KeyError:
        tk.messagebox.showwarning("Configuration Failure", "Please Fix Config File and Restart!")



def back_a_page(*args):
    try:
        if current_pdf_var.get() is not False:
            text_box.configure(state="normal")
            current_page_number = current_page_count_var.get()
            current_page_number -= 1
            current_page_count_var.set(current_page_number)
            text_box.delete("1.0", "end")
            pdf_parser()
            page_text = current_page_text_var.get()
            # text_box.tag_config('tag-center', justify='left')
            text_box.insert(tk.END, page_text)
            update_highest_page()
            text_box.configure(state="disabled")
        else:
            pass
    except FileNotFoundError:
        current_page_count_var.set(0)


def forward_a_page(*args):
    try:
        if current_pdf_var.get() is not False:
            text_box.configure(state="normal")
            current_page_number = current_page_count_var.get()
            current_page_number += 1
            current_page_count_var.set(current_page_number)
            text_box.delete("1.0", "end")
            pdf_parser()
            # text_box.tag_config('tag-center', justify='left')
            page_text = current_page_text_var.get()
            text_box.insert(tk.END, page_text)
            update_highest_page()
            text_box.configure(state="disabled")
        else:
            pass
    except FileNotFoundError:
        current_page_count_var.set(0)


root.bind("<Left>", lambda e: back_a_page())
root.bind("<Right>", lambda e: forward_a_page())


def highlight_page_text():
    try:
        start = text_box.index("sel.first")
        end = text_box.insert("sel.last")
        text_box.tag_add("sel_txt", start, end)
        text_box.tag_config('sel_txt', background="yellow", foreground='red')
    except tk.TclError:
        pass

def reset_highlight():
    text_box.tag_remove('sel_txt', '1.0', 'end')

def pop_up_translation():
    pass


def pop_up_definition():
    pass


def pop_up_text_to_speech():
    pass




def pdf_parser():
    try:
        file_handle = pdfplumber.open(f"{file_name_var.get()}")


        # statistics
        # set page counts
        page_count = len(file_handle.pages)
        page_count_var.set(page_count)

        text_string = file_handle.pages[current_page_count_var.get()].extract_text()
        current_page_text_var.set(text_string)


        file_handle.close()
    except FileNotFoundError:
        open_pdf()


def open_pdf(*args):
    try:
        if current_pdf_var.get() is False:
            file_name = tk.filedialog.askopenfilename()
            file_name_var.set(file_name)
            current_pdf_var.set(True)
            current_page_count_var.set(default_page_number_var.get())
            pdf_parser()
            build_info_panel()
            end_page_var.set(0)

        else:
            pass
    except FileNotFoundError:
        current_pdf_var.set(False)
        tk.messagebox.showwarning("No File Found", "Please try again opening the PDF file.")


def build_info_panel():
    info_frame.grid(row=1, column=1, columnspan=1, sticky="n")
    text_title_label = tk.Label(info_frame, text="Title")
    text_title_label.grid(row=0, column=0)

    text_title_entry = tk.Entry(info_frame, textvariable=text_title_var, width=30, justify="center")
    text_title_entry.grid(row=0, column=1)
    text_title_entry.bind("<Button-3>", lambda e: copy_to_title())

    text_authors_label = tk.Label(info_frame, text="Author")
    text_authors_label.grid(row=1, column=0)

    text_authors_entry = tk.Entry(info_frame, textvariable=text_authors_var, width=30)
    text_authors_entry.grid(row=1, column=1)
    text_authors_entry.bind("<Button-3>", lambda e: copy_to_author())

    text_publisher_label = tk.Label(info_frame, text="Publisher")
    text_publisher_label.grid(row=2, column=0)

    text_publisher_entry = tk.Entry(info_frame, textvariable=publisher_name_var, width=30)
    text_publisher_entry.grid(row=2, column=1)
    text_publisher_entry.bind("<Button-3>", lambda e: copy_to_publisher())

    text_location_label = tk.Label(info_frame, text="Location")
    text_location_label.grid(row=3, column=0)

    text_location_entry = tk.Entry(info_frame, textvariable=publisher_location_var, width=30)
    text_location_entry.grid(row=3, column=1)
    text_location_entry.bind("<Button-3>", lambda e: copy_to_publisher_location())

    text_publish_date_label = tk.Label(info_frame, text="Date")
    text_publish_date_label.grid(row=4, column=0)

    text_publish_date_entry = tk.Entry(info_frame, textvariable=publishing_date_var, width=30)
    text_publish_date_entry.grid(row=4, column=1)
    text_publish_date_entry.bind("<Button-3>", lambda e: copy_to_publishing_date())

    # details
    text_page_count_label = tk.Label(info_frame, text="Page Count")
    text_page_count_label.grid(row=5, column=0)

    text_page_count_entry = tk.Entry(info_frame, textvariable=page_count_var, width=30, justify="center")
    text_page_count_entry.grid(row=5, column=1)

    file_name_label = tk.Label(info_frame, text="File")
    file_name_label.grid(row=6, column=0)

    file_name_entry = tk.Entry(info_frame, textvariable=file_name_var, justify="left", width=30)
    file_name_entry.grid(row=6, column=1)

    highest_page_label = tk.Label(info_frame, text="Highest Page")
    highest_page_label.grid(row=7, column=0)

    highest_page_entry = tk.Entry(info_frame, textvariable=end_page_var, justify="left", width=30)
    highest_page_entry.grid(row=7, column=1)

    build_text_box()

def move_back_page():
    page_num = current_page_count_var.get()
    page_num -= 1
    current_page_count_var.set(page_num)
    forward_a_page()


def change_page_number(*args):
    new_frame = tk.Toplevel(root)
    page_count_entry = tk.Entry(new_frame, textvariable=current_page_count_var)
    page_count_entry.pack()

    page_count_update_button = tk.Button(new_frame, text="Go to", command=move_back_page)
    page_count_update_button.pack()


def build_control_panel():
    control_panel_frame.grid(row=0, column=0, columnspan=3, sticky="swen")
    name_label = tk.Label(control_panel_frame, textvariable=text_title_var)
    name_label.grid(row=0, column=0, ipadx=10)
    name_label.bind("<Button-1>", lambda e: open_pdf())

    mode_entry_box = ttk.Combobox(control_panel_frame, textvariable=mode_var, values=modes, state="readonly")
    mode_entry_box.grid(row=0, column=1)


    page_number_label = tk.Label(control_panel_frame, textvariable=current_page_count_var)
    page_number_label.grid(row=0, column=2)
    page_number_label.bind("<Button-3>", lambda e: change_page_number())

    back_button = tk.Button(control_panel_frame, text="back", command=back_a_page)
    back_button.grid(row=0, column=3)

    forward_button = tk.Button(control_panel_frame, text="forward", command=forward_a_page)
    forward_button.grid(row=0, column=4)

    save_button = tk.Button(control_panel_frame, text="Save")
    save_button.grid(row=0, column=5)


def build_text_box():
    main_panel_frame.grid(row=1, column=0, sticky="swen")
    text_box.configure(height=30)
    text_box.configure(width=100)
    text_box.grid(row=0, column=0, sticky="swen", padx=(5, 0), pady=(0, 5))
    current_text = current_page_text_var.get()
    # text_box.tag_config('tag-center', justify='left')
    text_box.insert(tk.END, current_text)
    text_box.configure(state="disabled")


    text_box.configure(font=(text_font_family_var.get(), text_size_var.get(), text_weight_var.get()))


def create_reader_save_file():
    pass


def open_reader_save_file():
    pass


def main():
    configure_app()
    pdf_parser()
    build_control_panel()

text_box.bind("<KeyPress-h>", lambda e: highlight_page_text())
text_box.bind("<KeyPress-r>", lambda e: reset_highlight())
text_box.bind("<KeyPress-t>", lambda e: pop_up_translation())
text_box.bind("<KeyPress-d>", lambda e: pop_up_definition())
text_box.bind("<KeyPress-s>", lambda e: pop_up_text_to_speech())


main()



root.mainloop()


