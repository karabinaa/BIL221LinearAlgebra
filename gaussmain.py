from lineereq import *

print "Katsay�lar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek i�in B yaz�n�z."
sabitler = Matris.readStdin(False)

cozumkumesi = gauss_elemination(katsayilar, sabitler)

for i in range(len(cozumkumesi)):
        var = "x" + str(i+1)
        print var, " = ", cozumkumesi[i]
