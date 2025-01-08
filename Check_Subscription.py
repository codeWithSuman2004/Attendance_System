import sqlite3
import getmac
from time import strftime
import time
from datetime import datetime,timedelta

def Check_Subscription():
            MAC=getmac.get_mac_address()
            conn=sqlite3.connect(r'C:\ProgramData\Windows Secret Data.db')
            cursor=conn.cursor()
            cursor.execute("SELECT Subscription,Till_Date FROM devicemac WHERE MAC=?",(MAC,))
            Subs_Data=cursor.fetchall()
            a=0
            Subs_Detail=[]
            for i in Subs_Data:
                 Subs_Detail.append(Subs_Data[a])
                 a=a+1      

            Subs_Detail = [item for sublist in Subs_Detail for item in sublist]
            Current_Date=datetime.now()
            
            if datetime.strptime(Subs_Detail[1], '%Y-%m-%d %H:%M:%S.%f') <= Current_Date:
                return False
            else:
                return True
if __name__== "__main__":
    Check_Subscription()
