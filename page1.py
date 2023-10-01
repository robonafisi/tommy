import tkinter as tk
from tkinter import ttk
import signal

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
def signal_handler(signum, frame):
    root.quit()

# Bind the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Create the main window
root = tk.Tk()
root.title("Welcome, Michael!")  # Updated title
root.geometry("1600x980")  # Adjusted size to fit content
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
med_schedule_button.place(x=20, y=660, width=700, height=240)

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
get_assistance_button.place(x=860, y=660, width=700, height=240)

# Add the headline at the top left
headline = tk.Label(root, text="Welcome, Michael!", font=('calibri', 75, 'bold'), bg='white')
headline.place(x=25, y=15)

# Add logo
logo = tk.PhotoImage(file="logo.png")  # Replace 'logo.png' with your file
logo_label = tk.Label(root, image=logo, bg='white')
logo_label.place(x=1300, y=50)  # Adjust the x and y coordinates as needed

root.mainloop()
