import datetime

class CommonUtils:
    def __init__(self):
        pass
    
    def seconds_to_hm(self, n_seconds):
        hours = n_seconds // 3600
        minutes = (n_seconds % 3600) // 60
        if hours != 0 and minutes != 0:
            return f"{int(hours)} Hours {int(minutes)} Minutes"
        elif hours == 0:
            return f"{int(minutes)} Minutes"
        elif minutes == 0:
            return f"{int(hours)} Hours"
        else:
            return f"{int(n_seconds)} seconds"
    
    def convert_speed_mps_to_minkm(self,speed_mps):
        mps_to_kph = 3.6
        speed_kph = speed_mps * mps_to_kph
        if speed_kph != 0:
            min_per_km = 60 / speed_kph
        else:
            min_per_km = float('inf')
        seconds = min_per_km * 60
        mins = seconds // 60
        secs = seconds % 60
        return f"{int(mins)}'{int(secs)}\""
        
    def convert_str_time(self, duration):
        duration = str(duration)
        hours, minutes, seconds = map(int, duration.split(":"))
        out = ''''''
        if hours > 0:
            out += f"{hours} Hour " if hours == 1 else f"{hours} Hours "
        if minutes > 0:
            out += f"{minutes} Min " if minutes == 1 else  f"{minutes} Mins "
        if seconds > 0:
            out += f"{seconds} Second " if seconds == 1 else f"{seconds} Seconds "
        return out.strip()
    
    def write_status_file(self):
        with open("/tmp/Garmin_Statistics_Status.txt", "w") as f:
            data = f"{datetime.datetime.today().strftime('%d/%m/%y')}: done"
            f.write(data)
        return True