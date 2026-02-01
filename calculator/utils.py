
def button_press(num):
	pass

def append(value, equation_var):
    equation_var.set(equation_var.get() + str(value))
    print(equation_var.get())

def clear(equation_var):
	equation_var.set("")

def compute(equation_var):
    try:
        result = str(eval(equation_var.get()))
        equation_var.set(result)
    except Exception:
        equation_var.set("")

def apply_function(function, equation_var):
    current = equation_var.get()

    if current == "" or current == "Error":
        return

    try:
        value = float(current)
        result = function(value)
        equation_var.set(str(result))
    except Exception:
        equation_var.set("Error")