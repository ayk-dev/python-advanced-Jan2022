import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, 'custom_files', 'text_evenlines.txt')
chars_to_replace = ["-", ",", ".", "!", "?"]
new_char = '@'

with open(file_path) as file:
    text = file.read().splitlines()
    for i in range(len(text)):
        if i % 2 == 0:
            line = text[i]
            for ch in chars_to_replace:
                line = line.replace(ch, new_char)
            print(' '.join(reversed(line.split())))


