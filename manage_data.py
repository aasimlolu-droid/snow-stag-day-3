
import sqlite3

# connecting to database
db = sqlite3.connect("school_exam.db")
db.execute("PRAGMA foreign_keys = ON")
cur = db.cursor()


# 1. function to add a teacher
def add_teacher():
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    email = input("Enter email: ")

    cur.execute("""
    INSERT INTO Teachers (teacher_name, subject, email)
    VALUES (?, ?, ?)
    """, (name, subject, email))

    db.commit()
    print("Teacher added successfully!")


# 2. function to add a subject
def add_subject():
    name = input("Enter subject name: ")

    cur.execute("""
    INSERT INTO Subjects (subject_name)
    VALUES (?)
    """, (name,))

    db.commit()
    print("Subject added successfully!")


# 3. function to add a question
def add_question():
    question = input("Enter question: ")
    subject_id = int(input("Enter subject ID: "))
    teacher_id = int(input("Enter teacher ID: "))
    marks = int(input("Enter marks: "))

    cur.execute("""
    INSERT INTO Questions
    (question_text, subject_id, teacher_id, marks)
    VALUES (?, ?, ?, ?)
    """, (question, subject_id, teacher_id, marks))

    db.commit()
    print("Question added successfully!")


# 4. display all teachers
def show_teachers():
    cur.execute("SELECT * FROM Teachers")
    data = cur.fetchall()

    print("\nRegistered Teachers:")

    for teacher in data:
        print(teacher)


# 5. display all subjects
def show_subjects():
    cur.execute("SELECT * FROM Subjects")
    data = cur.fetchall()

    print("\nAvailable Subjects:")

    for subject in data:
        print(subject)


# 6. display all questions
def show_questions():
    cur.execute("""
    SELECT Questions.question_id, Questions.question_text,
           Subjects.subject_name, Teachers.teacher_name,
           Questions.marks
    FROM Questions
    JOIN Subjects ON Questions.subject_id = Subjects.subject_id
    JOIN Teachers ON Questions.teacher_id = Teachers.teacher_id
    """)

    data = cur.fetchall()

    print("\nAll Questions:")

    for question in data:
        print(question)


# 7. search questions by subject
def search_by_subject():
    name = input("Enter subject name: ")

    cur.execute("""
    SELECT Questions.question_text, Teachers.teacher_name,
           Questions.marks
    FROM Questions
    JOIN Subjects ON Questions.subject_id = Subjects.subject_id
    JOIN Teachers ON Questions.teacher_id = Teachers.teacher_id
    WHERE Subjects.subject_name = ?
    """, (name,))

    data = cur.fetchall()

    if data:
        print("\nQuestions for", name)

        for question in data:
            print(question)
    else:
        print("No questions found for this subject.")


# 8. search questions by teacher
def search_by_teacher():
    name = input("Enter teacher name: ")

    cur.execute("""
    SELECT Questions.question_text, Subjects.subject_name,
           Questions.marks
    FROM Questions
    JOIN Subjects ON Questions.subject_id = Subjects.subject_id
    JOIN Teachers ON Questions.teacher_id = Teachers.teacher_id
    WHERE Teachers.teacher_name = ?
    """, (name,))

    data = cur.fetchall()

    if data:
        print("\nQuestions submitted by", name)

        for question in data:
            print(question)
    else:
        print("No questions found for this teacher.")


# inserting sample data
def insert_sample_data():

    cur.execute("SELECT COUNT(*) FROM Teachers")
    result = cur.fetchone()

    # checking if sample data is already inserted
    if result[0] == 0:

        teachers = [
            ("Ahmad Dar", "Python", "ahmad@gmail.com"),
            ("Sahil Khan", "Artificial Intelligence", "sahil@gmail.com"),
            ("Riya Sharma", "Database Management", "riya@gmail.com"),
            ("Adil Ahmad", "Python", "adil@gmail.com"),
            ("Zoya Jan", "Artificial Intelligence", "zoya@gmail.com")
        ]

        cur.executemany("""
        INSERT INTO Teachers (teacher_name, subject, email)
        VALUES (?, ?, ?)
        """, teachers)

        subjects = [
            ("Python",),
            ("Artificial Intelligence",),
            ("Database Management",)
        ]

        cur.executemany("""
        INSERT INTO Subjects (subject_name)
        VALUES (?)
        """, subjects)

        questions = [
            # Python questions
            ("What is Python?", 1, 1, 2),
            ("What are variables in Python?", 1, 1, 2),
            ("Explain Python loops.", 1, 4, 5),
            ("What is a function?", 1, 4, 2),
            ("What is a list?", 1, 1, 2),
            ("Explain tuples in Python.", 1, 4, 3),
            ("What is a dictionary?", 1, 1, 3),
            ("What is the use of if-else?", 1, 4, 2),
            ("Explain the range function.", 1, 1, 3),
            ("What is a Python module?", 1, 4, 5),

            # Artificial Intelligence questions
            ("What is Artificial Intelligence?", 2, 2, 2),
            ("What is Machine Learning?", 2, 2, 3),
            ("Explain neural networks.", 2, 5, 5),
            ("What is deep learning?", 2, 5, 3),
            ("What is an expert system?", 2, 2, 2),
            ("Explain natural language processing.", 2, 5, 5),
            ("What is computer vision?", 2, 2, 3),
            ("Explain supervised learning.", 2, 5, 3),
            ("What is an intelligent agent?", 2, 2, 2),
            ("Explain reinforcement learning.", 2, 5, 5),

            # Database Management questions
            ("What is a database?", 3, 3, 2),
            ("What is SQL?", 3, 3, 2),
            ("Explain primary key.", 3, 3, 3),
            ("What is a foreign key?", 3, 3, 3),
            ("What is a database table?", 3, 3, 2),
            ("Explain database relationships.", 3, 3, 5),
            ("What is SQLite?", 3, 3, 2),
            ("What is a SQL query?", 3, 3, 3),
            ("Explain the SELECT command.", 3, 3, 3),
            ("What is data redundancy?", 3, 3, 5)
        ]

        cur.executemany("""
        INSERT INTO Questions
        (question_text, subject_id, teacher_id, marks)
        VALUES (?, ?, ?, ?)
        """, questions)

        db.commit()

        print("Sample data inserted successfully!")

    else:
        print("Sample data is already available.")


# main program
insert_sample_data()

while True:

    print("\n===== School Examination System =====")
    print("1. Add Teacher")
    print("2. Add Subject")
    print("3. Add Question")
    print("4. Display Teachers")
    print("5. Display Subjects")
    print("6. Display Questions")
    print("7. Search Questions by Subject")
    print("8. Search Questions by Teacher")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_teacher()

    elif choice == "2":
        add_subject()

    elif choice == "3":
        add_question()

    elif choice == "4":
        show_teachers()

    elif choice == "5":
        show_subjects()

    elif choice == "6":
        show_questions()

    elif choice == "7":
        search_by_subject()

    elif choice == "8":
        search_by_teacher()

    elif choice == "9":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")


# closing database
db.close()
