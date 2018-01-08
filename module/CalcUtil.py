
import datetime




def checkIfPastSpecificTimeInSec(lastTime, currentTime ,pastTimeInSec):
    """前に通知した時間よりも５分(5*60)以上たっているか判定する"""

    #lastNotifiedTime =datetime.datetime(2017, 12, 28, 22, 5, 6, 620836)

    #currentTime=datetime.datetime.now()

    diff = currentTime-lastTime
    print(diff.seconds)

    if diff.seconds > pastTimeInSec:
        return True
    else:
        return False
    
    #return True
    #print(dif.seconds)


#配列の中で今の温度よりも0.5度以上高いデータが無いか調べる
def checkIfHigerValueExist(tempArray, currentTemp):
    if max(tempArray) >= currentTemp+0.5:
        return True
    else:
        return False



#配列の中で今の温度よりも0.5度以上低いデータが無いか調べる
def checkIfLowerValueExist(tempArray, currentTemp):
    if min(tempArray) <= currentTemp-0.5:
        return True
    else:
        return False
