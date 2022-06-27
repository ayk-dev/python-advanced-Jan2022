import os


def count_letters_and_punct(string):
    punctuation =  ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" )
    count_letters = 0
    count_punct = 0
    for ch in string:
        if ch.isalpha():
            count_letters += 1
        elif ch in punctuation:
            count_punct += 1
    return count_letters, count_punct


absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path_read = os.path.join(absolute_path, 'custom_files', 'text_evenlines.txt')
file_path_write = os.path.join(absolute_path, 'custom_files', 'output_line_numbers.txt')

with open(file_path_read) as read_file, open(file_path_write, 'w') as write_file:
    text = read_file.read().splitlines()
    for index, line in enumerate(text):
        letters_count, punct_count = count_letters_and_punct(line)
        new_line = f'Line {index+1}: {line} ({letters_count})({punct_count})\n'
        write_file.write(new_line)

