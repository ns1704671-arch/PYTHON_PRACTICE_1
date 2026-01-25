import calendar
yy = 1982 # year
mm = 8    # month
# display the calendar
print(calendar.month(yy, mm))
import datetime
now = datetime.datetime.now()
print(now)
import time
sec = int(input("kitne second baad alarm: "))
time.sleep(sec)
print("Alarm bje gya!")