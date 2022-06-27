import re
import os


def get_searched_words(file_path):
    searched_words = []
    with open(file_path) as file:
        searched_words = file.read().split()
    return searched_words


def count_words(searched, file_path):
    words_count = {}
    with open(file_path) as file:
        text = file.read()
        for word in searched:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count
    return words_count


def write_output(words_count, file_path):
    with open(file_path, 'w') as file:
        sorted_count = sorted(words_count.items(), key=lambda kvpt: -kvpt[1])
        for word, count in sorted_count:
            file.write(f'{word} - {count}\n')


absolute_path = os.path.dirname(os.path.abspath(__file__))

words_path = os.path.join(absolute_path, 'custom_files', 'words.txt')
# print(words_path)
words = get_searched_words(words_path)

input_path = os.path.join(absolute_path, 'custom_files', 'input.txt')
# print(input_path)
words_count_dict = count_words(words, input_path)

output_path = os.path.join(absolute_path, 'custom_files', 'output')
# print(output_path)
write_output(words_count_dict, output_path)

