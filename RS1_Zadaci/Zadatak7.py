def filtriraj_parne(lista):
    lista_parnih_brojeva = []
    for broj in lista:
        if broj%2 == 0:
            lista_parnih_brojeva.append(broj)
    return lista_parnih_brojeva

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filtriraj_parne(lista))

if __name__ == "__main__":
    main()