from lineereq import *

print "cramer v0.1"
print " "

print "Katsayýlar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek için B yazýnýz."
sabitler = Matris.readStdin(False)

cozumkumesi = cramer(katsayilar, sabitler)

if cozumkumesi == False:
    print "Denklem sisteminin çözümü yoktur"

elif  cozumkumesi == True:
    print "Denklem sisteminin sonsuz çözümü vardýr."

else:
    for i in range(len(cozumkumesi)):
        var = "x" + str(i+1)
        print var, " = ", cozumkumesi[i]
