# -*- coding: cp1254 -*-

from determinant import *

while True:
    A = Matris.readStdin(True)
    print " Girdi�iniz matrisin determinant� ", det(A), " d�r"
    print " "
    print 'Yeni bir determinant hesab� yapmak i�in "D"(Devam) yaz�p entera bas�n�z...'
    answer = raw_input()

    if answer != ( "D" or "Devam" or "d" or "devam" ): break
            
