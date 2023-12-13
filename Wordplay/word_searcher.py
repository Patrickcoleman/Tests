n = open('names.txt','r')
w = open('words.txt','r')

names = []
words = []


for name in n:
    names.append(name[:-1])

target_word = 'interstate'

for name2 in names:
    for name in names:
        name_letters = [i for i in name] + [i for i in name2]
        word_letters = [i for i in target_word]

        failed = False
        for letter in word_letters:
            if letter in name_letters:
                name_letters.remove(letter)
            else:
                failed = True
                break

        if not failed:
            print(f'{target_word} was in the names {name} + {name2}')

