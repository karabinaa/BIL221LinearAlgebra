# -*- coding: cp1254 -*-

from determinant import *

while True:
    A = Matris.readStdin(True)
    print " Girdiğiniz matrisin determinantı ", det(A), " dır"
    print " "
    print 'Yeni bir determinant hesabı yapmak için "D"(Devam) yazıp entera basınız...'
    answer = raw_input()

    if answer != ( "D" or "Devam" or "d" or "devam" ): break
            
