def prvi_i_zadnji_broj(lista):
    return (lista[0], lista[-1])

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(prvi_i_zadnji_broj(lista))

if __name__ == "__main__":
    main()