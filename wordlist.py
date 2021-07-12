import itertools
import string

resultado = itertools.permutations(string.ascii_letters + string.digits, 5)

for i in resultado:
    print(''.join(i))