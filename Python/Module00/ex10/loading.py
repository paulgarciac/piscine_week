import time
import sys

start = time.time()

def ft_progress(lst):
    n = 0
    for n in lst:
        n += 1
        yield n
        
TotCalculs = 1000
listy = range(TotCalculs)

ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    pourcentage = round(elem/TotCalculs*100, 1)
    timePassed = round(time.time() - start, 1)
    ETA = round(timePassed/(pourcentage/100) - timePassed)
    nbTiret = round(pourcentage/10)

    print(" ETA: " + str(ETA) + "s " + 
    "[" + str(pourcentage) + "%] [" + nbTiret * "=" + ">" + (10 - nbTiret) * " " + "] " +
     str(elem) + "/" + str(TotCalculs) + 
     " | elapsed time " + str(timePassed) + 's', 
     sep = "", end = f"\r", flush = True)
    time.sleep(0.005)



