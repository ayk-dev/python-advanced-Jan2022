n = int(input())

chemical_compounds = set()

for _ in range(n):
    data = input().split()
    chemical_compounds.update({el for el in data})

print('\n'.join(chemical_compounds))