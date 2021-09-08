# coffee-vending-machine
> Low Level System Design Of Coffee Vending Machine

### Project Requirements
> Python 3.9

### Project layout

    .
    ├── controllers               # Controllers ( business logic )
    ├── models                    # All Class Based Entities
    ├── services                  # Services Communicating
    ├── test                      # Test Case Files
    ├── main.py                   # Main Method ( driver code ) 
    ├── test.py                   # 1 Stub with 4 testcase ( mocking execution )
    └── README.md                 # General Info

### Running Program
```
python main.py
```

### Running TestCase
```
python test.py
```

# Expected Output
```
Configured Machine With 4 outlets

Name     :  hot_water
Qty      :  400
Added On :  2021-09-08 12:08:14.278542
Name     :  hot_milk
Qty      :  350
Added On :  2021-09-08 12:08:14.278547
Name     :  ginger_syrup
Qty      :  100
Added On :  2021-09-08 12:08:14.278552
Name     :  sugar_syrup
Qty      :  120
Added On :  2021-09-08 12:08:14.278556
Name     :  tea_leaves_syrup
Qty      :  100
Added On :  2021-09-08 12:08:14.278558


hot_tea is prepared

hot_coffee cannot be prepared because hot_milk is not sufficient

black_tea cannot be prepared because hot_water is not sufficient

green_tea cannot be prepared because green_mixture is not available
```



