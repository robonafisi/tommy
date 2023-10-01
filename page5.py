import tkinter as tk
import signal

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
def signal_handler(signum, frame):
    root.quit()

# Bind the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Create the main window
root = tk.Tk()
root.title("Medication Reminder")  # Updated title
root.geometry("1600x960")
root.configure(bg='pink')

# Make the program run in full screen
root.attributes("-fullscreen", True)

logo = tk.PhotoImage(file="Tommy.png")  # Replace 'logo.png' with your file
logo_label = tk.Label(root, image=logo, bg='pink')
logo_label.place(x=1200, y=250)  # Adjust the x and y coordinates as needed

# Add the 'sub_heading' label at the top left
sub_heading = tk.Label(root, text="Michael, Congratulations!!", font=('calibri', 80, 'bold'), bg='pink', justify=tk.LEFT, wraplength=1850)
sub_heading.place(x=10, y=10)

# Display text indicating the number of tablets taken
tablets_taken = tk.Label(root, text="You have taken 4 tablets of Melatonin!\nWell done!!", font=('calibri', 60, 'bold'), bg='pink', justify=tk.LEFT, wraplength=1200)
tablets_taken.place(x=10, y=250)

root.mainloop()