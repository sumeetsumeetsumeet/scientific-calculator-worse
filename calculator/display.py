from tkinter import Entry, StringVar

def create_display(window):
    equation_var = StringVar(master=window)
    equation_var.set("")

    display = Entry(
        window,
        textvariable=equation_var,
        font=("Consolas", 20),
        bg="white",
        fg = "black",
        justify = "right"
    )
    display.pack(fill = "x", padx = 10, pady=10)
    display.configure(state="readonly")

    return equation_var