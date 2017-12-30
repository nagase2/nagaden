import numpy as np
import datetime


list = []
list.append(3)
list.append(5)
list.append(7)
list.append(8)

list.pop(0)
print(list)


nmlist = np.asarray(list)
#nmlist = np.append(nmlist,[39,98])

print(nmlist)
print(np.average(nmlist))



#前に通知した時間よりも５分(5*60)以上たっているか
lastNotifiedTime =datetime.datetime(2017, 12, 28, 22, 5, 6, 620836)

currentTime=datetime.datetime.now()

dif = currentTime- lastNotifiedTime

print(dif.seconds)