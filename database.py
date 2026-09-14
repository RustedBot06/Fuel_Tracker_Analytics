import sqlite3
from pathlib import Path

base_directory=Path(__file__).resolve().parent
#test for update_db, og is "fuel_logs.db" 
db_path=base_directory/"test_logs.db" 

def ini_db():
    mydb = sqlite3.connect(db_path)
    try:
        cur = mydb.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS LOGS (
                ID INTEGER PRIMARY KEY,
                price REAL,
                volume REAL,
                odometer REAL,
                date TEXT,
                is_full INTEGER,
                Fuel_Type TEXT
            )""")
    except sqlite3.DatabaseError as e:
        print("Database error:", e)
    finally:
        mydb.close()

def DBCONNECTOR(querystr, values=()):
    mydb = sqlite3.connect(db_path)

    try:
        cursor = mydb.cursor()

        cursor.execute(querystr, values)

        if querystr.strip().upper().startswith("SELECT"):
            return cursor.fetchall()

        else:
            mydb.commit()
            print("SUCCESSFUL COMMIT")

    except sqlite3.DatabaseError as e:
        print("Database error:", e)

    finally:
        mydb.close()