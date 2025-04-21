'''Genera una contraseña aleatoria de 8 caracteres'''

import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(caracteres)for _ in range(8))

print("Tu contraseña aleatoria es: ", password)