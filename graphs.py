import matplotlib.pyplot as plt
from mileage import mil
from functions import DBCONNECTOR

def show_graphs():
    clist=DBCONNECTOR("SELECT date FROM LOGS")
    lod=list(date for (date,) in clist)
    listofdates,mileages=mil()
    plt.figure(figsize=(10,8))

    #plot of datevsmil
    plt.subplot(3,1,1)
    x = range(len(lod))
    plt.stairs(values=mileages, edges=x, fill=True)
    plt.xticks(x, lod, rotation=45)
    plt.title("Interval vs Mileage")
    plt.xlabel("Interval")
    plt.ylabel("Mileage")
    plt.grid(axis="y",which="both", linestyle= "--")
    for i, y in enumerate(mileages):
        plt.text(i + 0.5, y, f"{y:.1f}")

    #plot of rate vs date
    clist=DBCONNECTOR("SELECT price, volume FROM LOGS")
    listofrate=list(price/volume for price,volume in clist)
    plt.subplot(3,1,2)
    plt.plot(lod,listofrate,marker="o")
    plt.title("Date vs Rate")
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.xticks(rotation=45)
    plt.grid(axis="y",which="both", linestyle= "--")
    for x, y in zip(lod, listofrate):
        plt.text(x, y, f"{y:.1f}")

    #price vs date
    clist=DBCONNECTOR("SELECT price FROM LOGS")
    listofprc=list(price for (price,) in clist)
    plt.subplot(3,1,3)
    plt.plot(lod,listofprc,marker="o")
    plt.title("Date vs Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(axis="y",which="both", linestyle= "--")
    for x, y in zip(lod, listofprc):
        plt.text(x, y, f"{y:.1f}")

    plt.tight_layout()
    plt.gcf().autofmt_xdate()
    plt.show()