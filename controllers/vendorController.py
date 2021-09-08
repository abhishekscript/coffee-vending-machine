from models.vendor import VendorMachine
from services.database import db


def message( code, beverage, ingredient ):
    statusCode= {
        0 : "sufficient",
        1 : "available"
    }
    
    if code is None:
        return f"{beverage} is prepared"
    else:
        return f"{beverage} cannot be prepared because {ingredient} is not {statusCode[code]}"


def add( name, outlet ):
    if type(outlet)!=int:
        raise ValueError("Need int for outlet")

    vendor    = VendorMachine( name, outlet )
    db.vendor = vendor
    print(f"Configured Machine With {outlet} outlets", end="\n")
    

