import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import hashlib
import os

# -----------------------------
# Global Variables
# -----------------------------

selected_file = ""
current_hash = ""

# -----------------------------
# Browse File
# -----------------------------

def browse_file():
    global selected_file

    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_label.config(text=os.path.basename(selected_file))
        result_box.delete("1.0", tk.END)
        hash_entry.delete(0, tk.END)

# -----------------------------
# Calculate File Hash
# -----------------------------

def calculate_hash(algorithm="sha256"):

    global current_hash

    if selected_file == "":
        messagebox.showwarning(
            "Warning",
            "Please select a file."
        )
        return

    if algorithm == "sha256":
        hash_object = hashlib.sha256()
    else:
        hash_object = hashlib.md5()

    with open(selected_file, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            hash_object.update(chunk)

    current_hash = hash_object.hexdigest()

    hash_entry.delete(0, tk.END)
    hash_entry.insert(0, current_hash)

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        f"{algorithm.upper()} Hash Generated Successfully.\n\n"
    )

# -----------------------------
# Compare Hash
# -----------------------------

def compare_hash():

    if current_hash == "":
        messagebox.showwarning(
            "Warning",
            "Generate a hash first."
        )
        return

    entered_hash = hash_entry.get().strip()

    result_box.delete("1.0", tk.END)

    if entered_hash == current_hash:

        result_box.insert(
            tk.END,
            "Integrity Verified ✅\n\n"
        )

        status_label.config(
            text="Status : File Not Modified",
            fg="green"
        )

    else:

        result_box.insert(
            tk.END,
            "Integrity Failed ❌\n\n"
        )

        status_label.config(
            text="Status : File Modified",
            fg="red"
        )

# -----------------------------
# Save Hash
# -----------------------------

def save_hash():

    if current_hash == "":
        messagebox.showwarning(
            "Warning",
            "Generate hash first."
        )
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt"
    )

    if save_path:

        with open(save_path, "w") as file:

            file.write(current_hash)

        messagebox.showinfo(
            "Success",
            "Hash saved successfully."
        )
# -----------------------------
# Dark Mode
# -----------------------------

def dark_mode():

    root.configure(bg="#2b2b2b")

    widgets = [
        title,
        file_label,
        hash_label,
        status_label
    ]

    for widget in widgets:
        widget.configure(bg="#2b2b2b", fg="white")

    result_box.configure(
        bg="#3b3b3b",
        fg="white"
    )


# -----------------------------
# Light Mode
# -----------------------------

def light_mode():

    root.configure(bg="white")

    widgets = [
        title,
        file_label,
        hash_label,
        status_label
    ]

    for widget in widgets:
        widget.configure(bg="white", fg="black")

    result_box.configure(
        bg="white",
        fg="black"
    )


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("File Integrity Checker")

root.geometry("650x700")

root.configure(bg="white")


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    root,
    text="File Integrity Checker",
    font=("Arial",18,"bold"),
    bg="white"
)

title.pack(pady=15)


# -----------------------------
# Browse Button
# -----------------------------

tk.Button(
    root,
    text="Browse File",
    command=browse_file,
    bg="#2196F3",
    fg="white",
    width=20
).pack(pady=5)


# -----------------------------
# Selected File
# -----------------------------

file_label = tk.Label(
    root,
    text="No file selected",
    bg="white",
    font=("Arial",11)
)

file_label.pack(pady=10)


# -----------------------------
# Generate Hash Buttons
# -----------------------------

tk.Button(
    root,
    text="Generate SHA-256",
    command=lambda: calculate_hash("sha256"),
    bg="#4CAF50",
    fg="white",
    width=20
).pack(pady=5)

tk.Button(
    root,
    text="Generate MD5",
    command=lambda: calculate_hash("md5"),
    bg="#9C27B0",
    fg="white",
    width=20
).pack(pady=5)


# -----------------------------
# Progress Bar
# -----------------------------

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="indeterminate"
)

progress.pack(pady=10)


# -----------------------------
# Hash Entry
# -----------------------------

hash_label = tk.Label(
    root,
    text="File Hash",
    bg="white",
    font=("Arial",12,"bold")
)

hash_label.pack()

hash_entry = tk.Entry(
    root,
    width=70
)

hash_entry.pack(pady=10)


# -----------------------------
# Buttons
# -----------------------------

tk.Button(
    root,
    text="Compare Hash",
    command=compare_hash,
    bg="#FF9800",
    fg="white",
    width=20
).pack(pady=5)

tk.Button(
    root,
    text="Save Hash",
    command=save_hash,
    bg="#795548",
    fg="white",
    width=20
).pack(pady=5)
# -----------------------------
# Result Box
# -----------------------------

result_label = tk.Label(
    root,
    text="Result",
    font=("Arial",12,"bold"),
    bg="white"
)

result_label.pack(pady=10)

result_box = tk.Text(
    root,
    width=70,
    height=10,
    font=("Arial",10)
)

result_box.pack(pady=10)


# -----------------------------
# Status Label
# -----------------------------

status_label = tk.Label(
    root,
    text="Status : Waiting",
    font=("Arial",12,"bold"),
    bg="white",
    fg="blue"
)

status_label.pack(pady=10)


# -----------------------------
# Theme Buttons
# -----------------------------

theme_frame = tk.Frame(root, bg="white")

theme_frame.pack(pady=10)

dark_button = tk.Button(
    theme_frame,
    text="Dark Mode",
    command=dark_mode,
    bg="black",
    fg="white",
    width=12
)

dark_button.grid(row=0, column=0, padx=5)

light_button = tk.Button(
    theme_frame,
    text="Light Mode",
    command=light_mode,
    bg="white",
    fg="black",
    width=12
)

light_button.grid(row=0, column=1, padx=5)


# -----------------------------
# Footer
# -----------------------------

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Arial",10),
    bg="white"
)

footer.pack(pady=20)


# -----------------------------
# Start GUI
# -----------------------------

root.mainloop()
