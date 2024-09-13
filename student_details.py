import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import os

# Excel file setup
db_path = r'C:\Users\harih\OneDrive\Desktop\Face_Recognition_Attendance_System\db.xlsx'

# Create an empty Excel file if it doesn't exist
if not os.path.exists(db_path):
    df = pd.DataFrame(columns=['Name', 'RegNo', 'PhotoPath'])
    df.to_excel(db_path, index=False)

def submit_details():
    name = name_entry.get()
    regno = regno_entry.get()
    photo_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if not name or not regno or not photo_path:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    # Save student details to Excel
    df = pd.read_excel(db_path)
    df = df.append({'Name': name, 'RegNo': regno, 'PhotoPath': photo_path}, ignore_index=True)
    df.to_excel(db_path, index=False)

    # Save photo in images folder
    if not os.path.exists('images'):
        os.makedirs('images')
    img = Image.open(photo_path)
    img.save(f'images/{regno}.jpg')

    messagebox.showinfo("Success", "Student details submitted successfully!")
    name_entry.delete(0, tk.END)
    regno_entry.delete(0, tk.END)

# Create GUI
root = tk.Tk()
root.title("Student Details")
root.geometry("400x300")

tk.Label(root, text="Name of Student").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="RegNo of Student").pack(pady=5)
regno_entry = tk.Entry(root)
regno_entry.pack(pady=5)

tk.Button(root, text="Upload Photo & Submit", command=submit_details).pack(pady=20)

root.mainloop()
