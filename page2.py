import tkinter as tk
from tkinter import ttk
from page1 import Page1
from page3 import Page3
from page4 import Page4

class Page2(tk.Frame):
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
        med_schedule_button = ttk.Button(self, text="Medicine Schedule", command=lambda: controller.show_page(Page1), style='Green.TButton')
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
        get_assistance_button = ttk.Button(self, text="Get Assistance", command=lambda: controller.show_page(Page4), style='Yellow.TButton')
        get_assistance_button.place(x=1025, y=660, width=700, height=240)

        # Add the headline at the top left
        headline = tk.Label(self, text="Michael, 30 mins until your next dose of Melatonin", font=('calibri', 75, 'bold'), bg='white',justify=tk.LEFT, wraplength=1850)
        headline.place(x=35, y=75)

        self.after(10000, self.move_to_page3)  # Stay on this page for 10 seconds

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def move_to_page3(self):
        self.controller.show_page(Page3)
