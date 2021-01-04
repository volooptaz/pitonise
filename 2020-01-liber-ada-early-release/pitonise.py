#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import random
from subprocess import Popen, PIPE 

# Wordlist customizada del modulo python diceware (no hay ES en el modulo)
# Lista utilizada:
# https://theworld.com/~reinhold/diceware_espanol/DW-Espanol-1.txt
#WORDLIST = 'pt-br'

# Diferentes fuentes de entropia. Pueden tener diferentes codificaciones, pero
# como utilizamos aqui solamente fuentes del script `lava.py` para LavaRand,
# simplificamos asumindo que todos estan en hexadecimal
FUENTES = [
    # Resultado do LavaRand na imagem da Lava Lamp
    'd4c410d8e0fe143c8cbee8aaaa488cb29c8fa3ce68aca9edcaa40b2d696da92c08c8e288a0ee2c94b8fc90f8c0e05ae482e470c494d0d2a610a0ba82fe9e928e96b2fa8420ae98e4e0c0bc80c229aae7cf438e2b4dae0c0cc5264fcbac6ea62e6c2a0daea2884f89ad6b6223edc82aea8cca6468616c8e2aacaa8f4baf2cadeaceab4c2cc1e9a88f044d4bab8ae4a2dea2ea4c4afec2d24886e6e0b2e2ee24d08ccacc060a63a9c9ea0e2c8a2dec6509a269896224250f6de96aaecac9cc8a2f68e926e0b026fc4af0b0901292b6941cc6e8e0a4d46286c4b690e08e8226c7e20a8d4b2f0f4fab0dc28dab898b0de84f4ba8b8bafccef4a06aece8feceacaacaf4eef4840649e5c48c692d2e634b49eaf2dc2094bef2f08eec268ebe9cc098888c9eeeda3c24e4d8a8aedad4fab46ec036a0ecce3cd02efc908acaa09e96bac6c6d2e4aaccc268d2fa18c81ce68cc04ac7494729898446af0aefaecf828cb0b6a4',
]

# Caracters unicode para representaren los dados
# (con 'x' de padding para indexacion equivalente a el numero)
DADOS = ' ⚀⚁⚂⚃⚄⚅'


# Retorna una palabra de Diceware
def palabra():
    # Executa el programa 'diceware' disponible en en modulo `diceware` de python.
    # Hecho esto en vez de importar el módulo porque así hay como generar nuestros
    # propios dados (usando nuestro seed)
    def comando_diceware(rodadas):
        comando = ['diceware', '-n', '1', '-r', 'realdice']
        cli_input = rodadas.encode('utf-8')
        p = Popen(comando, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=cli_input)[0][99:-1]
        return stdout_data.decode('utf-8')

    # Rodada de 5 dados
    rs = [random.choice(range(1, 7)) for i in range(5)]

    # Envia rodadas para diceware CLI
    rodadas_cli = ', '.join([str(n) for n in rs])
    palabra = comando_diceware(rodadas_cli)

    # Salida para terminal
    rodadas_unicode = ' '.join([DADOS[n] for n in rs])
    print(rodadas_unicode + ' ' + palabra)

    return palabra

if __name__ == '__main__':
    ### ENTROPIA - Sumando fuentes
    # Utiliza solo los primeros 700 bits de entropia para evitar un error aún
    # no explicado - investigar lava.py
    entropia_total = b''.join(
        bytes(bytearray.fromhex(entropia[:700]))
        for entropia in FUENTES
    )

    random.seed(entropia_total)

    print(random.choice(range(1, 31))) # Arcano maior - Enochian
    print(random.choice(range(31, 87))) # Arcano menor - Enochian

    random.seed(entropia_total)

    ### DICEWARE - Palabras
    resultado = [palabra() for i in range(13)]
    resultado_str = ' '.join(resultado)
    print(resultado_str)

    random.seed(entropia_total)
