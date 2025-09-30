print("ZINSBERECHNUNG 2025")
startkapital = float(input("Wie groß ist das Startkapital?"))
zinssatza = float(input("Wie hoch ist der jährliche Zinsatz?"))
n = int(input("Wieviele Zinsperioden pro Jahr?"))
laufzeit = int(input("Wieviele Jahre Laufzeit?"))

endbetrag = startkapital * (1 + zinssatza / n) ** (n * laufzeit)

print(f"Nach {laufzeit} Jahren beträgt der Endbetrag : {round(endbetrag,2)} Euro")