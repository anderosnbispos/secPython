import hashlib

def gerahash_md5(string):
    resultado = hashlib.md5(string.encode('utf-8'))
    print('\nO hash MD5 da string: {}, é: {}'
          .format(string, resultado.hexdigest()))

def gerahash_sha1(string):
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('\nO hash SHA1 da string: {}, é: {}'
          .format(string, resultado.hexdigest()))

def gerahash_sha256(string):
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('\nO hash SHA256 da string: {}, é: {}'
          .format(string, resultado.hexdigest()))

def gerahash_sha512(string):
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('\nO hash SHA512 da string: {}, é: {}'
          .format(string, resultado.hexdigest()))

def menu():
    escolha = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ###
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    Digite o número do hash a ser gerado: '''))

    return escolha

if __name__ == '__main__':
    string = input('Digite o texto a ser hasheado: ')
    esc = menu()

    if esc == 1:
        gerahash_md5(string)
    elif esc == 2:
        gerahash_sha1(string)
    elif esc == 3:
        gerahash_sha256(string)
    elif esc == 4:
        gerahash_sha512(string)
    else:
        print('Opção {} inválida.'.format(esc))

