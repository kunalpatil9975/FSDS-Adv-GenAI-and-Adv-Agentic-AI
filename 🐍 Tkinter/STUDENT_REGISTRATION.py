# ============================================================
# STUDENT REGISTRATION SYSTEM USING TKINTER + MYSQL
# ============================================================

# Import Required Libraries
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ============================================================
# DATABASE CONNECTION FUNCTION
# ============================================================

def get_db_connection():
    """
    Create and return MySQL database connection
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Qwerty@123",
        database="webgui"
    )

# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    # Read values from Entry Boxes
    studentname = e2.get()
    coursename = e3.get()
    fee = e4.get()

    # Validate Input
    if studentname == "" or coursename == "" or fee == "":
        messagebox.showerror("Input Error", "All Fields Are Required")
        return

    conn = None

    try:
        # Connect Database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL Query
        sql = "INSERT INTO registration(name,course,fee) VALUES(%s,%s,%s)"

        values = (studentname, coursename, fee)

        # Execute Query
        cursor.execute(sql, values)

        # Save Changes
        conn.commit()

        messagebox.showinfo("Success", "Student Added Successfully")

        # Clear Entry Boxes
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)

        # Refresh Treeview
        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn:
            conn.close()

# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    if not listBox.selection():
        messagebox.showerror("Error", "Select Student")
        return

    studentid = e1.get()
    studentname = e2.get()
    coursename = e3.get()
    fee = e4.get()

    conn = None

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE registration
        SET name=%s, course=%s, fee=%s
        WHERE id=%s
        """

        values = (studentname, coursename, fee, studentid)

        cursor.execute(sql, values)

        conn.commit()

        messagebox.showinfo("Success", "Record Updated")

        e1.config(state="normal")
        e1.delete(0, tk.END)
        e1.config(state="disabled")

        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)

        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn:
            conn.close()

# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    studentid = e1.get()

    if studentid == "":
        messagebox.showerror("Error", "Select Student")
        return

    conn = None

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("DELETE FROM registration WHERE id=%s", (studentid,))

        conn.commit()

        messagebox.showinfo("Success", "Record Deleted")

        e1.config(state="normal")
        e1.delete(0, tk.END)
        e1.config(state="disabled")

        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)

        load_students()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if conn:
            conn.close()

# ============================================================
# LOAD STUDENTS
# ============================================================

def load_students():

    # Remove old records
    for row in listBox.get_children():
        listBox.delete(row)

    conn = None

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM registration")

        rows = cursor.fetchall()

        for row in rows:
            listBox.insert("", tk.END, values=row)

    except mysql.connector.Error as err:

        messagebox.showerror("Database Error", str(err))

    finally:

        if conn:
            conn.close()

# ============================================================
# TREEVIEW SELECT EVENT
# ============================================================

def on_treeview_select(event):

    selected = listBox.selection()

    if selected:

        data = listBox.item(selected)

        sid, name, course, fee = data["values"]

        e1.config(state="normal")
        e1.delete(0, tk.END)
        e1.insert(0, sid)
        e1.config(state="disabled")

        e2.delete(0, tk.END)
        e2.insert(0, name)

        e3.delete(0, tk.END)
        e3.insert(0, course)

        e4.delete(0, tk.END)
        e4.insert(0, fee)

# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Student Registration System")

root.geometry("650x500")

# ============================================================
# LABELS
# ============================================================

tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=10)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)

tk.Label(root, text="Course").grid(row=2, column=0, padx=10, pady=10)

tk.Label(root, text="Fee").grid(row=3, column=0, padx=10, pady=10)

# ============================================================
# ENTRY BOXES
# ============================================================

e1 = tk.Entry(root, state="disabled")
e1.grid(row=0, column=1)

e2 = tk.Entry(root)
e2.grid(row=1, column=1)

e3 = tk.Entry(root)
e3.grid(row=2, column=1)

e4 = tk.Entry(root)
e4.grid(row=3, column=1)

# ============================================================
# BUTTONS
# ============================================================

tk.Button(root, text="Add", width=12, command=add_student).grid(row=4, column=0)

tk.Button(root, text="Update", width=12, command=update_student).grid(row=4, column=1)

tk.Button(root, text="Delete", width=12, command=delete_student).grid(row=4, column=2)

# ============================================================
# TREEVIEW
# ============================================================

cols = ("id", "name", "course", "fee")

listBox = ttk.Treeview(root, columns=cols, show="headings")

listBox.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

for col in cols:
    listBox.heading(col, text=col.upper())
    listBox.column(col, width=150)

# Bind Mouse Click Event
listBox.bind("<ButtonRelease-1>", on_treeview_select)

# Load Existing Records
load_students()

# Start Application
root.mainloop()