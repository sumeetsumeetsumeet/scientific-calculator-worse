from tkinter import PhotoImage

def configure_window(root_window):
	root_window.title("Scientific Calculator.")
	root_window.config(background = "black")
	icon = PhotoImage(file = "misc/logo.png")
	root_window.iconphoto(True, icon)