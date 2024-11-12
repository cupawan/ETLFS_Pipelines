class StravaError(Exception):
    def __init__(self,msg, code):
        print(f"Error {code}: {msg}")
        self.msg = msg
        self.code = code
        
        
class NoDataError(StravaError):
    def __init__(self, msg="", code=404):
        super().__init__(msg, code)
        
class LoginError(StravaError):
    def __init__(self, msg="", code=401):
        super().__init__(msg, code)