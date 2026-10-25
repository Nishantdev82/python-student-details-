
import json
import os

FILE_NAME = "students.json"

# Load saved students
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        try:
            students = json.load(file)
        except json.JSONDecodeError:
            students = []
else:
    students = []


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Update Student")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        name = input("Enter student name: ").strip()
        if name == "":
          print("Error! Student name cannot be empty.")
          continue
        roll_no = input("Enter roll number: ").strip()
        
        if roll_no == "":
            print("Error! Roll number cannot be empty.")
            continue

        marks = input("Enter marks: ").strip()
        
        try:
            marks_value = float(marks.replace("%", "").strip())

            if marks_value < 0 or marks_value > 100:
                print("Error! Marks must be between 0 and 100.")
                continue

        except ValueError:
            print("Error! Please enter valid numeric marks.")
            continue

        
        if marks == "":
            print("Error! Marks cannot be empty.")
            continue

        duplicate = False

        for student in students:
            if student["roll_no"].strip() == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Error! This roll number already exists.")
        else:
            student = {
                "name": name,
                "roll_no": roll_no,
                "marks": marks
            }

            students.append(student)

            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)

            print("Student added and saved successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students added yet.")
        else:
            print("\n===== ALL STUDENTS =====")

            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Marks:", student["marks"])
                print("--------------------")

    elif choice == "3":
        print("Thank you for using the program!")
        break

    elif choice == "4":
        search_roll = input("Enter roll number to search: ")

        found = False

        for student in students:
            if student["roll_no"].strip() == search_roll.strip():
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found!")
            
    elif choice == "5":
        delete_roll = input("Enter roll number to delete: ")

        found = False

        for student in students:
            if student["roll_no"].strip() == delete_roll.strip():
                print("Student Found:", student["name"])
                students.remove(student)
                found = True
                break

        if found:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)

            print("Student deleted successfully!")
        else:
            print("Student not found!")
            
    elif choice == "6":
        update_roll = input("Enter roll number to update: ")

        found = False

        for student in students:
            if student["roll_no"].strip() == update_roll.strip():
                print("Student Found:", student["name"])

                new_name = input("Enter new name: ")
                new_marks = input("Enter new marks: ")

                student["name"] = new_name
                student["marks"] = new_marks

                found = True
                break

        if found:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file, indent=4)

            print("Student updated successfully!")
        else:
            print("Student not found!")

    else:
        print("Invalid choice! Please try again.")
