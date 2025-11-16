#𝑥3 +4𝑥2 −10 =0 denkleminin [1,2] aralığında kökünü ikiye
#bölme metodu ile 4 iterasyonda gerçekleştiriniz. Bulunan çözümün
#kodunu hazır fonksiyon kullanmadan yazınız
#çözüme bağıl hata payı e=10^-6 olana kadar devam ediniz
import math
def gecerli(x):
    return (x**3)+(4*x**2)-10

def ikiyebolme(a,b,iterasyon_sayısı):
    for n in range(iterasyon_sayısı):
        ikiyebol=(a+b)/2
        sonuc=gecerli(ikiyebol)
        print(f"{n+1}. iterasyon: x = {ikiyebol}, f(x) = {sonuc}")
        if gecerli(a)*sonuc<0:
            b=ikiyebol
        else:
            a=ikiyebol
        if(b-a)/2**n<10**-6:
            print(f"Çözüme yakınlık: {b-a/2**n}")
            break
    return (a+b)/2

a=1
b=2
if gecerli(a)*gecerli(b)<0:
    print("İkiye bölme metodu uygulanabilir\n")
    kok=ikiyebolme(a,b,4)
    print("Kök:", kok)
else:
    print("İkiye bölme metodu uygulanamaz\n")

