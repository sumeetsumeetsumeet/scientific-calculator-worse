from tkinter import Button, Frame
from calculator.utils import append, clear, compute, delete
BUTTONS = [
    ["sin", "cos", "tan", "√","(", ")"],
    ["asin", "acos", "atan", "π", "DEL", "AC"],
    ["ln", "log10", "7", "8", "9", "/"],
    ["exp", "1/x", "4", "5", "6", "*"],
    ["x²", "xʸ", "1", "2", "3", "-"],
    ["x³","e", "0", ".", "=", "+"]
    ]

def create_buttons(root_window, input_equation_var):
    frame = Frame(root_window)
    frame.pack()

    for row in BUTTONS:
        row_frame = Frame(frame)
        row_frame.pack()
        
        for label in row:
            # Utils
            if label == "AC":
                cmd = lambda ev = input_equation_var: clear(ev)

            elif label == "DEL":
                cmd = lambda ev = input_equation_var: delete(ev)
            elif label == "=":
                cmd = lambda ev = input_equation_var: compute(ev)

            # Trigonometric Functions
            elif label == "sin":
                cmd = lambda ev=input_equation_var: append("sin(", ev)

            elif label == "cos":
                cmd = lambda ev=input_equation_var: append("cos(", ev)

            elif label == "tan":
                cmd = lambda ev=input_equation_var: append("tan(", ev)

            elif label == "asin":
                cmd = lambda val="asin(", ev=input_equation_var: append(val, ev)

            elif label == "acos":
                cmd = lambda val="acos(", ev=input_equation_var: append(val, ev)

            elif label == "atan":
                cmd = lambda val="atan(", ev=input_equation_var: append(val, ev)

            # Roots
            elif label == "√":
                cmd = lambda ev=input_equation_var: append("sqrt(", ev)

            # Constants
            elif label == "π":
                cmd = lambda ev=input_equation_var: append("pi", ev)

            elif label == "e":
                cmd = lambda val="e", ev=input_equation_var: append(val, ev)

            # Powers
            elif label == "x²":
                cmd = lambda ev=input_equation_var: append("**2", ev)

            elif label == "x³":
                cmd = lambda ev=input_equation_var: append("**3", ev)

            elif label == "xʸ":
                cmd = lambda ev=input_equation_var: append("**", ev)

            # For digits
            else:
                cmd = lambda val = label, ev= input_equation_var: append(val, ev)
                  
            Button(
                row_frame,
                text=label,
                width=5,
                height=2,
                command=cmd
                ).pack(side="left", padx=2, pady=2)