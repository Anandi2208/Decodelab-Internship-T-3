import tkinter as tk
from tkinter import messagebox

def analyze_message():

    message = input_text.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning(
            "Warning",
            "Please enter a message or email."
        )
        return

    red_flags = []

    keywords = [
        "urgent",
        "verify",
        "click here",
        "password",
        "bank",
        "login",
        "winner",
        "prize",
        "gift",
        "account suspended",
        "free"
    ]

    for word in keywords:
        if word.lower() in message.lower():
            red_flags.append(word)

    if "http://" in message or "https://" in message:
        red_flags.append("Suspicious Link")

    output_text.delete("1.0", tk.END)

    if len(red_flags) == 0:

        report = """
Threat Level : LOW

No phishing indicators detected.

Status:
Message appears safe.
"""

    elif len(red_flags) <= 3:

        report = f"""
Threat Level : MEDIUM

Red Flags Found:

{chr(10).join('- ' + flag for flag in red_flags)}

Status:
Possible suspicious content detected.
"""

    else:

        report = f"""
Threat Level : HIGH

Red Flags Found:

{chr(10).join('- ' + flag for flag in red_flags)}

Status:
Potential Phishing Attempt Detected.
"""

    output_text.insert(tk.END, report)

def clear_data():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Phishing Awareness Analysis")
root.geometry("750x550")
root.configure(bg="#0f172a")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎣 Phishing Awareness Analysis",
    font=("Segoe UI", 20, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=15)

frame = tk.Frame(
    root,
    bg="#1e293b",
    bd=2
)
frame.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)

input_label = tk.Label(
    frame,
    text="Paste Email / Message",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="white"
)
input_label.pack(pady=(15,5))

input_text = tk.Text(
    frame,
    width=80,
    height=8,
    font=("Consolas", 11)
)
input_text.pack()

button_frame = tk.Frame(
    frame,
    bg="#1e293b"
)
button_frame.pack(pady=15)

analyze_btn = tk.Button(
    button_frame,
    text="Analyze",
    width=15,
    font=("Segoe UI", 11, "bold"),
    bg="#22c55e",
    fg="white",
    command=analyze_message
)
analyze_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=15,
    font=("Segoe UI", 11, "bold"),
    bg="#ef4444",
    fg="white",
    command=clear_data
)
clear_btn.grid(row=0, column=1, padx=10)

output_label = tk.Label(
    frame,
    text="Analysis Report",
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b",
    fg="white"
)
output_label.pack(pady=(10,5))

output_text = tk.Text(
    frame,
    width=80,
    height=10,
    font=("Consolas", 11)
)
output_text.pack()

footer = tk.Label(
    root,
    text="Cyber Security Internship Project | DecodeLabs",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="lightgray"
)
footer.pack(pady=10)

root.mainloop()
