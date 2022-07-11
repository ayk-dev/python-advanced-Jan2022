import os

while True:
    command = input()
    if command == 'End':
        break

    cmd, file_name, *args = command.split('-')
    if cmd == 'Create':
        open(file_name, 'w').close()

    elif cmd == 'Add':
        content = args[0] + '\n'
        with open(file_name, 'a') as file:
            file.write(content)

    elif cmd == 'Replace':
        old_string = args[0]
        new_string = args[1]
        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(file_content)
        else:
            print('An error occurred')

    elif cmd == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')


