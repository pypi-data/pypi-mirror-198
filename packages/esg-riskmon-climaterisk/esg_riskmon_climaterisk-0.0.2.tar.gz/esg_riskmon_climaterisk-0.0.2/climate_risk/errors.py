
class ServiceError(Exception):
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return self.msg
