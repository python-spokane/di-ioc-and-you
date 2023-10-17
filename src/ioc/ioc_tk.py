"""An example of using Inversion of Control with the Tkinter framework.

See https://martinfowler.com/bliki/InversionOfControl.html
"""
import tkinter as tk

def process_name(entry_widget):
    """Handle the name processing logic"""
    name = entry_widget.get()
    # ...

def process_quest(entry_widget):
    """Handle the quest processing logic"""
    quest = entry_widget.get()
    # ...

def main():
    root = tk.Tk()

    # Name Label
    name_label = tk.Label(root, text="What is Your Name?")
    name_label.pack()

    # Name Entry
    name_entry = tk.Entry(root)
    name_entry.pack()
    name_entry.bind("<FocusOut>", lambda event: process_name(name_entry))

    # Quest Label
    quest_label = tk.Label(root, text="What is Your Quest?")
    quest_label.pack()

    # Quest Entry
    quest_entry = tk.Entry(root)
    quest_entry.pack()
    quest_entry.bind("<FocusOut>", lambda event: process_quest(quest_entry))

    tk.mainloop()


if __name__ == "__main__":
    main()
