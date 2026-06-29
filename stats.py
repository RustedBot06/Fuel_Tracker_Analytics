from functions import DBCONNECTOR
from mileage import date_mil,net_avg_mil
#graph has sep file

def mileage(x):
    if x>=2:
        mil_menu={1:("For Mileage per refill and date",date_mil),
            2:("For Net Average Mileage till last log",net_avg_mil)}
        for keys,vals in mil_menu.items():
            print(f"{keys}. {vals[0]}")
        x = int(input("Enter choice:"))
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print(mil_menu[x][1]())
    else: print("Data Insufficient for Mileage Calculations")

def tot_mon():
    tot_prc=DBCONNECTOR("SELECT SUM(price) FROM LOGS")
    for _ in tot_prc:
        print(_[0])
    
def tot_fuel():
    tot_fu=DBCONNECTOR("SELECT SUM(volume) FROM LOGS")
    for _ in tot_fu:
        print(_[0])

def no_refu():
    refu=DBCONNECTOR("SELECT COUNT(*) FROM LOGS")
    for _ in refu:
        print(_[0])

def avg_prc_perlit():
    avgprc=DBCONNECTOR("SELECT AVG(price/volume) FROM LOGS")
    for _ in avgprc:
        print(_[0])
    
def highest_fuel_price_perlit():
    hipl=DBCONNECTOR("SELECT MAX(price/volume) FROM LOGS")
    for _ in hipl:
        print(_[0])

def lowest_fuel_price_perlit():
    lipl=DBCONNECTOR("SELECT MIN(price/volume) FROM LOGS")
    for _ in lipl:
        print(_[0])

def tot_dist():
    x=DBCONNECTOR("SELECT MAX(odometer)-MIN(odometer) FROM LOGS")
    if x[0][0]==0.0: print("Not enough data")
    else: print(x[0][0])

def avg_refu_prc():
    x=DBCONNECTOR("SELECT AVG(price) FROM LOGS")
    print(x[0][0])