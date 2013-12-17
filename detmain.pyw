# -*- coding: cp1254 -*-

from determinant import *

while True:
    A = Matris.readStdin(True)
    print  A,
    print " det(A) = ", det(A)

    answer = raw_input('Yeni bir determinant hesabı yapmak için "D"(Devam) yazıp entera basınız...')

    if answer != ( "D" or "Devam" or "d" or "devam" ): break
            
