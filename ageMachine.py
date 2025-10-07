"""
this function take integer age as Argument and 
print if he/she/they/Them is old or will be old
"""
def ageMachine(age: int)->None:
        
        #input function return is always a string
        #input function is someting like async in javascript
        age = int(input("Wie alt bist du?"))
       
        if age > 50:
                print("Du bist alt geworden!")
        else:
                print("Aha. Eines Tages du wirst Alt auch!")
            


"""
this function accept two integer as Argument and add 
them and return result of summation
"""
#mercedes_auto snake_case wir können es für variablen nutzen
def addTwoNumber(first_number:int , second_number:int)->int:
        return first_number+second_number



ageMachine(age=input)
