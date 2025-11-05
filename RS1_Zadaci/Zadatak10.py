def parni_neparni_brojevi(lista):
    parni = []
    neparni = []
    rijecnik_brojeva = {"parni" : parni, "neparni" : neparni}
    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)
    return rijecnik_brojeva

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(parni_neparni_brojevi(lista))

if __name__ == "__main__":
    main()