
def button_press(num):
	pass

def append(value, input_equation_var):
    input_equation_var.set(input_equation_var.get() + str(value))
    #print(input_equation_var.get())

def delete(input_equation_var):
     input_equation_var.set(input_equation_var.get()[:-1])

def clear(input_equation_var):
	input_equation_var.set("")

def compute(input_equation_var):
    try:
        result = str(eval(input_equation_var.get()))
        input_equation_var.set(result)
    except Exception:
        input_equation_var.set("")

def apply_function(function, input_equation_var):
    current = input_equation_var.get()

    if current == "" or current == "Error":
        return

    try:
        value = float(current)
        result = function(value)
        input_equation_var.set(str(result))
    except Exception:
        input_equation_var.set("Error")