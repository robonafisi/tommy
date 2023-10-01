import tkinter as tk
from tkinter import ttk
import signal
from page2 import *

# # Handler to close the tkinter window when receiving a SIGINT or SIGTERM
# def signal_handler(signum, frame):
#     root.quit()

def page1(root, controller):
    # Bind the signal handler
    signal.signal(signal.SIGINT, lambda signum, frame: controller.quit())
    signal.signal(signal.SIGTERM, lambda signum, frame: controller.quit())

    # Create the main window
    # root.title("Welcome, Michael!")  # Updated title
    # root.geometry("1600x980")  # Adjusted size to fit content
    root.configure(bg='white')

    # Make the program run in full screen
    # root.attributes("-fullscreen", True)

    # Create a style object
    style = ttk.Style(root)

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
    med_schedule_button = ttk.Button(root, text="Medicine Schedule", command=lambda: controller.show_page(Page2), style='Green.TButton')
    med_schedule_button.place(x=20, y=660, width=700, height=240)
    # med_schedule_button.pack()

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
    get_assistance_button = ttk.Button(root, text="Get Assistance", command=lambda: controller.show_page(Page2), style='Yellow.TButton')
    get_assistance_button.place(x=860, y=660, width=700, height=240)
    # get_assistance_button.pack()

    # Add the headline at the top left
    headline = tk.Label(root, text="Welcome, Michael!", font=('calibri', 75, 'bold'), bg='white')
    headline.place(x=25, y=15)

    # Add logo
    logo = tk.PhotoImage(file="logo.png")  # Replace 'logo.png' with your file
    logo_label = tk.Label(root, image=logo, bg='white')
    logo_label.place(x=1300, y=50)  # Adjust the x and y coordinates as needed

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        page1(self, controller)
        
        # button_page2 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
        # button_page2.pack()
    
        # button_page2 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
        # button_page2.pack()

        self.after(10000, self.move_to_page2)
        # stay on this page for 10 seconds 

    def move_to_page2(self):
        self.controller.show_page(Page2)