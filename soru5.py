
import pandas as pd
import matplotlib.pyplot as plt

df_csv = pd.read_csv('Kidem_ve_Maas_VeriSeti.csv')
print(df_csv.head())
plt.figure(figsize=(10,6))
plt.scatter(df_csv['Kidem'], df_csv['Maas'], color='blue', label='Veri Noktaları')
plt.title('Kıdem ve Maaş İlişkisi')
plt.xlabel('Kıdem ')
plt.ylabel('Maaş ')
plt.show()

def linear_regression(x, b, w):
    return w*x+b

def maliyet_fonksiyonu(x,y,w,b):
    m=len(y)#veri setindeki örnek sayısı
    y_tahmin=linear_regression(x,b,w)
    maliyet=(1/(2*m))*sum((y_tahmin-y)**2)
    return maliyet

def gradyaninişi(x,y,w,b,öğrenme_oranı,epok_sayısı):
    m=len(y)
    for i in range(epok_sayısı):
        y_tahmin=linear_regression(x,b,w)
        dw=(1/m)*sum((y_tahmin-y)*x)
        db=(1/m)*sum(y_tahmin-y)
        w=w-öğrenme_oranı*dw
        b=b-öğrenme_oranı*db
    return w,b

#model eğitimi
w,b=gradyaninişi(df_csv['Kidem'],df_csv['Maas'], w=0,b=0,öğrenme_oranı=0.001,epok_sayısı=1000)

y_tahmin=linear_regression(df_csv['Kidem'],b,w)

#görsel gösterim
plt.figure(figsize=(10,6))#grafik boyutunu ayarlama
plt.scatter(df_csv['Kidem'], df_csv['Maas'], color='blue', label='Veri Noktaları')
plt.plot(df_csv['Kidem'], y_tahmin, color='red', label='Regresyon Doğrusu')#regresyon doğrusunu çizme
plt.title('Kıdem ve Maaş İlişkisi - Regresyon Doğrusu')#başlık
plt.xlabel('Kıdem ')#eksen ismi
plt.ylabel('Maaş ')
plt.legend()#grafige açıklama ekleme hangi nokta neyi temsil ediyor
plt.show()#grafiği gösterme

mse=maliyet_fonksiyonu(df_csv['Kidem'],df_csv['Maas'],w,b)
print("final mse",mse)

#R2 değeri hesaplama 
y=df_csv['Maas']
y_tahmin=linear_regression(df_csv['Kidem'],b,w)
res=sum((y-y_tahmin)**2)
tot=sum((y-y.mean())**2)
r2=1-(res/tot)
print("R2 değeri:",r2)

print("5 yıl kıdem için maaş tahmini:",linear_regression(5,b,w))
print("7,5 yıl kıdem için maaş tahmini:",linear_regression(7.5,b,w))
print("12 yıl kıdem için maaş tahmini:",linear_regression(12,b,w))






    

    

