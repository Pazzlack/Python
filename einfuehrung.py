"""
Erste lektion
#Deklaration

umschueler=21 #in der Variable umschueler steckt die Zahl 21

a=10
b=2
c=a/b #Division

c=a*b #Multiplikation
c=a+b # Addition
c=a-b #Subtraktion
c=a%b #Modulo (Gibt den Restwert der Division zurück)

print(c)#Ausgabe alles was im Terminal erscheinen soll
#alles was in () steht nennt man Funktion, eine Funktion tut was

print (10/2) #Alternative
print (f"{a/b}") #Alternative
print("Das Ergebnis ist: ", a/b) #Alternative
print (f" Das Ergebnis von {a} und {b} ist {c}") # f-string String 
"""

"""
Zweite Lektion
schueler0="Marcel"
schueler1="Mostafa"
schueler2="Hamit"
schueler3="Brüning"
#           0           1       2       3
schueler=["Marcel","Mostafa","Hamit","Brüning"]

schueler.pop() #löscht den letzten Eintag in der Liste

schueler.append("Graf") #fügt einen Eintrag am Ende der Liste hinzu

print(len(schueler)) #gibt die Länge der Liste zurück

print(schueler)

print(schueler[2])#gibt den Eintrag an der Stelle 2 zurück
"""
"""
Lektion 3


a=2
b=3

istkorrekt=a!=b #entweder true oder false

print(istkorrekt)
"""

istaufgestanden = False
hatsichangezogen = False
hatgefruehstueckt = False

perfektgestartet = istaufgestanden and hatsichangezogen #AND Operator
print(perfektgestartet)

perfektgestartet = istaufgestanden or hatsichangezogen #OR Operator