from functions import DBCONNECTOR

def mil():
    qrylist=DBCONNECTOR("SELECT ID,odometer,date FROM LOGS WHERE is_full=1 ORDER BY ID")
    listofvol=[]
    listofodo=[]
    mileages=[]
    listofdates=[]  
    if qrylist and len(qrylist)>=2:
        for i in range(len(qrylist)-1):
            lowerlim=qrylist[i][0]
            higherlim=qrylist[i+1][0]
            vals=DBCONNECTOR("SELECT SUM(volume) FROM LOGS WHERE ID>? AND ID<=?", (lowerlim,higherlim))
            listofvol+=[val for (val,) in vals]
            listofodo.append(qrylist[i+1][1]-qrylist[i][1])

        mileages+=[dist/fuel for fuel,dist in zip(listofvol,listofodo) if fuel!=0]

        for i in range(1,len(qrylist)):
            listofdates.append(qrylist[i][2])

    return listofdates,mileages
#mil per refill
def date_mil():
    listofdates,mileages = mil()
    if len(listofdates)!=0: return list(zip(listofdates,mileages))
    else: return "Sufficient Data Unavailable"
    
def net_avg_mil():
    listofdates,mileages = mil()
    if len(mileages)>=1:
        return sum(mileages)/len(mileages)
    else:
        return "Sufficient Data Unavailable"