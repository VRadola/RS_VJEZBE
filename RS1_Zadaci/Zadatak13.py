def min_max(lista):
    min = lista[0]
    max = lista[0]
    for broj in lista:
        if broj < min:
            min = broj
        elif broj > max:
            max = broj
        else:
            continue
    return min, max

def main():
    lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
    print(min_max(lista))

if __name__ == "__main__":
    main()