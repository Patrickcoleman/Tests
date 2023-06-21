prime1 = 13
prime2 = 2
N = prime1 * prime2
phiN = (prime1 - 1) * (prime2 - 1)
notcoprimesoffN = []
notcoprimesoffphiN = []

def appendnoncoprimestoarray(num,array):
    array.append(1)
    breaking = False
    for i in range(2,num + 1):
        breaking = False
        for j in range(2,i + 1):
            if num % j == 0 and i % j == 0:
                breaking = True
                break
        if breaking:
            array.append(i)

appendnoncoprimestoarray(N,notcoprimesoffN)
appendnoncoprimestoarray(phiN,notcoprimesoffphiN)

notcoprimesoffboth = [*set(notcoprimesoffN + notcoprimesoffphiN)]

e = 2
while e < phiN:
    if e not in notcoprimesoffboth:
        break
    elif e == phiN - 1:
        print('didnt find a good E')
    e += 1

d = 2
while d < 1000:
    print(f'd: {d} * e:{e} = {e*d}, which mod phiN is: {e*d % phiN} ')
    if e*d % phiN == 1 and d != e:
        print(f'd: {d} * e:{e} = {e*d}, which mod phiN is: {e*d % phiN} ')
        break
    d += 1

print('prime1: ' + str(prime1))
print('prime2: ' + str(prime2))
print('N: ' + str(N))
print('phiN: ' + str(phiN))
print('e: ' + str(e))
print('d: ' + str(d))
