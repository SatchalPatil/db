import mysql.connector

# Connect to the database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",     # localhost
        port=3306,            
        user="root",          # Your MySQL username
        password="",          # Your MySQL password
        database="school"     # Your MySQL database
    )

# Add a new record
def add_student(name, class_name, marks):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, class, marks) VALUES (%s, %s, %s)", (name, class_name, marks))
    conn.commit()
    conn.close()
    print(f"Added student: {name}, Class: {class_name}, Marks: {marks}")

# Fetch all records
def fetch_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    conn.close()
    return result

# Update a record
def update_student(student_id, name, class_name, marks):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = %s, class = %s, marks = %s WHERE id = %s", (name, class_name, marks, student_id))
    conn.commit()
    conn.close()
    print(f"Updated student ID {student_id} to {name}, Class: {class_name}, Marks: {marks}")

# Delete a record
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    print(f"Deleted student ID {student_id}")

# Main function to demonstrate the operations
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Add Student")
        print("2. Fetch Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            class_name = input("Enter student class: ")
            marks = float(input("Enter student marks: "))
            add_student(name, class_name, marks)
        elif choice == '2':
            students = fetch_students()
            print("Students:")
            for student in students:
                print(student)
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new student name: ")
            class_name = input("Enter new student class: ")
            marks = float(input("Enter new student marks: "))
            update_student(student_id, name, class_name, marks)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
