import tkinter as tk
from tkinter import ttk
import signal

from page1 import *
from page3 import *
from page4 import *

def page2(root, controller):
    signal.signal(signal.SIGINT, lambda signum, frame: controller.quit())
    signal.signal(signal.SIGTERM, lambda signum, frame: controller.quit())
    root.configure(bg='white')
    style = ttk.Style(root)
    style.configure('Green.TButton',
    font=('calibri', 40, 'bold'),
    borderwidth='4',
    background='light green')
    style.map('Green.TButton',
foreground=[('pressed', 'black'), ('active', 'black')],
background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
)

# Create the 'Medicine Schedule' button using the custom style and place it at the bottom left
    med_schedule_button = ttk.Button(root, text="Medicine Schedule", command=lambda: controller.show_page(Page1), style='Green.TButton')
    med_schedule_button.place(x=125, y=660, width=700, height=240)

# Configure the custom style for the 'Get Assistance' button
    style.configure('Yellow.TButton',
font=('calibri', 40, 'bold'),
borderwidth='4',
background='light yellow')
    style.map('Yellow.TButton',
foreground=[('pressed', 'black'), ('active', 'black')],
background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
)

# Create the 'Get Assistance' button using the custom style and place it at the bottom right
    get_assistance_button = ttk.Button(root, text="Get Assistance", command=lambda: controller.show_page(Page4), style='Yellow.TButton')
    get_assistance_button.place(x=1025, y=660, width=700, height=240)

# Add the headline at the top left
    headline = tk.Label(root, text="Michael, 30 mins until your next dose of Melatonin", font=('calibri', 75, 'bold'), bg='white',justify=tk.LEFT, wraplength=1850)
    headline.place(x=35, y=75)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        page2(self, controller)
        self.after(30000, self.move_to_page2)
# stay on this page for 10 seconds

    def move_to_page2(self):
        self.controller.show_page(Page3)