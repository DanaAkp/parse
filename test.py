import datetime


time1 = datetime.datetime(122, 1, 1, 10, 30)
time2 = datetime.datetime(122, 1, 1, 11, 30)

dt = time2-time1
dt2 = datetime.datetime(122, 1, 2, 23, 30)
print(dt2 + dt)

print(dt2 - time2)
