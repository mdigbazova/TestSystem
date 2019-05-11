import sqlite3

conn = sqlite3.connect('django.db')
c = conn.cursor()

def del_table_todos():
    c.execute('DELETE TABLE todos_todo')
    conn.commit()
    c.close()
    conn.close()