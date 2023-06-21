n = 0
tri = 0
maxFax = 0
maxFaxNum = 0

def factorFinder(num):
    i = 1
    factors = 0
    while i < num ** (1/2):
        if num % i == 0:
            factors += 2
        i += 1
    if i == num ** (1/2):
        factors += 1
    return factors


while maxFax < 500:
    n += 1
    tri += n
    currentFax = factorFinder(tri)
    if currentFax > maxFax:
        maxFax = currentFax
        maxFaxNum = tri
    #print(f'tri {tri} is a triangular number with {currentFax} factors, maxfactors {maxFax}')

print(f'The smallest triangular number with {maxFax} factirs was {maxFaxNum}')

