from services.database import db
from models.item import Beverage, Recipe, Ingredient

def addBeverage(name):
    beverage = Beverage(name)
    if beverage in db.beverages:
        #print(f"{name} already exists")
        return
    db.beverages.append( beverage )
    return id(beverage)

def getAllBeverages():
    if db.beverages == []:
        print("No Beverages Added")
        return 
    return db.beverages

def getBeverage(name):
    for beverage in db.beverages:
        if beverage.name == name:
            return beverage
    return None

def addIngredient(name, totalQty):
    
    if name not in db.ingredients:
        ingredient = Ingredient(name, totalQty)
        db.ingredients[ name ] = ingredient
    else:
        db.ingredients[ name ].totalQty += totalQty 

def getAllIngredient():
    ingredientRecord = db.ingredients
    for ingredient in ingredientRecord:
        print("Name     : ", ingredientRecord[ingredient].name)
        print("Qty      : ", ingredientRecord[ingredient].totalQty)
        print("Added On : ", ingredientRecord[ingredient].createdAt)
    print("\n")
def getIngredient(name):
    
    if name not in db.ingredients:
        return None
    
    return id( db.ingredients[name] )

'''
Prepare Beverage Logic
'''
def prepareBeverage(beverageId, ingredientId, qty):
 
    if ingredientId==None:
        return 1
    
    # Fetch Ingredient , Check If Exists In Sufficient Quantity
    result = [db.ingredients[x] for x in db.ingredients if id(db.ingredients[x]) == ingredientId ]
    ingredientRecord = result[0]
    if ingredientRecord.totalQty - qty < 0:
        return 0

    # Update Stock Quantity If They Are Being Consumed
    ingredientRecord.totalQty-=qty
    receipe = Recipe( beverageId, ingredientId,  qty)
    
    # Store In DB
    if beverageId not in db.beverageRecipe:
        db.beverageRecipe[ beverageId ] = []
    db.beverageRecipe[beverageId].append( receipe )
    return

