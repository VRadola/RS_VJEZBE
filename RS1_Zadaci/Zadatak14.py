def presjek(skup1, skup2):
    presjek_brojeva = set()
    for brojevi_skup1 in skup1:
        for brojevi_skup2 in skup2:
            if brojevi_skup1 == brojevi_skup2:
                presjek_brojeva.add(brojevi_skup1)
    return presjek_brojeva

def main():
    skup_1 = {1, 2, 3, 4, 5}
    skup_2 = {4, 5, 6, 7, 8}
    print(presjek(skup_1, skup_2))

if __name__ == "__main__":
    main()