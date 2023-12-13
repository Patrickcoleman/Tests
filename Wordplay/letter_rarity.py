letters = 'abcdefghijklmnopqrstuvwxyz'

f = open('names.txt','r')

names = {}
for name in f:
    names[name[:-1].lower()] = {}

for letter in letters:
    count = 0
    names_in = []
    for name in names:
        if letter in name:
            names_in.append(name)
            count += 1

    print(f'The letter {letter} was found in {count} names: {names_in}')
    for name in names_in:
        names[name][letter] = count

print(names)