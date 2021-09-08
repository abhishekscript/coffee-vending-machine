import json, unittest
import main as driver

class TestVendorMachine(unittest.TestCase):

    stubCount = 1
    def testAllRequestStub(self):
        

        with open("tests/allTestCases.json", encoding='utf-8') as inpFile:
            #print(inpFile.read())
            allData = []
            try:
                allData = json.loads(inpFile.read())
            except JSONDecodeError as e:
                print("Invalid JSON File")
                exit()
        
            for inputData in allData:
                print(f"Stub Count : {TestVendorMachine.stubCount} ")
                driver.main(inputData)
                TestVendorMachine.stubCount+=1
                
if __name__ == '__main__':
    # 1 Stub :: Test All Request
    unittest.main()