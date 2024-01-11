import os
import rarfile
import tkinter as tk
from tkinter import filedialog

def unrar_file(path_to_rar_file, path_to_extract_to):
    with rarfile.RarFile(path_to_rar_file) as rf:
        rf.extractall(path_to_extract_to)

def gui_unrar():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    rar_path = filedialog.askopenfilename(title="Select RAR File", filetypes=[("RAR files", "*.rar")])
    if not rar_path:
        print("No RAR file selected. Exiting.")
        return

    extract_path = filedialog.askdirectory(title="Select Extraction Directory")
    if not extract_path:
        print("No extraction directory selected. Exiting.")
        return

    unrar_file(rar_path, extract_path)
    print(f"Extraction complete. Files extracted to {extract_path}")

# Uncomment the line below to enable command-line extraction
# gui_unrar()