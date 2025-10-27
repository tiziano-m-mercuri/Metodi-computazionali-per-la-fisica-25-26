from datetime import datetime, timedelta
import numpy as np
datenow=datetime.now()
mydatehr_str=input("Quando sei nato? ")
mydatehr=datetime.strptime(mydatehr_str, "%d-%m-%Y %H:%M:%S")
timediff=datenow-mydatehr
toty=timediff.total_seconds()/(3600*24*365)
totd=timediff.total_seconds()/(3600*24)
tots=timediff.total_seconds()
print("Anni trascorsi: ", toty)
print("Giorni trascorsi: ", totd)
print("Secondi trascorsi: ", tots)

