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
root.configure(bg='white')

# Make the program run in full screen
root.attributes("-fullscreen", True)

# Add the 'sub_heading' label at the top left
sub_heading = tk.Label(root, text="Michael, Congratulations!!", font=('calibri', 80, 'bold'), bg='white')
sub_heading.place(x=10, y=10)

# Display text indicating the number of tablets taken
tablets_taken = tk.Label(root, text="You have taken 4 tablets of Melatonin!\nWell done!!", font=('calibri', 40, 'bold'), bg='white')
tablets_taken.place(x=10, y=140)

root.mainloop()