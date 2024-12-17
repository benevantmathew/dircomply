import tkinter as tk
from tkinter import filedialog, messagebox
import os

# extension to compare
ext_list=('.txt','.py','.bat','.html')
# Function to read file content
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error: {e}"

# Function to get all files with specific extensions in a folder and its subdirectories
def get_files_with_extensions(folder, extensions):
    all_files = set()
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extensions):
                relative_path = os.path.relpath(os.path.join(root_dir, file), folder)
                all_files.add(relative_path)
    return all_files

# Function to compare files and find differences
def compare_folders(folder1, folder2):
    folder1_files = get_files_with_extensions(folder1, ext_list)
    folder2_files = get_files_with_extensions(folder2, ext_list)

    # Common files
    common_files = folder1_files & folder2_files

    # Unique files
    unique_to_folder1 = folder1_files - folder2_files
    unique_to_folder2 = folder2_files - folder1_files

    # Files with differences
    different_files = []
    for file in common_files:
        path1 = os.path.join(folder1, file)
        path2 = os.path.join(folder2, file)
        if read_file(path1) != read_file(path2):
            different_files.append(file)

    return different_files, unique_to_folder1, unique_to_folder2

# GUI Application
def create_gui():
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
        different_files, unique_to_folder1, unique_to_folder2 = compare_folders(folder1, folder2)

        # Create result message
        result = """Comparison Results:\n\n"""
        if different_files:
            result += "Files with differences:\n" + "\n".join(different_files) + "\n\n"
        else:
            result += "No files with differences found.\n\n"

        if unique_to_folder1:
            result += "Files unique to Folder 1:\n" + "\n".join(unique_to_folder1) + "\n\n"
        if unique_to_folder2:
            result += "Files unique to Folder 2:\n" + "\n".join(unique_to_folder2) + "\n\n"
        
        # Display results in a popup window
        popup = tk.Toplevel(root)
        popup.title("Comparison Results")
        popup.geometry("600x400")

        result_text = tk.Text(popup, wrap=tk.WORD, font=("Arial", 10))
        result_text.pack(expand=True, fill=tk.BOTH)
        result_text.insert(tk.END, result)
        result_text.config(state=tk.DISABLED)

    # Main window
    root = tk.Tk()
    root.title("Folder File Comparator")
    root.geometry("500x300")

    folder1_var = tk.StringVar()
    folder2_var = tk.StringVar()

    # GUI Layout
    tk.Label(root, text="Folder 1 Path:", font=("Arial", 12)).pack(pady=5)
    tk.Entry(root, textvariable=folder1_var, width=50).pack()
    tk.Button(root, text="Select Folder 1", command=select_folder1).pack(pady=5)

    tk.Label(root, text="Folder 2 Path:", font=("Arial", 12)).pack(pady=5)
    tk.Entry(root, textvariable=folder2_var, width=50).pack()
    tk.Button(root, text="Select Folder 2", command=select_folder2).pack(pady=5)

    tk.Button(root, text="Compare Folders", command=compare, font=("Arial", 12, "bold"), bg="lightblue").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
