publicKey = [5,26]
privateKey = [17,26]
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def power(pow,i):
    return i ** pow


for i in range(1,27):
    letter = alphabet[i-1]
    ipow = power(publicKey[0],i)
    ipowrem = (ipow % publicKey[1]) % 26
    encryptedletter = alphabet[ipowrem - 1]
    decryptpow = ipowrem**privateKey[0]
    decryptpowrem = (decryptpow % privateKey[1] % 26)
    decryptedletter = alphabet[decryptpowrem - 1]
    print('{} > {} > {}'.format(letter,encryptedletter,decryptedletter))
    print('the number for {} is: '.format(letter) + str(i) + '           i ** '+ str(publicKey[0]) + '  is: ' + str(ipow) + '         i**5 % 14 is: ' + str(ipowrem) + '    which converts to: ' + encryptedletter)
    print('To decrypt encryptedletter: {} we convert back to num: {}   then take it to the power of {} = {}, and then take this remainder {} which gives us the number {} which converts to letter: {}'.format(encryptedletter,ipowrem,privateKey[0],decryptpow,privateKey[1],decryptpowrem,decryptedletter))
