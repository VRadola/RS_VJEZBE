def izbaci_duple(lista):
    set_bez_duplih_brojeva = set(lista)
    return list(set_bez_duplih_brojeva)

def main():
    lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(izbaci_duple(lista))

if __name__ == "__main__":
    main()