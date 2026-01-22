import tkinter as tk

def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry_var = tk.StringVar()

# Display
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 22),
    bd=8,
    relief="sunken",
    justify="right",
    bg="#ffffff"
)
entry.pack(fill="x", padx=10, pady=15)

# Button frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Button colors
num_color = "#8fd3ff"      # light blue
op_color = "#c3b1e1"       # soft purple
eq_color = "#7CFC98"       # green
clear_color = "#ff7f7f"    # red

buttons = [
    ("7", num_color), ("8", num_color), ("9", num_color), ("/", op_color),
    ("4", num_color), ("5", num_color), ("6", num_color), ("*", op_color),
    ("1", num_color), ("2", num_color), ("3", num_color), ("-", op_color),
    ("0", num_color), (".", num_color), ("=", eq_color), ("+", op_color)
]

row = 0
col = 0

for text, color in buttons:
    if text == "=":
        btn = tk.Button(
            frame, text=text, bg=color, fg="black",
            font=("Arial", 14, "bold"),
            width=5, height=2,
            command=calculate
        )
    else:
        btn = tk.Button(
            frame, text=text, bg=color, fg="black",
            font=("Arial", 14),
            width=5, height=2,
            command=lambda t=text: press(t)
        )

    btn.grid(row=row, column=col, padx=6, pady=6)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(
    root, text="Clear",
    bg=clear_color, fg="black",
    font=("Arial", 14, "bold"),
    width=22, height=2,
    command=clear
)
clear_btn.pack(pady=15)

root.mainloop()
