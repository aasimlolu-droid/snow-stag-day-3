
import sqlite3

db = sqlite3.connect("school_exam.db")
db.execute("PRAGMA foreign_keys = ON")
cur = db.cursor()


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


def view_question():
    qid = int(input("Enter question ID: "))

    cur.execute("SELECT * FROM Questions WHERE question_id = ?", (qid,))
    data = cur.fetchone()

    if data:
        print("Question ID:", data[0])
        print("Question:", data[1])
        print("Subject ID:", data[2])
        print("Teacher ID:", data[3])
        print("Marks:", data[4])
    else:
        print("Question not found.")


def update_question():
    qid = int(input("Enter question ID: "))

    cur.execute("SELECT * FROM Questions WHERE question_id = ?", (qid,))
    data = cur.fetchone()

    if data:
        print("1. Update question text")
        print("2. Update marks")

        choice = input("Enter choice: ")

        if choice == "1":
            new_question = input("Enter new question: ")

            cur.execute("""
            UPDATE Questions
            SET question_text = ?
            WHERE question_id = ?
            """, (new_question, qid))

            db.commit()
            print("Question updated successfully!")

        elif choice == "2":
            new_marks = int(input("Enter new marks: "))

            cur.execute("""
            UPDATE Questions
            SET marks = ?
            WHERE question_id = ?
            """, (new_marks, qid))

            db.commit()
            print("Marks updated successfully!")

        else:
            print("Invalid choice.")

    else:
        print("Question not found.")


def delete_question():
    qid = int(input("Enter question ID: "))

    cur.execute("SELECT * FROM Questions WHERE question_id = ?", (qid,))
    data = cur.fetchone()

    if data:
        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":
            cur.execute("DELETE FROM Questions WHERE question_id = ?", (qid,))
            db.commit()
            print("Question deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Question not found.")


def add_sample_questions():

    cur.execute("SELECT COUNT(*) FROM Questions")
    total = cur.fetchone()[0]

    if total == 0:

        questions = [
            ("What is Python?", 1, 1, 2),
            ("What are variables?", 1, 1, 2),
            ("What is a loop?", 1, 4, 3),
            ("What is a function?", 1, 4, 2),
            ("What is a list in Python?", 1, 1, 3),

            ("What is Artificial Intelligence?", 2, 2, 2),
            ("What is Machine Learning?", 2, 2, 3),
            ("What are neural networks?", 2, 5, 5),
            ("What is deep learning?", 2, 5, 3),
            ("What is an expert system?", 2, 2, 2),

            ("What is a database?", 3, 3, 2),
            ("What is SQL?", 3, 3, 2),
            ("What is a primary key?", 3, 3, 3),
            ("What is a foreign key?", 3, 3, 3),
            ("What is SQLite?", 3, 3, 2)
        ]

        cur.executemany("""
        INSERT INTO Questions
        (question_text, subject_id, teacher_id, marks)
        VALUES (?, ?, ?, ?)
        """, questions)

        db.commit()
        print("Sample questions added!")

    else:
        print("Questions are already available.")


add_sample_questions()

while True:
    print("\n===== Question Management System =====")
    print("1. Add Question")
    print("2. View Question")
    print("3. Update Question")
    print("4. Delete Question")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        view_question()

    elif choice == "3":
        update_question()

    elif choice == "4":
        delete_question()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")

db.close()
