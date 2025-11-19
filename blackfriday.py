# BLACK FRIDAY
 
# 1: define list with items
items = ["Produkt1", "Produkt2", "Produkt3", "Produkt4", "Produkt5",
    "Produkt6", "Produkt7", "Produkt8", "Produkt9", "Produkt10"]
 
# 2: show all defined list
print("Verfügbare Items:")
for i in range(len(items)):
    print(f"{i + 1}: {items[i]}")   # +1 weil Anzeige bei 1 startet
 
# 3: print question
print("Welche magst du? Bitte ItemNummer eingeben:")
 
# 4: kunde input ItemNummer
inputNum = int(input())
 
# 5: delete itemNummer von list
# Da Python bei 0 beginnt, müssen wir -1 rechnen
del items[inputNum - 1]
 
# 6: print Danke!
print("Danke!")
 
# 7: print availableList() // ohne ausgewähltes Item
print("Verbleibende Items:")
for i in range(len(items)):
    print(f"{i + 1}: {items[i]}")