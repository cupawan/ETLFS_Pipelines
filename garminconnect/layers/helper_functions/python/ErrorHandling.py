class GarminError(Exception):
    def __init__(self,msg, code):
        print(f"Error {code}: {msg}")
        self.msg = msg
        self.code = code
        
        
class NoRunningError(GarminError):
    def __init__(self, msg="No Running Activity Recorded Yet", code=100):
        super().__init__(msg, code)

class NoSleepError(GarminError):
    def __init__(self, msg="Could Not Fetch Sleep Data", code=200):
        super().__init__(msg, code)
        

class NoBodyStatsError(GarminError):
    def __init__(self, msg="Could Not Fetch Body Statitics", code=200):
        super().__init__(msg, code)