n = open('names.txt','r')
w = open('words.txt','r')

names = []
words = []

for word in w:
    words.append(word[:-1])

for name in n:
    names.append(name[:-1])

best_word = ''

# for name2 in names:
for name in names:
    name_letters = [i for i in name] #+ [i for i in name2]

    record_word = None
    record_length = 0

    for word in words:
        if len(word) < record_length:
            continue
        else:
            word_letters = [i for i in word]
            name_letters_copy = name_letters.copy()
            failed = False
            for letter in word_letters:
                if letter in name_letters_copy:
                    name_letters_copy.remove(letter)
                else:
                    failed = True
                    break
            
            if not failed:
                if len(word) > record_length:
                    record_length = len(word)
                    record_word =[word]
                else:
                    record_word.append(word)
                
    if record_length > len(best_word):
        best_word = record_word[0]

    print(f'The best word/s I found for the names {name} are {record_word} of len {record_length}')

# print(f' the best word I found overall was { best_word}')