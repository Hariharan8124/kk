import cv2
import pandas as pd
import os

# Load student details from Excel
db_path = r'C:\Users\harih\OneDrive\Desktop\Face_Recognition_Attendance_System\db.xlsx'
df = pd.read_excel(db_path)

# Capture video feed
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

attended_students = []

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_img = frame[y:y+h, x:x+w]

        # Implement face recognition logic here (using a pre-trained model or OpenCV matching)
        # For simplicity, assume face_img matches if found in db.xlsx (this needs a proper model for real use)
        for _, row in df.iterrows():
            stored_image = cv2.imread(row['PhotoPath'])

            # Dummy match condition (real project should use face recognition model)
            if stored_image is not None:  # Replace with a matching function
                attended_students.append(row['RegNo'])

    cv2.imshow('Attendance Capture', frame)

    # Stop capturing when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()

# Save attendance report
attendance_report_path = r'C:\Users\harih\OneDrive\Desktop\Face_Recognition_Attendance_System\attendance_report.xlsx'
attendance_df = pd.DataFrame({'RegNo': attended_students})
attendance_df = attendance_df.drop_duplicates()
attendance_df.to_excel(attendance_report_path, index=False)

print("Attendance recorded successfully!")
