#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, 'C:/Users/laure/PycharmProjects/c04-ch6-exercices_LaureneRly')
from exercice2 import frequence

# TODO: Définissez vos fonction ici
def ellipsoide(a = 2, b = 4, c = 2, p = 10):

    volume = (4/3)*a*b*c*math.pi
    masse = p*volume

    return volume, masse







if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoide())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("ceci est uuuuuuune phrase"))


