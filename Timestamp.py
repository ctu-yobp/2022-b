from datetime import datetime, time
import calendar

class TimestampsClass:
    def Time(self):
        now = datetime.utcnow()
        dates = now.strftime("%Y-%m-%d %H:%M:%S")
        unixtime = calendar.timegm(now.utctimetuple())
        return dates, unixtime

