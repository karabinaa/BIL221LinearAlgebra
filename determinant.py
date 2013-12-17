# -*- coding: cp1254 -*-


from matris import *
import sys

def det2x2(mat):
    if mat.m != 2 and mat.n !=2:
        print ""

    else:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

def minor(mat, idn, idm=0):
    temp2=[]
    for i in range(1,mat.m):
        temp1 = []
        for j in range(len(mat[i])):
            if j!= idn:
                temp1.append(mat[i][j])
        temp2.append(temp1)
        
    if len(temp2) == 2:
        return det2x2(Matris.fromList(temp2))
    else:
        return det(Matris.fromList(temp2))

def det(mat):

    if mat.m != mat.n:
        raise MatrisError, "Yalnızca kare matrislerin determinantı alınabilir."

    elif mat.m == 2 and mat.n == 2:
        return det2x2(mat)

    else:
        toplam = 0
        for i in range(mat.n):
            kofaktor = ((-1)**(i+2))* minor(mat, i)
            toplam += mat[0][i]*kofaktor

        return toplam
