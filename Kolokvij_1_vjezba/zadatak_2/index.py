from fakultet import student as s
from fakultet import podaci as p

# 2.2

def stvori_sve_studente_objekte(razredi_studenti: list):
    svi_studenti_objekti = []
    for razred_info in razredi_studenti:
        naziv_razreda = razred_info["razred"]
        for student_info in razred_info["studenti"]:
            ime, prezime = student_info["ime_prezime"].split(" ", 1)
            kolegij_ocjene = {k["naziv"]: k["ocjena"] for k in student_info["kolegiji"]}

            student_objekt = s.Student(
                ime = ime,
                prezime = prezime,
                razred = naziv_razreda,
                kolegij_ocjene = kolegij_ocjene
            )

            svi_studenti_objekti.append(student_objekt)
    return svi_studenti_objekti

studenti_objekti = stvori_sve_studente_objekte(p.razredi_studenti)

for so in studenti_objekti:
    print(f"Student: {so.ime} {so.prezime}, razred: {so.razred}, kolegij i ocjene {so.kolegij_ocjene}")
# 2.3
    print(f"Prosjek: {so.prosjek_ocjene()}")

# 2.4
studenti_objekti[0].promjena_razreda("1B")
studenti_objekti[0].promjena_razreda("1C")

print(f"Student: {studenti_objekti[0].ime} je sada {studenti_objekti[0].razred}")