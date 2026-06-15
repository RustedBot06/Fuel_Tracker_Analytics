from datetime import date
import sqlite3
from pathlib import Path

base_directory=Path(__file__).resolve().parent
db_path=base_directory/"log_test.db"  #remember to change to fuel_logs.db after dev 

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
                is_full INTEGER
            )""")
    except sqlite3.DatabaseError as e:
        print("Database error:", e)
    finally:
        mydb.close()

def inpt():
    today=str(date.today())
    price=float(input("Enter total price:"))
    amt=float(input("Enter total vol of fuel filled in litres:"))
    odo=float(input("Enter odometer reading:"))
    isfull=int(input("Enter 1 if full refill, 0 for non full refill: "))
    tupl=(price,amt,odo,today,isfull)
    return tupl

def write(tupl):
    DBCONNECTOR("INSERT INTO LOGS (price, volume, odometer,date, is_full) VALUES (?,?, ?, ?, ?)", tupl)

def print_records(L):
    headers=["ID","Total Price","Litres Filled","Odometer Reading","Date(YYYY-MM-DD)","Is_Full"]
    tuples_list = L

    # 1. Dynamically find the maximum width needed for each column
    widths = [
    max(len(str(val)) for val in col)
    for col in zip(headers, *tuples_list)
    ]

    # 2. Create a dynamic format string based on column widths
    fmt = " | ".join(f"{{:<{w}}}" for w in widths)

    # 3. Print the header row
    print(fmt.format(*headers))

    # 4. Print a decorative separator line
    print("-+-".join("-" * w for w in widths))

    # 5. Print the data rows
    for row in tuples_list:
        print(fmt.format(*row))

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