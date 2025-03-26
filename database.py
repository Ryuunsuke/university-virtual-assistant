import sqlite3

dtb = "database/university_assistant.db"

def create_database():
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id_user INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL,
                        admin INTEGER NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id_course INTEGER PRIMARY KEY,
                        course_name TEXT NOT NULL,
                        instructor TEXT NOT NULL,
                        schedule DATE NOT NULL,
                        class_num TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
                        id_assignment INTEGER PRIMARY KEY,
                        course_id INTEGER,
                        title TEXT NOT NULL,
                        due_date DATE NOT NULL,
                        FOREIGN KEY(course_id) REFERENCES courses(id_course)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                        id_event INTEGER PRIMARY KEY,
                        event_name TEXT NOT NULL,
                        event_date DATE NOT NULL,
                        event_time TIME NOT NULL,
                        location TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

create_database()

def check_user(name):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result[0] if result else None

def check_pass(name):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result[0] if result else None

def register(name, password, email, admin):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, password, email, admin) VALUES (?, ?, ?, ?)',
                   (name, password, email, admin))  # Corrected order
    conn.commit()
    conn.close()