n = open('names.txt','r')
w = open('words.txt','r')

names = []
words = []
min_shared = 5
min_length = 9


for word in w:
    words.append(word[:-1])

for name in n:
    names.append(name[:-1])

letters = 'abcdefghijklmnopqrstuvwxyz'
banned_letters = []
for letter in letters:
    count = 0
    for name in names:
        if letter in name:
            count += 1
    if count < min_shared:
        banned_letters.append(letter)
        print(f'letter {letter} is shared by {count} names and banned')

print(f'banned_letters: {banned_letters}')
searched_combos = []
found_words = {}
unique_words = {}
for name2 in names:
    for name in names:
        if name == name2:
            continue

        if [name,name2] in searched_combos:
            continue
        else:
            searched_combos.append([name2,name])
            searched_combos.append([name,name2])
        name_letters = [i for i in name] + [i for i in name2]

        record_word = []
        record_length = 6

        for word in words:
            skip = False
            for banned_letter in banned_letters:
                if banned_letter in word:
                    skip = True
                    continue
            if len(word) < min_length or skip:
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
                    if word not in found_words:
                        found_words[word] = 1
                        unique_words[word] = [name,name2]
                    else:
                        if word in unique_words:
                            unique_words.pop(word)
                    
        # if record_length > len(best_word):
        #     best_word = record_word[0]

print(unique_words)
        # print(f'The best word/s I found for the names {name} and {name2} are {record_word} of len {record_length}')

# print(f' the best word I found overall was { best_word}')