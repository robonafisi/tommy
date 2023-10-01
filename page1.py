import tkinter as tk
from tkinter import ttk
from page2 import Page2

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='white')

        # Create a style object
        style = ttk.Style(self)

        # Configure the custom style for the 'Medicine Schedule' button
        style.configure('Green.TButton',
                        font=('calibri', 40, 'bold'),
                        borderwidth='4',
                        background='light green')
        style.map('Green.TButton',
                  foreground=[('pressed', 'black'), ('active', 'black')],
                  background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
                  )

        # Create the 'Medicine Schedule' button using the custom style and place it at the bottom left
        med_schedule_button = ttk.Button(self, text="Medicine Schedule", command=lambda: controller.show_page(Page2), style='Green.TButton')
        med_schedule_button.place(x=20, y=660, width=700, height=240)

        # ... Other UI elements ...

        self.after(10000, self.move_to_page2)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def move_to_page2(self):
        self.controller.show_page(Page2)
