import tkinter as tk
from tkinter import ttk
import signal

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
def signal_handler(signum, frame):
    root.quit()

def page2():
    # Bind the signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Create the main window
    root = tk.Tk()
    root.title("Michael, 30 mins until your next dose of Melatonin")  # Updated title
    root.geometry("800x480")
    root.configure(bg='white')

    # Make the program run in full screen
    root.attributes("-fullscreen", True)

    # Create a style object
    style = ttk.Style()

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
    med_schedule_button = ttk.Button(root, text="Medicine Schedule", command=lambda: print("Medicine Schedule pressed"), style='Green.TButton')
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
    get_assistance_button = ttk.Button(root, text="Get Assistance", command=lambda: print("Get Assistance pressed"), style='Yellow.TButton')
    get_assistance_button.place(x=1025, y=660, width=700, height=240)

    # Add the headline at the top left
    headline = tk.Label(root, text="Michael, 30 mins until your next dose of Melatonin", font=('calibri', 75, 'bold'), bg='white',justify=tk.LEFT, wraplength=1850)
    headline.place(x=35, y=75)

    root.mainloop()
