#it is a callBack example, customer in restaurant put order and Waiter deliver food


##--
#PS code (beachten Sie arr_lenght is definieren in Linie 12
# def food_exists = 0
# // i ist Array Index
# For i = 0 BIS i <= arr_lenght i PLUS 1
#     WENN food_name IST GLEICH arr_foods[i] 
#         food_exists = 1
# END IF
# Return food_exists
##--

def checkFoodExistence(food_name:str)->bool:
   #              0         1      2        ..... n
    arr_foods=["Pizza", "Pasta","Döner"]
    
    if food_name in arr_foods:
        return True
    else:
        return False

def orderFood(food_name:str, checkFoodExistence):
    is_food_exist = checkFoodExistence(food_name)
    if is_food_exist:
        print(f"your {food_name} is delivering soon!")
    else:
        print(f"Sorry, we don't have {food_name} in our menu!")

#-- actual program use upper defined methods --#
order_string = input("What is your order?")
orderFood(order_string,checkFoodExistence)