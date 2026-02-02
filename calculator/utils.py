from math import sin,cos,tan,asin,acos,atan,log10,log,sqrt,cbrt,exp,pi,e, radians

def sin_deg(x): return sin(radians(x))
def cos_deg(x): return cos(radians(x))
def tan_deg(x): return tan(radians(x))

def button_press(num):
	pass

def append(value, input_equation_var):
    input_equation_var.set(input_equation_var.get() + str(value))

def delete(input_equation_var):
     input_equation_var.set(input_equation_var.get()[:-1])

def clear(input_equation_var):
	input_equation_var.set("")

def compute(equation_var):
    expr = equation_var.get()

    if not expr:
        return

    try:
        functions_dict = {

            # Trigonometric Fucntions
            "sin": sin_deg,
            "cos": cos_deg,
            "tan": tan_deg,
            "asin": asin,
            "acos": acos,
            "atan": atan,

            # constants
            "pi": pi,
            "e": e,

            # log and exponent
            "log10": log10,
            "ln": log,
            "exp": exp,

            # roots
            "sqrt": sqrt,
        }

        result = eval(expr, functions_dict)
        equation_var.set(str(result))

    except Exception as error:
        print("error-:", error)
        equation_var.set("Error")