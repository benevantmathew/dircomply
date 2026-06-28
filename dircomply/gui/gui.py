"""
gui.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os
import tkinter as tk
import tkinter.font as tkfont
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
    result_font_size = ui_settings["result_font_size"]
    result_font_weight = "bold" if ui_settings["result_text_bold"] else "normal"
    background_color = ui_settings["background_color"]
    foreground_color = ui_settings["foreground_color"]
    input_background_color = ui_settings["input_background_color"]
    input_foreground_color = ui_settings["input_foreground_color"]
    button_background_color = ui_settings["button_background_color"]
    button_foreground_color = ui_settings["button_foreground_color"]
    accent_color = ui_settings["accent_color"]
    result_background_color = ui_settings["result_background_color"]
    result_foreground_color = ui_settings["result_foreground_color"]

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
        popup.title("Dircomply Results")
        popup.geometry(f"{ui_settings['popup_width']}x{ui_settings['popup_height']}")
        popup.configure(bg=background_color)
        result_font = tkfont.Font(
            root=popup,
            family=font_family,
            size=result_font_size,
            weight=result_font_weight
        )

        result_text = tk.Text(
            popup,
            wrap=tk.WORD,
            font=result_font,
            bg=result_background_color,
            fg=result_foreground_color,
            insertbackground=result_foreground_color,
            selectbackground=accent_color,
            selectforeground=result_foreground_color,
            spacing3=ui_settings["result_line_spacing"],
            borderwidth=0,
            highlightthickness=0
        )
        result_text.pack(expand=True, fill=tk.BOTH)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(
            popup,
            command=result_text.yview,
            bg=ui_settings["scrollbar_background_color"],
            troughcolor=background_color,
            activebackground=accent_color
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        result_text.config(yscrollcommand=scrollbar.set)

        current_result_font_size = {"value": result_font_size}
        control_mask = 0x0004

        def update_result_font(size):
            """
            Update result text font size while keeping configured weight.
            """
            safe_size = max(8, min(72, int(size)))
            current_result_font_size["value"] = safe_size
            result_font.configure(size=safe_size)

        def zoom_result_font(event):
            """
            Ctrl + mouse wheel dynamically changes result text size.
            """
            if not getattr(event, "state", 0) & control_mask:
                return None
            wheel_delta = getattr(event, "delta", 0)
            if wheel_delta:
                direction = 1 if wheel_delta > 0 else -1
            else:
                direction = 1 if getattr(event, "num", None) == 4 else -1
            update_result_font(current_result_font_size["value"] + direction)
            return "break"

        def zoom_result_font_from_key(direction):
            """
            Ctrl + plus/minus fallback for environments that intercept Ctrl-scroll.
            """
            def zoom(_event):
                update_result_font(current_result_font_size["value"] + direction)
                return "break"
            return zoom

        for widget in (result_text, popup, scrollbar):
            widget.bind("<MouseWheel>", zoom_result_font)
            widget.bind("<Button-4>", zoom_result_font)
            widget.bind("<Button-5>", zoom_result_font)
            widget.bind("<Control-plus>", zoom_result_font_from_key(1))
            widget.bind("<Control-equal>", zoom_result_font_from_key(1))
            widget.bind("<Control-minus>", zoom_result_font_from_key(-1))


    # Main window
    root = tk.Tk()
    root.tk.call("tk", "scaling", ui_settings["tk_scaling"])
    root.title(__app_label__)
    root.geometry(f"{ui_settings['window_width']}x{ui_settings['window_height']}")
    root.configure(bg=background_color)

    folder1_var = tk.StringVar()
    folder2_var = tk.StringVar()
    if folder1_path:
        folder1_var.set(folder1_path)
    if folder2_path:
        folder2_var.set(folder2_path)

    # GUI Layout
    label_options = {"font": normal_font, "bg": background_color, "fg": foreground_color}
    entry_options = {
        "width": 50,
        "font": normal_font,
        "bg": input_background_color,
        "fg": input_foreground_color,
        "insertbackground": input_foreground_color,
        "selectbackground": accent_color,
        "selectforeground": input_foreground_color,
        "relief": tk.FLAT
    }
    button_options = {
        "font": normal_font,
        "bg": button_background_color,
        "fg": button_foreground_color,
        "activebackground": accent_color,
        "activeforeground": button_foreground_color,
        "relief": tk.FLAT,
        "borderwidth": 0,
        "padx": 8,
        "pady": 4
    }

    tk.Label(root, text="Folder 1 Path:", **label_options).pack(pady=5)
    tk.Entry(root, textvariable=folder1_var, **entry_options).pack()
    tk.Button(root, text="Select Folder 1", command=select_folder1, **button_options).pack(pady=5)

    tk.Label(root, text="Folder 2 Path:", **label_options).pack(pady=5)
    tk.Entry(root, textvariable=folder2_var, **entry_options).pack()
    tk.Button(root, text="Select Folder 2", command=select_folder2, **button_options).pack(pady=5)

    compare_button_options = button_options.copy()
    compare_button_options.update({"font": button_font, "bg": accent_color})
    tk.Button(root, text="Compare Folders", command=compare, **compare_button_options).pack(pady=20)
    if compare_on_start and folder1_path and folder2_path:
        compare()

    root.mainloop()
