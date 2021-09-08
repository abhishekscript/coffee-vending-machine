from datetime import datetime

class VendorMachine:
    def __init__(self, name, outlet):
        self.name      = name  
        self.outlet    = outlet
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()

