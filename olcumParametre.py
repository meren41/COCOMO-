import tkinter as tk
import subprocess

def hesapla():
    # Kullanıcıdan metin kutuları aracılığıyla sayıları al
    Kullanıcı_Girdi = int(entry_kullanıcı_girdi.get())
    Kullanıcı_Çıktı = int(entry_kullanıcı_çıktı.get())
    Kullanıcı_Sorgu = int(entry_kullanıcı_sorgu.get())
    Kütük_Sayısı = int(entry_kütük_sayısı.get())
    Dışsal_Arayüz = int(entry_dışsal_arayüz.get())
    
    # Ağırlık faktörlerini seçilen radyo düğmesine göre al
    Kullanıcı_Girdi_Faktörü = faktör_seçici_kullanıcı_girdi.get()
    Kullanıcı_Çıktı_Faktörü = faktör_seçici_kullanıcı_çıktı.get()
    Kullanıcı_Sorgu_Faktörü = faktör_seçici_kullanıcı_sorgu.get()
    Kütük_Sayısı_Faktörü = faktör_seçici_kütük_sayısı.get()
    Dışsal_Arayüz_Faktörü = faktör_seçici_dışsal_arayüz.get()
    
    # Ağırlık faktörlerini belirle
    ağırlık_faktörleri = {
        'yalın': {'Kullanıcı_Girdi': 3, 'Kullanıcı_Çıktı': 4, 'Kullanıcı_Sorgu': 3, 'Kütük_Sayısı': 7, 'Dışsal_Arayüz': 5},
        'ortalama': {'Kullanıcı_Girdi': 4, 'Kullanıcı_Çıktı': 5, 'Kullanıcı_Sorgu': 4, 'Kütük_Sayısı': 10, 'Dışsal_Arayüz': 7},
        'karmaşık': {'Kullanıcı_Girdi': 6, 'Kullanıcı_Çıktı': 7, 'Kullanıcı_Sorgu': 6, 'Kütük_Sayısı': 15, 'Dışsal_Arayüz': 10}
    }
    
    # Her bir ölçüm parametresi için hesaplama
    toplam = 0
    toplam += ağırlık_faktörleri[Kullanıcı_Girdi_Faktörü]['Kullanıcı_Girdi'] * Kullanıcı_Girdi
    toplam += ağırlık_faktörleri[Kullanıcı_Çıktı_Faktörü]['Kullanıcı_Çıktı'] * Kullanıcı_Çıktı
    toplam += ağırlık_faktörleri[Kullanıcı_Sorgu_Faktörü]['Kullanıcı_Sorgu'] * Kullanıcı_Sorgu
    toplam += ağırlık_faktörleri[Kütük_Sayısı_Faktörü]['Kütük_Sayısı'] * Kütük_Sayısı
    toplam += ağırlık_faktörleri[Dışsal_Arayüz_Faktörü]['Dışsal_Arayüz'] * Dışsal_Arayüz
    
    # Toplamı göster
    label_sonuç.config(text=f"Toplam: {toplam}")
    
    # TKF değerini dosyaya kaydet
    with open("toplam_deger.txt", "w") as dosya:
        dosya.write(str(toplam))

def ac_tkfHesaplama():
    root.destroy()
    # tkfHesaplama.py dosyasını aç
    subprocess.run(["python", "tkfHesaplama.py"])

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("Ölçüm Parametreleri Hesaplama")

# Kullanıcı Girdi
label_kullanıcı_girdi = tk.Label(root, text="Kullanıcı Girdi Sayısı:")
label_kullanıcı_girdi.grid(row=0, column=0)
entry_kullanıcı_girdi = tk.Entry(root)
entry_kullanıcı_girdi.grid(row=0, column=1)

# Kullanıcı Çıktı
label_kullanıcı_çıktı = tk.Label(root, text="Kullanıcı Çıktı Sayısı:")
label_kullanıcı_çıktı.grid(row=1, column=0)
entry_kullanıcı_çıktı = tk.Entry(root)
entry_kullanıcı_çıktı.grid(row=1, column=1)

# Kullanıcı Sorgu
label_kullanıcı_sorgu = tk.Label(root, text="Kullanıcı Sorgu Sayısı:")
label_kullanıcı_sorgu.grid(row=2, column=0)
entry_kullanıcı_sorgu = tk.Entry(root)
entry_kullanıcı_sorgu.grid(row=2, column=1)

# Kütük Sayısı
label_kütük_sayısı = tk.Label(root, text="Kütük Sayısı:")
label_kütük_sayısı.grid(row=3, column=0)
entry_kütük_sayısı = tk.Entry(root)
entry_kütük_sayısı.grid(row=3, column=1)

# Dışsal Arayüz
label_dışsal_arayüz = tk.Label(root, text="Dışsal Arayüz Sayısı:")
label_dışsal_arayüz.grid(row=4, column=0)
entry_dışsal_arayüz = tk.Entry(root)
entry_dışsal_arayüz.grid(row=4, column=1)

# Ağırlık Faktörleri
faktör_seçici_kullanıcı_girdi = tk.StringVar(value = " ")
faktör_seçici_kullanıcı_çıktı = tk.StringVar(value = " ")
faktör_seçici_kullanıcı_sorgu = tk.StringVar(value = " ")
faktör_seçici_kütük_sayısı = tk.StringVar(value = " ")
faktör_seçici_dışsal_arayüz = tk.StringVar(value = " ")

