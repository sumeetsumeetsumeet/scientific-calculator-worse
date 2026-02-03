from tkinter import Tk
from calculator.window_config import configure_window
from calculator.display import create_display
from calculator.buttons import create_buttons

def main():
	root_window = Tk()
	configure_window(root_window)
	input_equation_var = create_display(root_window)
	create_buttons(root_window, input_equation_var)
	root_window.mainloop()

if __name__ == "__main__":
	main()