from lineereq import *

print "cramer v0.1"
print " "

print "Katsay�lar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek i�in B yaz�n�z."
sabitler = Matris.readStdin(False)

cozumkumesi = cramer(katsayilar, sabitler)

if cozumkumesi == False:
    print "Denklem sisteminin ��z�m� yoktur"

elif  cozumkumesi == True:
    print "Denklem sisteminin sonsuz ��z�m� vard�r."

else:
    for i in range(len(cozumkumesi)):
        var = "x" + str(i+1)
        print var, " = ", cozumkumesi[i]
