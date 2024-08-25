import tkinter as tk
import pdfplumber as plm

working_dict = {}


def get_fonts_used():
    pass


def read_pdf():
    pdf_loc = pdf_location.get()
    with plm.open(f"{pdf_loc}") as pdf:
        page_selected = pdf.pages[30]
        page_chars = list(page_selected.lines)
        for i in page_chars:
            print(f"{i}\n")
        pdf.close()


root = tk.Tk()

root.title('Chalk PDF Reader')
root.config(background="#222222")
# root.geometry("500x500")
pdf_location = tk.StringVar()


home_page_frame = tk.Frame(root)
home_page_frame.pack(side="top", fill="both", pady=50, padx=50)
home_page_frame.configure(background="#222222")

file_location_label = tk.Label(home_page_frame, text="PDF Location", background="#222222", foreground="white")
file_location_label.grid(row=0, column=0, padx=5, pady=5)

file_location_entry = tk.Entry(home_page_frame, textvariable=pdf_location)
file_location_entry.grid(row=0, column=1, padx=5, pady=5)

parse_pdf_button = tk.Button(home_page_frame, text="Read", command=read_pdf)
parse_pdf_button.grid(row=1, column=0, columnspan=2, sticky="swen")

root.mainloop()
