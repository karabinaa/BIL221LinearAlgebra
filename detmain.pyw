# -*- coding: cp1254 -*-

from determinant import *

while True:
    A = Matris.readStdin(True)
    print  A,
    print " det(A) = ", det(A)

    answer = raw_input('Yeni bir determinant hesab� yapmak i�in "D"(Devam) yaz�p entera bas�n�z...')

    if answer != ( "D" or "Devam" or "d" or "devam" ): break
            
