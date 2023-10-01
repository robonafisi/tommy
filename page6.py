import tkinter as tk
import signal

from page2 import *

# Handler to close the tkinter window when receiving a SIGINT or SIGTERM
# def signal_handler(signum, frame):
#     root.quit()

# Bind the signal handler
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

def page6(root, controller):
    # Create the main window
    signal.signal(signal.SIGINT, lambda signum, frame: controller.quit())
    signal.signal(signal.SIGTERM, lambda signum, frame: controller.quit())

    # root = tk.Tk()
    # root.title("Inactivity Warning")  # Updated title
    # root.geometry("1600x960")
    root.configure(bg='white')

    # Make the program run in full screen
    # root.attributes("-fullscreen", True)

    # Add the 'sub_heading' label at the top left
    sub_heading = tk.Label(root, text="Inactivity Warning!!", font=('calibri', 80, 'bold'), bg='white')
    sub_heading.place(x=10, y=10)

    # Display text indicating the inactivity warning
    warning_text = tk.Label(root, text="""Due to extended inactivity, we are now contacting your chosen\nemergency contact on your behalf. This is for your well being.""",
    font=('calibri', 60, 'bold'), bg='white', justify=tk.LEFT, wraplength=1850)
    warning_text.place(x=10, y=250)


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        page6(self, controller)
        self.after(5000, self.move_to_page2)
        # stay on this page for 5 seconds 

    def move_to_page2(self):
        self.controller.show_page(Page2)