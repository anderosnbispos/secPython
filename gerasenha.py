import random, string

def gera_senha():
    tamanho = 16
    chars = string.ascii_letters + string.digits + '!@#$%&()[]{}' + '!@#$%&'
    # chars = string.ascii_uppercase + string.digits + '!@#$%&*()-=+,.:;/?'
    # chars = string.ascii_lowercase + string.digits + '!@#$%&*()-=+,.:;/?'
    rnd = random.SystemRandom() #os.urandom
    print(''.join(rnd.choice(chars) for i in range(tamanho)))

if __name__ == '__main__':
    gera_senha()