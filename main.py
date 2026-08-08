from functions import *
from stats import *
from graphs import *
from feature import *

ini_db()
while(True):
    print("_______________________________________________________")
    print("-----WELCOME-----")
    print("Choose the from the following")
    count=DBCONNECTOR("SELECT COUNT(*) FROM LOGS")[0][0]
    if count==0:
        print("TABLE HAS NO RECORDS")
        print("0. To Quit")
        print("1. Add log")
    else:
        print("0. To Quit")
        print("1. Add log")
        print("2. View Logs")
        print("3. View stats")
        print("4. Delete Logs")
        print("5. Modify Entry")
        print("6. Backup Data (csv)")
    n=int(input("Enter your choice:"))
    print("_______________________________________________________")

    if n==0:    #To Quit
        break

    elif n==1:  #Add log
        prev_avg=net_avg_mil()
        tupl=inpt()
        if tupl:
            write(tupl)
            entry_summary(prev_avg,tupl)

    elif n==2:  #View Logs
        print("_______________________________________________________")
        print("1. For viewing whole Table.")
        print("2. For viewing logs within date range")
        print("3. For viewing logs within volume of fuel filled range")
        print("4. For viewing logs within price of fuel filled range")
        x=int(input("Enter choice:"))
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        if x==1:
            L=DBCONNECTOR("Select * from LOGS")
            print_records(L)
        elif x==2:
            lowerlim=str(input("Enter older date in format('YYYY-MM-DD') with hyphens:"))
            upperlim=str(input("Enter newer date in format('YYYY-MM-DD') with hyphens:"))
            L=DBCONNECTOR("SELECT * FROM LOGS WHERE date BETWEEN ? AND ?",(lowerlim,upperlim))
            print_records(L)
        elif x==3:
            lowerlim=float(input("Enter lower limit in Litres:"))
            upperlim=float(input("Enter upper limit in Litres:"))
            L=DBCONNECTOR("SELECT * FROM LOGS WHERE volume BETWEEN ? AND ?",(lowerlim,upperlim))
            print_records(L)
        elif x==4:
            lowerlim=float(input("Enter lower limit:"))
            upperlim=float(input("Enter upper limit:"))
            L=DBCONNECTOR("SELECT * FROM LOGS WHERE price BETWEEN (?) AND (?)",(lowerlim,upperlim))
            print_records(L)
        else:
            print("enter a correct choice")
            continue

    elif n==3:  #View stats
        stat_dict={1:("Summary",summary),
                   2:("Mileage", mileage),
                   3:("Total Money Spent ",tot_mon),
                   4:("Average Fuel Price per Litre",avg_prc_perlit),
                   5:("Highest Fuel Price per Litre",highest_fuel_price_perlit),
                   6:("Lowest Fuel Price per Litre",lowest_fuel_price_perlit),
                   7:("View graphs", show_graphs),
                    }
        print("_______________________________________________________")
        for keys,vals in stat_dict.items():
            print(f"{keys}. {vals[0]}")

        x = int(input("Enter choice:"))
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        if x==1:
            stat_dict[1][1](count)
        elif x==2:
            stat_dict[2][1](count)
        elif x!=1 and x!=2 and x in stat_dict:
            stat_dict[x][1]()
        else: print("Invalid Choice")

    elif n==4:  #Delete Logs
        print("_______________________________________________________")
        print("1. For deleting all entries.")
        print("2. For deleting latest entry.")
        x=int(input("Enter choice:"))
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        if x==1:
            DBCONNECTOR("DDELETE FROM LOGS")
            print("-----ALL LOGS DELETED-----")

        elif x==2:
            L=DBCONNECTOR("DELETE FROM LOGS WHERE ID = (SELECT MAX(ID) FROM LOGS)")
            print("Last entry successfuly removed")

    elif n==5:  #Modifying
        id=int(input("Enter ID to modify:"))
        x=int(input("-----------\n1. To modify date\n2. To modify" \
                    "odometer reading\n3. To modify total cost\n4. To modify total fuel filled" \
                    "\nChoose an option:"))
        if x==1:
            new_date=str(input("Enter new date in YYYY-MM-DD(with hyphens):"))
            DBCONNECTOR("UPDATE LOGS SET date = ? WHERE ID = ?",(new_date,id))
        elif x==2:
            od=int(input("Enter new odometer reading:"))
            DBCONNECTOR("UPDATE LOGS SET odometer = ? WHERE ID = ?",(od,id))
        elif x==3:
            new_p=int(input("Enter new total cost:"))
            DBCONNECTOR("UPDATE LOGS SET price = ? WHERE ID = ?",(new_p,id))
        elif x==4:
            new_f=int(input("Enter new total volume of fuel filled:"))
            DBCONNECTOR("UPDATE LOGS SET volume = ? WHERE ID = ?",(new_f,id))
        else:
            print("Enter correct option number")
            continue

    elif n==6:
        backup()

    else:   #break
        print("enter valid option number")
        continue