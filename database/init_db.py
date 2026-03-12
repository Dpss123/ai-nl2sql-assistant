import sqlite3
from config.settings import DB_PATH

def init_db():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks INTEGER,
        department TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments(
        dept_code TEXT PRIMARY KEY,
        dept_name TEXT,
        hod TEXT,
        building TEXT
    )
    """)

    cursor.execute("DELETE FROM students")
    cursor.execute("DELETE FROM departments")

    students = [
        (1,"Rahul",20,85,"CSE"),
        (2,"Anita",21,92,"ECE"),
        (3,"Aman",19,78,"ME"),
        (4,"Sneha",22,88,"CSE"),
        (5,"Rohit",20,65,"CE")
    ]

    departments = [
        ("CSE","Computer Science Engineering","Dr. Sharma","Block A"),
        ("ECE","Electronics & Communication","Dr. Verma","Block B"),
        ("ME","Mechanical Engineering","Dr. Singh","Block C"),
        ("CE","Civil Engineering","Dr. Gupta","Block D")
    ]

    cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?)", students)
    cursor.executemany("INSERT INTO departments VALUES (?,?,?,?)", departments)

    conn.commit()
    conn.close()