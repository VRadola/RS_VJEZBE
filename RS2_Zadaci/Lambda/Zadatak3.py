def kvadriraj_niz(lista, fukkcija):
    nova_lista = []
    for broj in lista:
        nova_vrijednost = fukkcija(broj)
        nova_lista.append(nova_vrijednost)
    return nova_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(kvadriraj_niz(lista, lambda x: x ** 2))