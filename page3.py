import tkinter as tk
from tkinter import ttk
from page4 import Page4
from page5 import Page5

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='white')

        # Create a style object
        style = ttk.Style(self)

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
        okay_button = ttk.Button(self, text="Okay", command=lambda: controller.show_page(Page5), style='Green.TButton')
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
        no_button = ttk.Button(self, text="No", command=lambda: controller.show_page(Page4), style='Yellow.TButton')
        no_button.place(x=1025, y=660, width=700, height=240)

        # Add the 'sub_heading' label at the top left
        sub_heading = tk.Label(self, text="Michael, time for your medication: ", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
        sub_heading.place(x=10, y=10)

        # Add the '[MEDICATION]' label to the left of the 'sub_heading' label
        medication_label = tk.Label(self, text="[<<X>> TABLETS OF <<MEDICATION>>]", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
        medication_label.place(x=10, y=140)

        self.after(10000, self.move_to_page4)  # Stay on this page for 10 seconds

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def move_to_page4(self):
        self.controller.show_page(Page4)
