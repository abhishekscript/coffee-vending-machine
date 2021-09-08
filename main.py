import json
from services.database import db
from json.decoder import JSONDecodeError
from controllers import itemController, vendorController



def main(inputData):
    
    data        = inputData["machine"]
    outlet      = data.get('outlets')
    outletCount = outlet.get("count_n")
    vendorController.add(
        data.get("name", "CoffeeMachine"),
        outletCount
    )
    
    totalItems = data.get("total_items_quantity")

    for item in totalItems:
        itemController.addIngredient(item, totalItems[item] )

    # Get All Stock Information
    itemController.getAllIngredient()

    
    beverages = data.get("beverages")
    for item in beverages:
        beverage   = itemController.addBeverage(item)
        for ingredient in beverages[item]:
            qty = beverages[item][ingredient]
            ingredientId = itemController.getIngredient(ingredient)
            code = itemController.prepareBeverage( beverage, ingredientId, qty)
            if code!=None:
                break
        
        print( vendorController.message( code, item, ingredient ), end="\n\n" )



if __name__ == "__main__":
    inputData = {}
    with open("tests/baseCase.json", encoding='utf-8') as inpFile:
        try:
            inputData = json.loads(inpFile.read())
        except JSONDecodeError as e:
            print("Invalid JSON File")
            exit()
        
        main(inputData)
    






