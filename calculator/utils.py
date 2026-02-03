from math import sin,cos,tan,asin,acos,atan,log10,log,sqrt,cbrt,exp,pi,e,radians,degrees,factorial

mode = "DEG"
def sin_(x): 
    if mode == "DEG":
        return sin(radians(x))
    return sin(x)

def cos_(x): 
    if mode == "DEG":
        return cos(radians(x))
    return cos(x)

def tan_(x): 
    if mode == "DEG":
        return tan(radians(x))
    return tan(x)

def asin_(x):
    result = asin(x)
    if mode == "DEG":
        return degrees(result)
    return result

def acos_(x):
    result = acos(x)
    if mode == "DEG":
        return degrees(result)
    return result

def atan_(x):
    result = atan(x)
    if mode == "DEG":
        return degrees(result)
    return result

def toggle_mode():
    global mode
    if mode == "DEG":
        mode = "RAD"
    else:
        mode = "DEG"

def append(value, input_equation_var):
    input_equation_var.set(input_equation_var.get() + str(value))

def delete(input_equation_var):
     input_equation_var.set(input_equation_var.get()[:-1])

def clear(input_equation_var):
	input_equation_var.set("")

def remove_floating_point_error(x, err=1e-10):
    try:
        if abs(x) < err:
            return 0.0

        nearest = round(x)
        if abs(x - nearest) < err:
            return float(nearest)
        return x
    except TypeError:
        return x

def compute(equation_var):
    expr = equation_var.get()
    
    if not expr:
        return

    try:
        functions_dict = {

            # Trigonometric Fucntions
            "sin": sin_,
            "cos": cos_,
            "tan": tan_,
            "asin": asin_,
            "acos": acos_,
            "atan": atan_,

            # constants
            "pi": pi,
            "e": e,

            # log and exponent
            "log10": log10,
            "ln": log,
            "exp": exp,

            # roots
            "sqrt": sqrt,
            "cbrt": cbrt,

            #factorial
            "fact":factorial
        }

        result = eval(expr, functions_dict)
        result = remove_floating_point_error(result)
        equation_var.set(str(result))

    except Exception as error:
        print("error:", error)
        equation_var.set("Error")