 #in following code problem solving is to calculate how much money each person get if 3 persons share 500 euro and they get exact same amount of money
geld = 500
moastafa = None
olga = None
gleb = None

restgeld = geld % 3 # in this case it is 2
teilbareGeld= geld - restgeld # in this case it is 498
mostafa = teilbareGeld / 3 # in this case it is 166
print (f"mostafa bekommt {mostafa}")