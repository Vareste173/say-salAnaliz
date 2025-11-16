#𝑥3 −2𝑥2 −5=0 denkleminin [2,4] aralığında kökünü ikiye bölme 
#metodu ile 4 iterasyonda gerçekleştiriniz. Bulunan çözümün kodunu 
#hazır fonksiyon kullanmadan yazınız.
import math
#x degeri fonksiyondaki x
def gecerli(x):
    return (x**3)-(2*x**2)-5

def ikiye_bolme(a,b,iterasyon_sayisi):
    for n in range(iterasyon_sayisi):
        ikiyebol=(a+b)/2
        sonuc=gecerli(ikiyebol)
        print(f"{n+1}. iterasyon: x = {ikiyebol}, f(x) = {sonuc}")
        if gecerli(a)*sonuc < 0:
            b=ikiyebol    
        else:
            a=ikiyebol
    return (a+b)/2

a=2
b=4

if gecerli(a)*gecerli(b)<0:
    print("ikiye bolme metodu uygulanabilir\n")
    kok=ikiye_bolme(a,b,4)
    print("Kök:", kok)
else:
    print("ikiye bolme metodu uygulanamaz\n")


