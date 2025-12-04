from data.prilog import razredi_studenti

# 1.2
def dohvati_studente_iz_razreda(studenti_razredi: list, naziv_razreda: str):
    imena_prezimena = []
    for student in studenti_razredi:
        if student["razred"] == naziv_razreda:
            for element in student["studenti"]:
                imena_prezimena.append(element)
    return imena_prezimena

#print(dohvati_studente_iz_razreda(razredi_studenti, "1B"))

# 1.3

def prosjek_studenata(razredi_studenti, ime_prezime):
    student_pronaden = None
    for element in razredi_studenti:
        for student in element["studenti"]:
            if student["ime_prezime"] == ime_prezime:
                student_pronaden = student
    if not student_pronaden:
        return None
    else:
        suma = 0.0
        for kolegij in student_pronaden["kolegiji"]:
            suma += kolegij["ocjena"]
        return round(suma/len(student_pronaden["kolegiji"]), 1)

#print(prosjek_studenata(razredi_studenti, "Ivana Kovač"))

# 1.4

broj_razreda_studenata = [(element["razred"], len(element["studenti"])) for element in razredi_studenti]

##print(broj_razreda_studenata)

# 1.5

imena_prezimena = [student["ime_prezime"] for element in razredi_studenti for student in element["studenti"] if element["razred"] == "1B"]

print(imena_prezimena)