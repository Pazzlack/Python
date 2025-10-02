def Addition (zahl_1, zahl_2):
    ergebnis=zahl_1+zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")
    
def Subtraktion (zahl_1, zahl_2):
    ergebnis=zahl_1-zahl_2  
    print(f"Das Ergebnis ist: {ergebnis}")
    

def Multiplikation (zahl_1, zahl_2):
    ergebnis=zahl_1*zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")
    
def Division (zahl_1, zahl_2):
    if(zahl_2==0):
        print("Fehler: Division durch 0 nicht möglich")
        return
    ergebnis=zahl_1/zahl_2
    print(f"Das Ergebnis ist: {ergebnis}")
    

print("Taschenrechner für 2 Zahlen")
ergebnis=0

zahl_1=(input("Bitte gebe Zahl 1 ein:"))

zahl_2=(input("Bitte gebe Zahl 2 ein:"))

operation=(input("Welche Operation möchtest du durchführen? (+,-,*,/):"))

if operation=="+":
    Addition (int(zahl_1), int(zahl_2))

elif operation=="-":
    Subtraktion (int(zahl_1), int(zahl_2))

elif operation=="*":
    Multiplikation (int(zahl_1), int(zahl_2))

elif operation=="/":
    Division (int(zahl_1), int(zahl_2)) 

else:
    print("Falsche Eingabe, bitte nur +,-,*,/ eingeben")








