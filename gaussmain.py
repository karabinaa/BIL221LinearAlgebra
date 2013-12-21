from lineereq import *

print "gauss v0.1"
print " "

print "Katsayýlar matrisini,",
katsayilar = Matris.readStdin()
print "Sabitler matrisini her elemandan sonra entera basarak giriniz. Bitirmek için B yazýnýz."
sabitler = Matris.readStdin(False)

cozumkumesi = gauss_elemination(katsayilar, sabitler)

if cozumkumesi == False:
        print "Denklem sisteminin çözüm kümesi boþ kümedir."
        
elif 'unknwn' in cozumkumesi or cozumkumesi == True:
        print "Denklem sisteminin sonsuz çözümü vardýr."

else:
        for i in range(len(cozumkumesi)):
                var = "x" + str(i+1)
                print var, " = ", cozumkumesi[i]
