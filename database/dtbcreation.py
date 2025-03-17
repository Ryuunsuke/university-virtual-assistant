import sqlite3

def create_database():
    conn = sqlite3.connect('university_assistant.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id_user INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL,
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


def main():
    create_database()
    print("Database and tables created successfully.")


if __name__ == "__main__":
    main()