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
root.title("Michael, time for your medication")  # Updated title
root.geometry("800x480")
root.configure(bg='white')

# Make the program run in full screen
root.attributes("-fullscreen", True)

# Create a style object
style = ttk.Style()

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
okay_button = ttk.Button(root, text="Okay", command=lambda: print("Okay pressed"), style='Green.TButton')
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
no_button = ttk.Button(root, text="No", command=lambda: print("No pressed"), style='Yellow.TButton')
no_button.place(x=1025, y=660, width=700, height=240)

# Add the 'sub_heading' label at the top left
sub_heading = tk.Label(root, text="Michael, time for your medication: ", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
sub_heading.place(x=10, y=10)

# Add the '[MEDICATION]' label to the left of the 'sub_heading' label
medication_label = tk.Label(root, text="[<<X>> TABLETS OF <<MEDICATION>>]", font=('calibri', 75, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
medication_label.place(x=10, y=140)

root.mainloop()
