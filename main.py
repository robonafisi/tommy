
import numpy as np
import tkinter as tk
from page1 import *
from page2 import *
from page3 import *
from page4 import *
from page5 import *
from page6 import *
import time
from move import *
import threading

def call_move():
    time.sleep(10)
    move_main()
    
    

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Create a container to hold the pages
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=1)

        # Expand to fill app
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Dictionary to store references to all pages
        self.pages = {}

        # Create instances of your pages and add them to the dictionary
        for PageClass in (Page1, Page2, Page3, Page4, Page5, Page6):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        t = threading.Thread(target=move_main)
        t.start()
        self.show_page(Page1)


    def show_page(self, page_class):
        # Hide the current page
        current_page = self.pages[page_class]
        current_page.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.geometry("1600x980")
    app.mainloop()

# # page 1 is just a welcome page -- buttons don't go to anything 
# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 1")
#         label.pack(pady=10, padx=10)
        
#         button_page2 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
#         button_page2.pack()
    
#         button_page2 = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
#         button_page2.pack()

#         self.after(10000, self.move_to_page2)
#         # stay on this page for 10 seconds 

#     def move_to_page2(self):
#         self.controller.show_page(Page2)

# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 2")
#         label.pack(pady=10, padx=10)
       
#         button_page1 = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page(Page1))
#         button_page1.pack()
#         button_page4 = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_page(Page4))
#         button_page4.pack()
        # timed with timer counting down till t = 0 (initialized to 10 seconds)

# take your meds 
# class Page3(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 3")
#         label.pack(pady=10, padx=10)
#         # ok button --> page 5 
#         button_page1 = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_page(Page5))
#         button_page1.pack()
#         # no button --> page 4
#         button_page4 = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_page(Page4))
#         button_page4.pack()

# # why are you not taking meds
# class Page4(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 4")
#         label.pack(pady=10, padx=10)
#         # dont want -->  fuck you
#         button_page2 = tk.Button(self, text="Go to Page 6", command=lambda: controller.show_page(Page6))
#         button_page2.pack()
#         # dont need --> fuck you
#         button_page3 = tk.Button(self, text="Go to Page 6", command=lambda: controller.show_page(Page6))
#         button_page3.pack()

# # congratulations
# class Page5(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 5")
#         label.pack(pady=10, padx=10)
#         self.after(5000, self.move_to_page2)
#         # stay on this page for 5 seconds 

#     def move_to_page2(self):
#         self.controller.show_page(Page2)


# # inactivity page
# class Page6(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Page 5")
#         label.pack(pady=10, padx=10)
#         self.after(5000, self.move_to_page2)
#         # stay on this page for 5 seconds 

#     def move_to_page2(self):
#         self.controller.show_page(Page2)
