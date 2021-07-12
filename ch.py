import hashlib

def compara():
    arq1 = 'a.txt'
    arq2 = 'b.txt'

    hash1 = hashlib.new('ripemd160')
    hash1.update(open(arq1, 'rb').read())

    hash2 = hashlib.new('ripemd160')
    hash2.update(open(arq2, 'rb').read())

    if (hash1.digest() != hash2.digest()):
        print('Arquivos diferentes')
        print('hash1 : {}'.format(hash1.hexdigest()))
        print('hash2 : {}'.format(hash2.hexdigest()))
    else:
        print('Mesmo arquivo')
        print('hash1 : {}'.format(hash1.hexdigest()))
        print('hash2 : {}'.format(hash2.hexdigest()))

if __name__ == '__main__':
    compara()