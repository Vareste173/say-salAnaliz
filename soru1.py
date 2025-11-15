#cos𝑥 fonksiyonunun Taylor serisini hesaplayarak, 
#𝜋/5 noktasındaki değerini;
# b) Python kodunu da yazınız (Github). 
import math
#eger taylor serisini otomatik üretmek isterseniz sympy kütüphanesini kullanabilirsiniz
def taylor_cos(x,n_terms):
    result = 0
    for n in range(n_terms):
        coeff = (-1)**n
        num = x**(2*n)
        denom = math.factorial(2*n)
        result += coeff * (num / denom)
    return result
#x:cos(x) fonksiyonunun radyan cinsinden hesaplanacağı nokta
#n_terms:taylor serisinde kaç terim kullanılacağı
x=math.pi/5
gercek_deger=math.cos(x)
terim1=taylor_cos(x,1)
terim2=taylor_cos(x,2)
print("Gerçek değer:", gercek_deger)
print("1 terimle:", terim1)
print("2 terimle:", terim2)
print("Kesme hatası (1 terim):", abs(gercek_deger - terim1))
print("Kesme hatası (2 terim):", abs(gercek_deger - terim2))