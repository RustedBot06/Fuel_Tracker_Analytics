import matplotlib.pyplot as plt
from mileage import mil
from functions import DBCONNECTOR

def show_graphs():
    listofdates,mileages=mil()
    plt.figure(figsize=(10,8))

    #plot of datevsmil
    plt.subplot(3,1,1)
    plt.plot(listofdates,mileages,marker="o")
    plt.title("Date vs Mileage")
    plt.xlabel("Date")
    plt.ylabel("Mileage")

    clist=DBCONNECTOR("SELECT date FROM LOGS")
    lod=list(date for (date,) in clist)

    #plot of rate vs date
    clist=DBCONNECTOR("SELECT price, volume FROM LOGS")
    listofrate=list(price/volume for price,volume in clist)
    plt.subplot(3,1,2)
    plt.plot(lod,listofrate,marker="o")
    plt.title("Date vs Rate")
    plt.xlabel("Date")
    plt.ylabel("Rate")

    #price vs date
    clist=DBCONNECTOR("SELECT price FROM LOGS")
    listofprc=list(price for (price,) in clist)
    plt.subplot(3,1,3)
    plt.plot(lod,listofprc,marker="o")
    plt.title("Date vs Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.tight_layout()
    plt.gcf().autofmt_xdate()
    plt.show()