from tkinter import Entry, StringVar

def create_display(root_window):
    input_equation_var = StringVar(master=root_window)
    input_equation_var.set("")

    display = Entry(
        root_window,
        textvariable=input_equation_var,
        font=("Consolas", 20),
        bg="white",
        fg = "black",
        justify = "right")
    
    display.pack(fill = "x", padx = 10, pady=10)
    # display.configure(state="readonly")

    return input_equation_var