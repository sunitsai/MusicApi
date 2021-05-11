class Errors:
    def __init__(self, message):
        self.errors = message
    
    def is_valid(self):
        return False