import tkinter as tk
from tkinter import ttk
import signal

from page6 import *

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM

def page4(root, controller):
    # Bind the signal handler
    signal.signal(signal.SIGINT, lambda signum, frame: controller.quit())
    signal.signal(signal.SIGTERM, lambda signum, frame: controller.quit())


    # This will change the headline when the "Don't need to take medicine" button is clicked
    def on_no_button_click():
        sub_heading.config(text="Michael, you clicked \"Don't need to take medicine\".\nPlease share why you are unable to take the medicine")

    # Create the main window
    # root = tk.Tk()
    # root.title("Medication Reminder")  # Initial title
    # root.geometry("1600x960")
    root.configure(bg='white')

    # Make the program run in full screen
    # root.attributes("-fullscreen", True)

    # Create a style object
    style = ttk.Style(root)

    # Configure the custom style for the 'Don't want to take medicine' button
    style.configure('Green.TButton',
    font=('calibri', 50, 'bold'),
    borderwidth='4',
    background='light green')
    style.map('Green.TButton',
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
    )

    logo = tk.PhotoImage(file="cry.png")  # Replace 'logo.png' with your file
    logo_label = tk.Label(root, image=logo, bg='white')
    logo_label.place(x=900, y=10)  # Adjust the x and y coordinates as needed


    # Create the 'Don't want to take medicine' button using the custom style and place it at the bottom left
    dont_want_button = ttk.Button(root, text="Don't want", command=lambda: controller.show_page(Page6), style='Green.TButton')
    dont_want_button.place(x=125, y=660, width=700, height=240)

    # Configure the custom style for the 'Don't need to take medicine' button
    style.configure('Yellow.TButton',
    font=('calibri', 50, 'bold'),
    borderwidth='4',
    background='light yellow')
    style.map('Yellow.TButton',
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
    )

    # Create the 'Don't need to take medicine' button using the custom style and place it at the bottom right
    dont_need_button = ttk.Button(root, text="Don't need", command=lambda: controller.show_page(Page6), style='Yellow.TButton')
    dont_need_button.place(x=1025, y=660, width=700, height=240)

    sub_heading = tk.Label(root, text="You chose No", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
    sub_heading.place(x=10, y=10)

    # Add the 'sub_heading' label at the top left
    sub_heading = tk.Label(root, text="Please share why you cannot take the medicine.", font=('calibri', 40, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
    sub_heading.place(x=10, y=200)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        page4(self, controller)
        # # dont want -->  fuck you
        # button_page2 = tk.Button(self, text="Go to Page 6", command=lambda: controller.show_page(Page6))
        # button_page2.pack()
        # # dont need --> fuck you
        # button_page3 = tk.Button(self, text="Go to Page 6", command=lambda: controller.show_page(Page6))
        # button_page3.pack()