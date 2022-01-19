text = sorted(list(input()))

characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for ch, occur in characters.items():
    print(f'{ch}: {occur} time/s')