# Kullanıcı Girdi
label_kullanıcı_girdi_faktör = tk.Label(root, text="Kullanıcı Girdi Ağırlık Faktörü:")
label_kullanıcı_girdi_faktör.grid(row=5, column=0)
radio_kullanıcı_girdi_yalın = tk.Radiobutton(root, text="Yalın", variable=faktör_seçici_kullanıcı_girdi, value='yalın')
radio_kullanıcı_girdi_yalın.grid(row=5, column=1)
radio_kullanıcı_girdi_ortalama = tk.Radiobutton(root, text="Ortalama", variable=faktör_seçici_kullanıcı_girdi, value='ortalama')
radio_kullanıcı_girdi_ortalama.grid(row=5, column=2)
radio_kullanıcı_girdi_karmaşık = tk.Radiobutton(root, text="Karmaşık", variable=faktör_seçici_kullanıcı_girdi, value='karmaşık')
radio_kullanıcı_girdi_karmaşık.grid(row=5, column=3)

# Kullanıcı Çıktı
label_kullanıcı_çıktı_faktör = tk.Label(root, text="Kullanıcı Çıktı Ağırlık Faktörü:")
label_kullanıcı_çıktı_faktör.grid(row=6, column=0)
radio_kullanıcı_çıktı_yalın = tk.Radiobutton(root, text="Yalın", variable=faktör_seçici_kullanıcı_çıktı, value='yalın')
radio_kullanıcı_çıktı_yalın.grid(row=6, column=1)
radio_kullanıcı_çıktı_ortalama = tk.Radiobutton(root, text="Ortalama", variable=faktör_seçici_kullanıcı_çıktı, value='ortalama')
radio_kullanıcı_çıktı_ortalama.grid(row=6, column=2)
radio_kullanıcı_çıktı_karmaşık = tk.Radiobutton(root, text="Karmaşık", variable=faktör_seçici_kullanıcı_çıktı, value='karmaşık')
radio_kullanıcı_çıktı_karmaşık.grid(row=6, column=3)

# Kullanıcı Sorgu
label_kullanıcı_sorgu_faktör = tk.Label(root, text="Kullanıcı Sorgu Ağırlık Faktörü:")
label_kullanıcı_sorgu_faktör.grid(row=7, column=0)
radio_kullanıcı_sorgu_yalın = tk.Radiobutton(root, text="Yalın", variable=faktör_seçici_kullanıcı_sorgu, value='yalın')
radio_kullanıcı_sorgu_yalın.grid(row=7, column=1)
radio_kullanıcı_sorgu_ortalama = tk.Radiobutton(root, text="Ortalama", variable=faktör_seçici_kullanıcı_sorgu, value='ortalama')
radio_kullanıcı_sorgu_ortalama.grid(row=7, column=2)
radio_kullanıcı_sorgu_karmaşık = tk.Radiobutton(root, text="Karmaşık", variable=faktör_seçici_kullanıcı_sorgu, value='karmaşık')
radio_kullanıcı_sorgu_karmaşık.grid(row=7, column=3)

# Kütük Sayısı
label_kütük_sayısı_faktör = tk.Label(root, text="Kütük Sayısı Ağırlık Faktörü:")
label_kütük_sayısı_faktör.grid(row=8, column=0)
radio_kütük_sayısı_yalın = tk.Radiobutton(root, text="Yalın", variable=faktör_seçici_kütük_sayısı, value='yalın')
radio_kütük_sayısı_yalın.grid(row=8, column=1)
radio_kütük_sayısı_ortalama = tk.Radiobutton(root, text="Ortalama", variable=faktör_seçici_kütük_sayısı, value='ortalama')
radio_kütük_sayısı_ortalama.grid(row=8, column=2)
radio_kütük_sayısı_karmaşık = tk.Radiobutton(root, text="Karmaşık", variable=faktör_seçici_kütük_sayısı, value='karmaşık')
radio_kütük_sayısı_karmaşık.grid(row=8, column=3)

# Dışsal Arayüz
label_dışsal_arayüz_faktör = tk.Label(root, text="Dışsal Arayüz Ağırlık Faktörü:")
label_dışsal_arayüz_faktör.grid(row=9, column=0)
radio_dışsal_arayüz_yalın = tk.Radiobutton(root, text="Yalın", variable=faktör_seçici_dışsal_arayüz, value='yalın')
radio_dışsal_arayüz_yalın.grid(row=9, column=1)
radio_dışsal_arayüz_ortalama = tk.Radiobutton(root, text="Ortalama", variable=faktör_seçici_dışsal_arayüz, value='ortalama')
radio_dışsal_arayüz_ortalama.grid(row=9, column=2)
radio_dışsal_arayüz_karmaşık = tk.Radiobutton(root, text="Karmaşık", variable=faktör_seçici_dışsal_arayüz, value='karmaşık')
radio_dışsal_arayüz_karmaşık.grid(row=9, column=3)

# Hesapla butonu
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
button_hesapla.grid(row=10, column=0, columnspan=4, pady=5)

# Sonuç
label_sonuç = tk.Label(root, text="")
label_sonuç.grid(row=11, column=0, columnspan=4)

# İleri butonu
button_ileri = tk.Button(root, text="İleri", command=ac_tkfHesaplama)
button_ileri.grid(row=12, column=0, columnspan=4, pady=5)

root.mainloop()
