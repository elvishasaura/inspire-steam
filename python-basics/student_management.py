import tkinter as tk
from tkinter import messagebox, filedialog

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("600x500")

        self.students = []

        # Labels and Entries
        tk.Label(root, text="Student ID").pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        tk.Label(root, text="First Name").pack()
        self.first_name_entry = tk.Entry(root)
        self.first_name_entry.pack()

        tk.Label(root, text="Last Name").pack()
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.pack()

        tk.Label(root, text="Phone Number").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        tk.Label(root, text="Courses (comma separated)").pack()
        self.courses_entry = tk.Entry(root)
        self.courses_entry.pack()

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_student, bg="green", fg="white").pack(pady=5)
        tk.Button(root, text="Export to Text File", command=self.export_students, bg="blue", fg="white").pack(pady=5)
        tk.Button(root, text="Clear Fields", command=self.clear_fields, bg="red", fg="white").pack(pady=5)

        # Display area
        tk.Label(root, text="Students List").pack()
        self.display_box = tk.Text(root, height=10, width=70)
        self.display_box.pack()

    def add_student(self):
        student_id = self.id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone = self.phone_entry.get()
        courses = self.courses_entry.get()

        if not student_id or not first_name or not last_name or not phone or not courses:
            messagebox.showerror("Error", "All fields are required!")
            return

        student = {
            "id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "courses": courses.split(",")
        }

        self.students.append(student)
        self.display_students()
        self.clear_fields()

        messagebox.showinfo("Success", "Student added successfully!")

    def display_students(self):
        self.display_box.delete(1.0, tk.END)
        for student in self.students:
            self.display_box.insert(tk.END,
                f"ID: {student['id']} | "
                f"Name: {student['first_name']} {student['last_name']} | "
                f"Phone: {student['phone']} | "
                f"Courses: {', '.join(student['courses'])}\n"
            )

    def export_students(self):
        if not self.students:
            messagebox.showwarning("Warning", "No students to export!")
            return

        file = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if file:
            for student in self.students:
                file.write(
                    f"ID: {student['id']}\n"
                    f"First Name: {student['first_name']}\n"
                    f"Last Name: {student['last_name']}\n"
                    f"Phone: {student['phone']}\n"
                    f"Courses: {', '.join(student['courses'])}\n"
                    "--------------------------\n"
                )
            file.close()
            messagebox.showinfo("Success", "Students exported successfully!")

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.courses_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()