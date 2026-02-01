from tkinter import Entry, StringVar

def create_display(window):
    input_equation_var = StringVar(master=window)
    input_equation_var.set("")

    display = Entry(
        window,
        textvariable=input_equation_var,
        font=("Consolas", 20),
        bg="white",
        fg = "black",
        justify = "right")
    
    display.pack(fill = "x", padx = 10, pady=10)
    display.configure(state="readonly")

    return input_equation_var