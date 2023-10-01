import tkinter as tk
from tkinter import ttk
from page1 import Page1
from page2 import Page2

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")

        # Create container frame to hold pages
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.pages = {}  # Dictionary to store page instances

        # Initialize and add pages to the dictionary
        self.pages[Page1] = Page1(self.container, self)
        self.pages[Page2] = Page2(self.container, self)

        # Show the initial page
        self.show_page(Page1)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.show()
        for other_page_class, other_page in self.pages.items():
            if other_page_class != page_class:
                other_page.hide()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
