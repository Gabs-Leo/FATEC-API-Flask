import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Discipline
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS discipline (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hours INTEGER NOT NULL
        )
    ''')

    # Course
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Course_Discipline
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course_discipline (
            course_id INTEGER NOT NULL,
            discipline_id INTEGER NOT NULL,
            PRIMARY KEY (course_id, discipline_id),
            FOREIGN KEY (course_id) REFERENCES course (id) ON DELETE CASCADE,
            FOREIGN KEY (discipline_id) REFERENCES discipline (id) ON DELETE CASCADE
        )
    ''')

    # Teacher
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            user TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Teacher_Discipline
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher_discipline (
            teacher_id INTEGER NOT NULL,
            discipline_id INTEGER NOT NULL,
            PRIMARY KEY (teacher_id, discipline_id),
            FOREIGN KEY (teacher_id) REFERENCES teacher (id) ON DELETE CASCADE,
            FOREIGN KEY (discipline_id) REFERENCES discipline (id) ON DELETE CASCADE
        )
    ''')

    # Student
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL,
            password TEXT NOT NULL,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES course (id) ON DELETE SET NULL
        )
    ''')

    print("Database Initialized!")
    conn.commit()
    conn.close()