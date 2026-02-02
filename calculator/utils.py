from math import sin,cos,tan,asin,acos,atan,log10,log,sqrt,cbrt,exp,pi,e

def button_press(num):
	pass

def append(value, input_equation_var):
    input_equation_var.set(input_equation_var.get() + str(value))

def delete(input_equation_var):
     input_equation_var.set(input_equation_var.get()[:-1])

def clear(input_equation_var):
	input_equation_var.set("")

def compute(input_equation_var):

    expression = input_equation_var.get()
    const_func = {"e": e, "π": pi}
    functions_dict = {"asin": asin, "acos": acos, "atan": atan,
                      "sin": sin, "cos": cos, "tan": tan, "exp": exp,
                      "log10": log10, "ln": log, "√": sqrt, "∛" :cbrt}

    for func in list(functions_dict.keys()):
        if func in expression:
            num = float(expression.replace(func,"").strip())
            result = functions_dict[func](num)
            input_equation_var.set(result)
            return
        
    for const in const_func:
         if const in expression:
            current = input_equation_var.get().replace(const,"").strip()
            if current == "":
                current = 1
            result = float(current)*const_func[const]
            input_equation_var.set(str(result))
            return

    try:
        result = str(eval(input_equation_var.get()))
        input_equation_var.set(result)
    except Exception:
        input_equation_var.set("")

def apply_function(label, input_equation_var):
    current = input_equation_var.get()

    if current == "" or current == "Error":
        return

    try:
        value = float(current)
        result = function(current)
        input_equation_var.set(str(result))
    except Exception:
         pass
        # input_equation_var.set("Error")