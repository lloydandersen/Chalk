import tkinter as tk

root = tk.Tk()
root.title("Chalk Reader")
root.configure(background="#222222")

file_name_var = tk.StringVar()
question_var = tk.StringVar()

# functions
def start_reading():
    pass

file_name_var.set("testvar1")

file_frame = tk.Frame(root, background="#222222")
file_frame.pack(side='top', fill='both', padx=50, pady=50)

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