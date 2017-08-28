import sys

new_file = sys.argv[0]
with open(new_file, 'w+') as file:
    text = str()
    while input() != 'EOF':
        file.write(text)
        text = input()