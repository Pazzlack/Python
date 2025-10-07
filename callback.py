def kundebestellt(essen):
    menu = ["Pizza", "Pasta", "Salat"]
    auswahl=input(f"Was möchten Sie bestellen? Wir haben {menu}.")

    if auswahl in menu:
        essen(auswahl)
    else:
        print("Entschuldigung, das haben wir nicht auf der Karte.")

def essen (auswahl):

        print(f"Vielen Dank für Ihre Bestellung von {auswahl}.")


kundebestellt(essen)