import tkinter as tk
from tkinter import ttk
import signal

from page4 import *
from page5 import *


def page3(root, controller):
    # Bind the signal handler
    signal.signal(signal.SIGINT, lambda signum, frame: controller.quit())
    signal.signal(signal.SIGTERM, lambda signum, frame: controller.quit())
    root.configure(bg='white')

    # Make the program run in full screen
    # root.attributes("-fullscreen", True)

    # Create a style object
    style = ttk.Style(root)

    # Configure the custom style for the 'Okay' button
    style.configure('Green.TButton',
    font=('calibri', 80, 'bold'),
    borderwidth='4',
    background='light green')
    style.map('Green.TButton',
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
    )

    # Create the 'Okay' button using the custom style and place it at the bottom left
    okay_button = ttk.Button(root, text="Okay", command=lambda: controller.show_page(Page5), style='Green.TButton')
    okay_button.place(x=125, y=660, width=700, height=240)

    # Configure the custom style for the 'No' button
    style.configure('Yellow.TButton',
    font=('calibri', 80, 'bold'),
    borderwidth='4',
    background='light yellow')
    style.map('Yellow.TButton',
    foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
    )

    # Create the 'No' button using the custom style and place it at the bottom right
    no_button = ttk.Button(root, text="No", command=lambda: controller.show_page(Page4), style='Yellow.TButton')
    no_button.place(x=1025, y=660, width=700, height=240)

    # Add the 'sub_heading' label at the top left
    sub_heading = tk.Label(root, text="Michael, time for your medication: ", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
    sub_heading.place(x=10, y=10)

    # Add the '[MEDICATION]' label to the left of the 'sub_heading' label
    medication_label = tk.Label(root, text="2 TABLETS OF Melatonin", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
    medication_label.place(x=10, y=140)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        page3(self, controller)
        # # ok button --> page 5 
        # button_page1 = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_page(Page5))
        # button_page1.pack()
        # # no button --> page 4
        # button_page4 = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_page(Page4))
        # button_page4.pack()