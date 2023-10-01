import tkinter as tk
from tkinter import ttk
import signal

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
def signal_handler(signum, frame):
    root.quit()

# Bind the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# This will change the headline when the "Don't need to take medicine" button is clicked
def on_no_button_click():
    sub_heading.config(text="Michael, you clicked \"Don't need to take medicine\".\nPlease share why you are unable to take the medicine")

# Create the main window
root = tk.Tk()
root.title("Medication Reminder")  # Initial title
root.geometry("1600x960")
root.configure(bg='white')

# Make the program run in full screen
root.attributes("-fullscreen", True)

# Create a style object
style = ttk.Style()

# Configure the custom style for the 'Don't want to take medicine' button
style.configure('Green.TButton',
font=('calibri', 40, 'bold'),
borderwidth='4',
background='light green')
style.map('Green.TButton',
foreground=[('pressed', 'black'), ('active', 'black')],
background=[('pressed', '!disabled', 'dark green'), ('active', 'light green')]
)

# Create the 'Don't want to take medicine' button using the custom style and place it at the bottom left
dont_want_button = ttk.Button(root, text="Don't want to take medicine", command=lambda: print("Don't want to take medicine pressed"), style='Green.TButton')
dont_want_button.place(x=20, y=660, width=750, height=200)

# Configure the custom style for the 'Don't need to take medicine' button
style.configure('Yellow.TButton',
font=('calibri', 40, 'bold'),
borderwidth='4',
background='light yellow')
style.map('Yellow.TButton',
foreground=[('pressed', 'black'), ('active', 'black')],
background=[('pressed', '!disabled', 'dark orange'), ('active', 'light yellow')]
)

# Create the 'Don't need to take medicine' button using the custom style and place it at the bottom right
dont_need_button = ttk.Button(root, text="Don't need to take medicine", command=on_no_button_click, style='Yellow.TButton')
dont_need_button.place(x=800, y=660, width=750, height=200)

# Add the 'sub_heading' label at the top left
sub_heading = tk.Label(root, text="It's time for your medication, Michael.", font=('calibri', 40, 'bold'), bg='white')
sub_heading.place(x=10, y=10)

root.mainloop()