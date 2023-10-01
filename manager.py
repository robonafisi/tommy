import tkinter as tk
from tkinter import ttk
from page1 import Page1
from page2 import Page2

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")
        
        # Create UI elements for the main app
        
        # Buttons to switch between pages
        self.page1_button = ttk.Button(root, text="Page 1", command=self.show_page1)
        self.page2_button = ttk.Button(root, text="Page 2", command=self.show_page2)
        
        self.page1_button.pack()
        self.page2_button.pack()
        
        # Initialize Page1 and Page2
        self.page1 = Page1(root)
        self.page2 = Page2(root)

    def show_page1(self):
        self.page2.hide()
        self.page1.show()

    def show_page2(self):
        self.page1.hide()
        self.page2.show()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.run()
