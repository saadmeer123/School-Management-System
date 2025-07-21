import csv
import os

f = 'todo.csv'
file = 'stu.csv'

# Create teacher file if not exist
if not os.path.exists(f):
    with open(f, mode='w', newline='') as l:
        writer = csv.writer(l)
        writer.writerow(['teacher_name', 'teacher_f/name', 'teacher_age', 'teacher_subject', 'teacher_assigned_class'])

# Create student file if not exist
if not os.path.exists(file):
    with open(file, mode='w', newline='') as l:
        writer = csv.writer(l)
        writer.writerow(['student_name', 'student_f/name', 'student_age', 'student_class'])


def login():
    while True:
        username = input("Enter your id name (or 'q' to quit): ")
        pwd = input("Enter your password (or 'q' to quit): ")

        if username == 'admin' and pwd == 'admin123':
            admin_menu()
        elif username == 'student' and pwd == 'student123':
            menu_student()
        elif username == 'q' and pwd == 'q':
            print("Goodbye")
            break
        else:
            print("Please try again")


# Teacher Menu
def admin_menu():
    while True:
        print("---> Welcome to Teacher Section <---")
        print("1. Add Teacher")
        print("2. View Teacher")
        print("3. Search Teacher")
        print("4. Update Teacher")
        print("5. Exit")

        choice = input("Enter your choice -> ")

        if choice == '1':
            add_teacher()
        elif choice == '2':
            view_teacher()
        elif choice == '3':
            search_teacher()
        elif choice == '4':
            update_teacher()
        elif choice == '5':
            print("Goodbye")
            break
        else:
            print("Invalid choice")


def add_teacher():
    teac_name = input("Enter your name -> ")
    teacher_f_name = input("Enter your father's name -> ")
    teac_age = input("Enter your age -> ")
    teac_subject = input("Enter your subject -> ")
    teac_assigned_class = input("Enter your assigned class -> ")

    with open(f, mode='a', newline='') as l:
        writer = csv.writer(l)
        writer.writerow([teac_name, teacher_f_name, teac_age, teac_subject, teac_assigned_class])
        print("Saved successfully")


def view_teacher():
    try:
        with open(f, mode='r') as l:
            reader = csv.reader(l)
            header = next(reader, None)
            for row in reader:
                print(f"Name: {row[0]}, F/Name: {row[1]}, Age: {row[2]}, Subject: {row[3]}, Class: {row[4]}")
    except FileNotFoundError:
        print("No teacher found")
    except Exception as e:
        print('Error:', e)


def search_teacher():
    name = input("Enter name to search -> ")
    found = False

    with open(f, mode='r') as w:
        reader = csv.reader(w)
        next(reader, None)
        for row in reader:
            if row[0].lower() == name.lower():
                print("Found:", row)
                found = True
                break
    if not found:
        print("Not found")


def update_teacher():
    name = input("Enter a name to update -> ")
    updated = False
    all_row = []

    with open(f, mode='r') as l:
        reader = csv.reader(l)
        header = next(reader, None)
        all_row.append(header)

        for row in reader:
            if row[0].lower() == name.lower():
                print('Found:', row)
                print("Give your new data please")
                teac_name = input(f"Enter your name ({row[0]}) -> ") or row[0]
                teacher_f_name = input(f"Enter your father's name ({row[1]}) -> ") or row[1]
                teac_age = input(f"Enter your age ({row[2]}) -> ") or row[2]
                teac_subject = input(f"Enter your subject ({row[3]}) -> ") or row[3]
                teac_assigned_class = input(f"Enter your class ({row[4]}) -> ") or row[4]
                all_row.append([teac_name, teacher_f_name, teac_age, teac_subject, teac_assigned_class])
                updated = True
            else:
                all_row.append(row)

    if updated:
        with open(f, mode='w', newline='') as l:
            writer = csv.writer(l)
            writer.writerows(all_row)
        print("Teacher updated successfully")
    else:
        print("Teacher not found")


# Student Menu
def menu_student():
    while True:
        print("---> Student Section <---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice -> ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            print("Goodbye")
            break
        else:
            print("Invalid choice")


def add_student():
    stu_name = input("Enter your name -> ")
    stu_f_name = input("Enter your father's name -> ")
    stu_age = input("Enter your age -> ")
    stu_class = input("Enter your class -> ")

    with open(file, mode='a', newline='') as w:
        writer = csv.writer(w)
        writer.writerow([stu_name, stu_f_name, stu_age, stu_class])
        print("Student added successfully")


def view_student():
    try:
        with open(file, mode='r') as w:
            reader = csv.reader(w)
            next(reader, None)
            for row in reader:
                print(f"Name: {row[0]}, F/Name: {row[1]}, Age: {row[2]}, Class: {row[3]}")
    except FileNotFoundError:
        print("Student not found")
    except Exception as e:
        print("Error:", e)


def search_student():
    name = input("Enter your name to search -> ")
    found = False

    with open(file, mode='r') as l:
        reader = csv.reader(l)
        next(reader, None)
        for row in reader:
            if row[0].lower() == name.lower():
                print("Found:", row)
                found = True
                break
    if not found:
        print("Not found")


def update_student():
    name = input("Enter student name to update -> ")
    updated = False
    all_rows = []

    with open(file, mode='r') as d:
        reader = csv.reader(d)
        header = next(reader, None)
        all_rows.append(header)

        for row in reader:
            if row[0].lower() == name.lower():
                print("Found:", row)
                print("Enter new data")
                new_name = input(f"Name ({row[0]}) -> ") or row[0]
                new_f_name = input(f"Father's Name ({row[1]}) -> ") or row[1]
                new_age = input(f"Age ({row[2]}) -> ") or row[2]
                new_class = input(f"Class ({row[3]}) -> ") or row[3]
                all_rows.append([new_name, new_f_name, new_age, new_class])
                updated = True
            else:
                all_rows.append(row)

    if updated:
        with open(file, mode='w', newline='') as j:
            writer = csv.writer(j)
            writer.writerows(all_rows)
        print("Updated successfully")
    else:
        print("Not found")


# Start program
login()
