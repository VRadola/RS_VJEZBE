brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda broj: (broj, broj ** 2), brojevi))
print(transform)