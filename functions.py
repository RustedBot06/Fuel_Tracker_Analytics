from datetime import date
from validation import *
from database import *
from settings import *
import csv

def dispdefault():
    print("Default Fuel Type:",DEFAULT_FUEL)

def changedefault(): #Not currently implemented anywhere as of 14.9.26
    DEFAULT_FUEL=input("Please enter new default Fuel Type:")
    return DEFAULT_FUEL

def inpt():
    try:
        today=str(date.today())
        price=float(input("Enter total price:"))
        validate_price(price)
        amt=float(input("Enter total vol of fuel filled in litres:"))
        validate_amount(amt)
        odo=float(input("Enter odometer reading:"))
        prev_odo=DBCONNECTOR("SELECT odometer FROM LOGS WHERE ID = (SELECT MAX(ID) FROM LOGS)")
        validate_odometer(odo, prev_odo[0][0] if prev_odo else 0)
        isfull=int(input("Enter 1 if full refill, 0 for non full refill: "))
        validate_full_refill_flag(isfull)
        fuel_type=str(input("Click Enter to continue with default fuel type, else enter the fuel type:"))
        if fuel_type=='': fuel_type=DEFAULT_FUEL
        tupl=(price,amt,odo,today,isfull,fuel_type)
        return tupl
    except ValueError:
        print("Enter valid numeric input")
    except ValidationError as e:
        print(f"Validation Error: {e}")

def write(tupl):
    DBCONNECTOR("INSERT INTO LOGS (price, volume, odometer,date, is_full, Fuel_Type) VALUES (?,?, ?, ?, ?,?)", tupl)

def print_records(L):
    headers=["ID","Total Price","Litres Filled","Odometer Reading","Date(YYYY-MM-DD)","Is_Full","Fuel_Type"]
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

def backup():
    with open("Latest_Back.csv","w", newline=" ") as fout:
        writerObj=csv.writer(fout)
        header=['ID','Total Price','Volume Refueled','Odometer Reading','Date(YYYY-MM-DD)','Full tank refill(1=yes)']
        writerObj.writerow(header)
        data=[list(t) for t in DBCONNECTOR("SELECT * FROM LOGS")]
        writerObj.writerows(data)
    print("BackUp csv created")
