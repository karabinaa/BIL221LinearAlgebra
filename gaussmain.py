from lineereq import *

print "Katsay�lar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek i�in B yaz�n�z."
sabitler = Matris.readStdin(False)

cozumkumesi = gauss_elemination(katsayilar, sabitler)

if cozumkumesi == True:
        print "Denklem sisteminin ", rankKatsayilar - rankSabitler, " parametreye ba�l� sonsuz ��z�m� vard�r."
elif cozumkumesi == False:
        print "Denklem sisteminin ��z�m k�mesi bo� k�medir."
else:
        for i in range(len(cozumkumesi)):
                var = "x" + str(i+1)
                print var, " = ", cozumkumesi[i]
