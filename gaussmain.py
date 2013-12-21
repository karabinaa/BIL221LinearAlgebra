from lineereq import *

print "Katsayýlar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek için B yazýnýz."
sabitler = Matris.readStdin(False)

cozumkumesi = gauss_elemination(katsayilar, sabitler)

if cozumkumesi == True:
        print "Denklem sisteminin ", rankKatsayilar - rankSabitler, " parametreye baðlý sonsuz çözümü vardýr."
elif cozumkumesi == False:
        print "Denklem sisteminin çözüm kümesi boþ kümedir."
else:
        for i in range(len(cozumkumesi)):
                var = "x" + str(i+1)
                print var, " = ", cozumkumesi[i]
