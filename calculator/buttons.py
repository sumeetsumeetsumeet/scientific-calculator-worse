from tkinter import Button, Frame
from calculator.utils import append, clear, compute, delete, toggle_mode
BUTTONS = [
    ["sin", "cos", "tan", "√","(", ")"],
    ["asin", "acos", "atan", "π", "DEL", "AC"],
    ["ln", "log10", "7", "8", "9", "/"],
    ["exp", "1/x", "4", "5", "6", "*"],
    ["x²", "xʸ", "1", "2", "3", "-"],
    ["x³","e","%", "0", ".", "+"],
    ["fact","∛","DEG/RAD", "="]
    ]

def create_buttons(root_window, input_equation_var):
    frame = Frame(root_window)
    frame.pack()

    for row in BUTTONS:
        row_frame = Frame(frame)
        row_frame.pack(fill="both", expand= True)
        
        for label in row:
            btn_width = 5
            if label in ["DEG/RAD", "="]:
                btn_width = 12
            # Utils
            if label == "AC":
                cmd = lambda ev = input_equation_var: clear(ev)
            elif label == "DEL":
                cmd = lambda ev = input_equation_var: delete(ev)
            elif label == "=":
                cmd = lambda ev = input_equation_var: compute(ev)
            elif label == "DEG/RAD":
                cmd = toggle_mode

            elif label in ["asin", "acos", "atan", "sin", "cos", "tan", "exp","log10", "ln"]:
                cmd = lambda val = label +"(", ev= input_equation_var: append(val, ev)

            elif label == "fact":
                cmd = lambda ev=input_equation_var: append("fact(", ev)

            # Roots
            elif label == "√":
                cmd = lambda ev=input_equation_var: append("sqrt(", ev)
            elif label == "∛":
                cmd = lambda ev = input_equation_var: append("cbrt(", ev)

            # Constants
            elif label == "π":
                cmd = lambda ev=input_equation_var: append("pi", ev)

            # Powers
            elif label == "x²":
                cmd = lambda ev=input_equation_var: append("**2", ev)

            elif label == "x³":
                cmd = lambda ev=input_equation_var: append("**3", ev)

            elif label == "xʸ":
                cmd = lambda ev=input_equation_var: append("**", ev)
            elif label == "1/x":
                cmd = lambda ev = input_equation_var: append("1/", ev)

            # For digits
            else:
                cmd = lambda val = label, ev= input_equation_var: append(val, ev)
                  
            Button(
                row_frame,
                text=label,
                width=btn_width,
                height=2,
                command=cmd
                ).pack(side="left", padx=2, pady=2)