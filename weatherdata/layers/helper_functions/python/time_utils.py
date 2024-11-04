import datetime
import pytz

class TimeUtils():
    def __init__(self):
        self.ist = pytz.timezone('Asia/Kolkata')

    def timestamp_to_date(self, timestamp):
        utc_dt = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
        ist_dt = utc_dt.astimezone(self.ist)
        return ist_dt.strftime('%A, %d %b %Y')

    def timestamp_to_time(self, timestamp):
        utc_dt = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
        ist_dt = utc_dt.astimezone(self.ist)
        return ist_dt.strftime('%I:%M %p')

    def timestamp_to_datetime(self, timestamp):
        utc_dt = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
        ist_dt = utc_dt.astimezone(self.ist)
        return ist_dt.strftime('%b %d %I:%M %p')