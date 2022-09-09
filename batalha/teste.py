people = {"Jim": 3, "Jack": 2, "Jane": 4, "Jill": 1}


coisa = sorted(people.items(), key=lambda item: item[1])
print(coisa[1][1])