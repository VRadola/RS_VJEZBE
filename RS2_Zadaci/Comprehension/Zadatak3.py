brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

neparni_brojevi = {broj: broj if broj % 2 == 0 else broj ** 3 for broj in brojevi}

print(neparni_brojevi)