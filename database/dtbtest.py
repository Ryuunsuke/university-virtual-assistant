import sqlite3

dtb = r"D:\ENV\Ariels\database\university_assistant.db"


def get_all_users():
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users")
    for results in result:
        print(results)
    conn.close()
    return result

def get_user(username):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    result = cursor.execute("SELECT username FROM users WHERE username = ?")

def insert_user(data):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    result = cursor.execute("INSERT INTO users (username, password, email, phone_number) VALUES (%s, %s, %s, %s) RETURNING id;", (data['username'], data['password'], data['email'], data['phone_number']))
    print("Successfully inserted")
    conn.commit()
    conn.close()
    return result

def delete(name):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    
    # Corrected DELETE syntax
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    
    conn.commit()
    conn.close()

def check_user(name):
    conn = sqlite3.connect(dtb)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        print(result[0])
    conn.commit()
    conn.close()
    return result[0] if result else None

get_all_users()
# delete("test")
# check_user('test')