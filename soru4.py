''' 𝑓
 𝑥 =4𝑒^−0.5𝑥 −𝑥 denkleminin kökünü Newton-raphson ile
 başlangıç değeri 𝑥0 = 2 alarak 4 iterasyon sonucunda bulunuz.
 Bulunan çözümün kodunu hazır fonksiyon kullanmadan yazınız.
'''

import math
def f(x):
    return 4*math.exp(-0.5*x)-x
def f_turev(x):
    return -2*math.exp(-0.5*x)-1
def newton_raphson(x,iterasyon_sayisi):
    for n in range(iterasyon_sayisi):
        deger=x-(f(x)/f_turev(x))
        x=deger
        print(f"{n+1}. iterasyon değeri yaklaşık={x}\n")
    return deger
    
x=2
iterasyon_sayisi=4
newton_raphson(x,iterasyon_sayisi)







