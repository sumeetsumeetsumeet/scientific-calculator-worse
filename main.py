from tkinter import Tk
from calculator.window_config import configure_window
from calculator.display import create_display
from calculator.buttons import create_buttons

def main():
	root_window = Tk()
	screen_width = root_window.winfo_screenwidth()
	screen_height = root_window.winfo_screenheight()
	width = int(screen_width*0.3)
	height = int(screen_height*0.7)
	root_window.geometry(f"{width}x{height}")
	root_window.resizable(False, False)
	configure_window(root_window)
	input_equation_var = create_display(root_window)
	create_buttons(root_window, input_equation_var)

	root_window.mainloop()

if __name__ == "__main__":
	main()