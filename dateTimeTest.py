#!/usr/bin/python

from datetime import datetime, timedelta

#timeFirst = datetime.now()
#print(timeFirst)
#timeSecond = str(datetime.now(timeFirst))
#print(timeSecond)
today = datetime.today()
print(today.strftime('%H:%M on %b %d, %Y'))
