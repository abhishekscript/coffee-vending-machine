from datetime import datetime
from enum import Enum

class State:
    HOT   =  0
    COLD  =  1 


class Ingredient:
    def __init__(self, name, totalQty):
        self.name      = name
        self.totalQty  = totalQty
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
    

class Beverage:
    def __init__(self, name):
        self.name      = name
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()


class Recipe:
    def __init__(self, beverage, ingredient, qty):
        self.beverage   = beverage
        self.ingredient = ingredient
        self.qty        = qty
        self.createdAt  = datetime.now()
        self.updatedAt  = datetime.now()
    
    def __repr__(self):
        return f'{self.__dict__}'


