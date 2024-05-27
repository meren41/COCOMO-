import tkinter as tk
import subprocess

def hesapla_tkf():
    cevaplar = [entry.get() for entry in entryler]
    tkf = sum(map(int, cevaplar))
    label_sonuç.config(text=f"Teknik Karmaşıklık Faktörü (TKF): {tkf}")
    
    # TKF değerini dosyaya kaydet
    with open("tkf_degeri.txt", "w") as dosya:
        dosya.write(str(tkf))

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("Teknik Karmaşıklık Faktörü (TKF) Hesaplama")

# Soruları içeren etiketler ve metin kutuları oluştur
sorular = [
    "1. Uygulama, güvenilir yedekleme ve kurtarma gerektiriyor mu?",
    "2. Veri iletişimi gerektiriyor mu?",
    "3. Dağıtılmış İşlemler var mı?",
    "4. Performans kritik mi?",
    "5. Girdiler, çıktılar, dosyalar ya da sorgular karmaşık mı?",
    "6. İçsel işlemler karmaşık mı?",
    "7. Tasarlanacak kod yeniden kullanılabilir mi?",
    "8. Dönüştürme ve kurulun tasarımda dikkate alınacak mı?"
]

etiketler = []
entryler = []
for i, soru in enumerate(sorular):
    etiket = tk.Label(root, text=soru)
    etiket.grid(row=i, column=0, sticky="w", padx=5, pady=5)
    etiketler.append(etiket)
    
    # Radio butonlarını oluştur
    var = tk.IntVar()
    for j in range(1, 6):
        radio = tk.Radiobutton(root, text=str(j), variable=var, value=j)
        radio.grid(row=i, column=j, padx=5, pady=5)
    entryler.append(var)

def ac_InHesaplama():
    root.destroy()
    # InHesaplama.py dosyasını aç
    subprocess.run(["python", "InHesaplama.py"])

# Hesapla butonu
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla_tkf)
button_hesapla.grid(row=len(sorular), column=0, columnspan=6, pady=10)

# Sonuç etiketi
label_sonuç = tk.Label(root, text="")
label_sonuç.grid(row=len(sorular)+1, column=0, columnspan=6)

# İleri butonu
button_ileri = tk.Button(root, text="İleri", command=ac_InHesaplama)
button_ileri.grid(row=len(sorular)+2, column=0, columnspan=6, pady=5)

root.mainloop()
