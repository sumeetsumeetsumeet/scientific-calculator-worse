from tkinter import PhotoImage

def configure_window(root_window):
	root_window.geometry("500x600") 
	root_window.title("Scientific Calculator.")
	root_window.config(background = "#9CD8F6")
	icon = PhotoImage(file = "misc/logo.png")
	root_window.iconphoto(True, icon)