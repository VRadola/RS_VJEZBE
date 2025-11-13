min_duljina = int(input("Unesite minimalnu duljinu rijeci: "))
duge_rijeci = 0
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

duge_rijeci = list(filter(lambda rijec: len(rijec) > min_duljina, rijeci))

print(duge_rijeci)