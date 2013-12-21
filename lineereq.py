# -*- coding: cp1254 -*-

from matris import *
from determinant import *
import copy
from fractions import Fraction

def satircarpma(satir, sayi):
    ysatir = []
    for i in range(len(satir)):
        ysatir.append(satir[i] * sayi)
    return ysatir

def elementercikarma(matris, satirno, csatir):
    for i in range(len(csatir)):
        matris[satirno][i] = matris[satirno][i] - csatir[i]
    return matris

def ekMatrisOlustur(katsayilar, sabitler):
    for i in range(sabitler.m):
        katsayilar[i].append(sabitler[i][0])
    return katsayilar

def indirge(matris):
    for i in range(matris.m):
        temp = satircarpma(copy.deepcopy(matris[i]), Fraction(1,matris[i][i])) 
        for j in range(i+1, matris.m):
            matris = elementercikarma(matris, j, satircarpma(temp, matris[j][i]))
    return matris
    

def gauss_elemination(katsayilar, sabitler):
    cozumkumesi = ["unknwn"]*katsayilar.m
    indirgenmis = indirge(ekMatrisOlustur(katsayilar, sabitler))
    rankKatsayilar = 0
    rankSabitler = 0
    
    for i in range(katsayilar.m):
        if 0 not in indirgenmis[i][:katsayilar.m]:
            rankKatsayilar +=1
        if 0 != indirgenmis[i][-1]:
            rankSabitler +=1

    if rankKatsayilar == rankSabitler:
        for i in range(1,katsayilar.m+1):
            for j in range(1, katsayilar.m+1):
                if (cozumkumesi[-j] != "unknwn"):
                    indirgenmis[-i][-1] -= indirgenmis[-i][-j-1]*cozumkumesi[-j]
            if indirgenmis[-i][-i-1] != 0:
                cozumkumesi[-i] = indirgenmis[-i][-1]/indirgenmis[-i][-i-1]

        return cozumkumesi

    elif rankKatsayilar < rankSabitler:
        return False

    elif rankKatsayilar > rankSabitler:
        return True

               
def cramer(katsayilar, sabitler):
    delta = float(det(katsayilar))
    cozumkumesi = []
    
    for i in range(katsayilar.n):
        temp = copy.deepcopy(katsayilar)
        for j in range(katsayilar.m):
            temp[j][i]=sabitler[j][0]
        if delta != 0:    
            cozumkumesi.append(det(temp)/delta)
        else:
            cozumkumesi.append(det(temp))

        temp = copy.deepcopy(katsayilar)
            
    if delta != 0 :
        return cozumkumesi         
    
    else:
        for i in cozumkumesi:
            if i != 0:
                return False
            else:
                return True
        
    
        

