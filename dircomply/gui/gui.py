"""
gui.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os
import tkinter as tk
from tkinter import filedialog, messagebox

from dircomply.application.config import paths
from dircomply.basic_functions.settings import load_ui_settings
from dircomply.core.compare import compare_folders
from dircomply.version import __app_label__

def create_gui(
        folder1_path=None,
        folder2_path=None,
        compare_on_start=False,
        compare_options=None,
        ui_options=None
    ):
    """
    create_gui
    # GUI Application
    """
    compare_options = compare_options or {}
    ui_settings = load_ui_settings(paths.get_settings_filepath(), ui_options)
    font_family = ui_settings["font_family"]
    normal_font = (font_family, ui_settings["font_size"])
    button_font = (font_family, ui_settings["font_size"], "bold")
    result_font = (font_family, ui_settings["result_font_size"])

    def select_folder1():
        path = filedialog.askdirectory(title="Select Folder 1")
        if path:
            folder1_var.set(path)

    def select_folder2():
        path = filedialog.askdirectory(title="Select Folder 2")
        if path:
            folder2_var.set(path)

    def compare():
        folder1 = folder1_var.get()
        folder2 = folder2_var.get()

        if not folder1 or not folder2:
            messagebox.showerror("Error", "Please select both folders")
            return

        if not os.path.exists(folder1) or not os.path.exists(folder2):
            messagebox.showerror("Error", "One or both folders do not exist")
            return

        # Compare folders
        different_files, unique_to_folder1, unique_to_folder2 = compare_folders(
            folder1,
            folder2,
            **compare_options
        )

        # Create result message
        result = f"Comparison Results: of {folder1} and {folder2}\n\n"
        if different_files:
            result += "Files with differences:\n" + "\n".join(different_files) + "\n\n"
        else:
            result += "No files with differences found.\n\n"

        if unique_to_folder1:
            result += f"Files unique to {folder1}:\n" + "\n".join(unique_to_folder1) + "\n\n"
        if unique_to_folder2:
            result += f"Files unique to {folder2}:\n" + "\n".join(unique_to_folder2) + "\n\n"

        # Display results in a popup window
        popup = tk.Toplevel(root)
        popup.title("Comparison Results")
        popup.geometry(f"{ui_settings['popup_width']}x{ui_settings['popup_height']}")

        result_text = tk.Text(popup, wrap=tk.WORD, font=result_font)
        result_text.pack(expand=True, fill=tk.BOTH)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(popup, command=result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        result_text.config(yscrollcommand=scrollbar.set)


    # Main window
    root = tk.Tk()
    root.tk.call("tk", "scaling", ui_settings["tk_scaling"])
    root.title(__app_label__)
    root.geometry(f"{ui_settings['window_width']}x{ui_settings['window_height']}")

    folder1_var = tk.StringVar()
    folder2_var = tk.StringVar()
    if folder1_path:
        folder1_var.set(folder1_path)
    if folder2_path:
        folder2_var.set(folder2_path)

    # GUI Layout
    tk.Label(root, text="Folder 1 Path:", font=normal_font).pack(pady=5)
    tk.Entry(root, textvariable=folder1_var, width=50, font=normal_font).pack()
    tk.Button(root, text="Select Folder 1", command=select_folder1, font=normal_font).pack(pady=5)

    tk.Label(root, text="Folder 2 Path:", font=normal_font).pack(pady=5)
    tk.Entry(root, textvariable=folder2_var, width=50, font=normal_font).pack()
    tk.Button(root, text="Select Folder 2", command=select_folder2, font=normal_font).pack(pady=5)

    tk.Button(root, text="Compare Folders", command=compare, font=button_font, bg="lightblue").pack(pady=20)
    if compare_on_start and folder1_path and folder2_path:
        compare()

    root.mainloop()
