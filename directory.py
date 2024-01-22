import tkinter as tk
from tkinter import filedialog

def directory_select():

    def select_directory():
        global directory_path
        directory_path = filedialog.askdirectory()
        if directory_path:
            show_selected_directory(directory_path)
            window.destroy()

    def show_selected_directory(directory_path):
        directory_window = tk.Toplevel(window)
        directory_window.title("Selected Directory")
        selected_directory_label = tk.Label(directory_window, text=f"Selected Directory: {directory_path}")
        selected_directory_label.pack(pady=10)
        ok_button = tk.Button(directory_window, text="OK", command=directory_window.destroy)
        ok_button.pack(pady=10)

    window = tk.Tk()
    window.title("Select Directory GUI")
    label = tk.Label(window, text="Click the button to select a directory:")
    label.pack(pady=10)
    select_button = tk.Button(window, text="Select Directory", command=select_directory)
    select_button.pack(pady=10)
    window.mainloop()

    global directory_path
    path=directory_path

    return path