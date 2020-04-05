import sqlite3

def connect():
    conn =sqlite3.connect("diseases.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS diseases (id INTEGER PRIMARY KEY, Symtom1 text, Symtom2 text, Symtom3 integer, isbn integer) ")
    conn.commit()
    conn.close()


def insert(Symtom1, Symtom2, Symtom3, isbn):
    conn =sqlite3.connect("diseases.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO diseases VALUES(NULL, ?,?,?,?)", (Symtom1,Symtom2,Symtom3,isbn))
    conn.commit()
    conn.close()


def view():
    conn =sqlite3.connect("diseases.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM diseases")
    rows =cur.fetchall()
    conn.close()
    return rows

def search(Symtom1="", Symtom2="", Symtom3="", isbn=""):
    conn =sqlite3.connect("diseases.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM diseases WHERE Symtom1=? OR Symtom2=? OR Symtom3=? OR isbn=?",(Symtom1,Symtom2,Symtom3,isbn))
    rows =cur.fetchall()
    conn.close()
    return rows

connect()

