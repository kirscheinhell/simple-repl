#import sys

def main(arg):
    new_file = arg
    lines = []
    print('START')
    line = input()
    while line != 'EOF':
        lines.append((line))
        line = input()
    print(lines)
    with open(new_file, 'w+') as file:
        file.write('\n'.join(lines))