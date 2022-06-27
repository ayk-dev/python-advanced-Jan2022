try:
    with open('custom_files/numbers.txt') as file:
        sum_numbers = 0
        for line in file.readlines():
            sum_numbers += int(line)
        print(sum_numbers)
except:
    print('File not found or path is wrong')