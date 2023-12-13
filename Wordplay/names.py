f = open('names.txt','r')

names = []
word = 'belle delphine'
letters = [i for i in word]
for name in f:
    names.append(name[:-1])

print(names)

for name in names:
    score = 0
    local_letters = letters.copy()
    for char in name:
        if char in local_letters:
            local_letters.remove(char)
            score +=1
    print(f'{name} got score {score}')