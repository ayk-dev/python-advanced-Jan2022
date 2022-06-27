try:
    file = open("custom_files/inner.txt")
    print('File found')
    file.close()
except FileNotFoundError:
    print('File not found')

###############################

with open("custom_files/inner.txt") as file:
    print('File found')