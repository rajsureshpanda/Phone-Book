import sqlite3

def create_table():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cell_number TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def insert_contact(name, cell_number, email):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO contacts (name, cell_number, email) VALUES (?, ?, ?)
    ''', (name, cell_number, email))
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    conn.close()
    return data

def print_contacts(contacts):
    print("ID\tName\tCell#\tEmail")
    print("-" * 40)
    for contact in contacts:
        print(f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}")

create_table()
insert_contact("Raj Panda", "9856774553", "raj.panda@gmail.com")
insert_contact("Jane Smith", "7968725678", "jane.smith@gmail.com")
insert_contact("Nidhi Gupta", "6368725678", "nidhi.gupta@gmail.com")
insert_contact("Jake White", "8468725678", "jake.white@gmail.com")
insert_contact("Vikram Jay", "9568725676", "vikram.jay@gmail.com")

contacts = fetch_contacts()
print_contacts(contacts)