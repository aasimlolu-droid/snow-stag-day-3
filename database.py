
import sqlite3
db = sqlite3.connect("school_exam.db")
cur = db.cursor()

CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT,
    subject TEXT,
    email TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT
)
""")

# creating questions table
cur.execute("""
CREATE TABLE IF NOT EXISTS Questions (
    question_id INTEGER PRIMARY KEY,
    question_text TEXT,
    subject_id INTEGER,
    teacher_id INTEGER,
    marks INTEGER,
    FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id),
    FOREIGN KEY(teacher_id) REFERENCES Teachers(teacher_id)
)
""")

# saving changes
db.commit()

print("Database created successfully")
print("Teachers table created")
print("Subjects table created")
print("Questions table created")

# closing database
db.close()
