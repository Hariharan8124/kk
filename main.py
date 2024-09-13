import tkinter as tk
from tkinter import messagebox
import os

def open_student_details():
    os.system('python student_details.py')

def open_take_attendance():
    os.system('python take_attendance.py')

def open_attendance_report():
    os.system('python attendance_report.py')

def open_db():
    os.system('start EXCEL.EXE db.xlsx')

# Create the main window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("600x400")

# Add buttons to the interface
tk.Button(root, text="Student Details", command=open_student_details, width=20, height=2).pack(pady=10)
tk.Button(root, text="Take Attendance", command=open_take_attendance, width=20, height=2).pack(pady=10)
tk.Button(root, text="Attendance Report", command=open_attendance_report, width=20, height=2).pack(pady=10)
tk.Button(root, text="DB", command=open_db, width=20, height=2).pack(pady=10)

root.mainloop()
