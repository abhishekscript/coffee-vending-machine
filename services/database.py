'''
In Memory Database Entity
'''
class Database:
    def __init__(self):
        self.vendor         = None
        self.beverages      = []
        self.ingredients    = {}
        self.beverageRecipe = {}

db = Database()
# Singleton Pattern