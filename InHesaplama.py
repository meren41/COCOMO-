import tkinter as tk
import subprocess

def hesapla_in():
    # Toplam değeri dosyadan oku
    with open("toplam_deger.txt", "r") as ain_file:
        ain = float(ain_file.read().strip())

    # TKF değerini dosyadan oku
    with open("tkf_degeri.txt", "r") as tkf_file:
        tkf = float(tkf_file.read().strip())

    # İn değerini hesapla
    in_degeri = ain * (0.65 + 0.01 * tkf)

    # İn değerini ekrana yazdır
    label_in_sonuc.config(text=f"İn Değeri: {in_degeri:.2f}")

    # Dil seçimi yapıldıktan sonra hesaplama butonunu aktif hale getir
    button_hesapla_satir_sayisi.config(state=tk.NORMAL)

def hesapla_satir_sayisi():
    # Seçilen dilin ağırlık değerini al
    secilen_dil = secim_dil.get()
    dil_ağırlıkları = {
        "Assembly": 300,
        "Cobol": 100,
        "Fortran": 100,
        "Pascal": 90,
        "C": 90,
        "Ada": 70,
        "Nesne Kökenli Diller": 30,
        "4. Kuşak Diller": 15,
        "Kod Üreticiler": 15
    }

    ağırlık = dil_ağırlıkları.get(secilen_dil, 0)

    # İn değerini al
    in_degeri = float(label_in_sonuc.cget("text").split(":")[1].strip())

    # Satır sayısını hesapla
    satir_sayisi = in_degeri * ağırlık

    # Satır sayısını ekrana yazdır
    label_satir_sayisi_sonuc.config(text=f"Satır Sayısı: {satir_sayisi:.2f}")

def hesapla_K_degeri():
    # Proje tipini al
    proje_tipi = secim_proje_tipi.get()

    # Satır sayısını al
    satir_sayisi = float(label_satir_sayisi_sonuc.cget("text").split(":")[1].strip())

    # K değerini hesapla
    if proje_tipi == "Ayrık Projeler":
        K_degeri = 3.2 * satir_sayisi ** 1.05
    elif proje_tipi == "Yarı Gömülü Projeler":
        K_degeri = 3.0 * satir_sayisi ** 1.12
    elif proje_tipi == "Gömülü Projeler":
        K_degeri = 2.8 * satir_sayisi ** 1.20
    else:
        K_degeri = 0
        
    # K değerini dosyaya yaz
    with open("k_degeri.txt", "w") as k_file:
        k_file.write(str(K_degeri))

    # K değerini ekrana yazdır
    label_K_sonuc.config(text=f"K Değeri: {K_degeri:.2f}")
    
def ac_maliyet():
    root.destroy()
    # tkfHesaplama.py dosyasını aç
    subprocess.run(["python", "maliyet_carpanı.py"])

# Yeni Tkinter penceresi oluştur
root = tk.Tk()
root.title("İn Değeri, Satır Sayısı ve K Değeri Hesaplama")

# İn hesapla butonu
button_hesapla_in = tk.Button(root, text="İn Değerini Hesapla", command=hesapla_in)
button_hesapla_in.pack(pady=10)

# İn değerini gösterecek etiket
label_in_sonuc = tk.Label(root, text="")
label_in_sonuc.pack(pady=5)

# Yazılım dilini seçme alanı
secim_dil = tk.StringVar()
secim_dil.set("Assembly")  # Başlangıçta Assembly seçili olarak göster

label_dil = tk.Label(root, text="Yazılım Dilini Seçin:")
label_dil.pack()

# Seçenekleri içeren açılır menüyü oluştur
menu = tk.OptionMenu(root, secim_dil, "Assembly", "Cobol", "Fortran", "Pascal", "C", "Ada", "Nesne Kökenli Diller", "4. Kuşak Diller", "Kod Üreticiler")
menu.pack()

# Satır sayısını hesapla butonu (ilk başta devre dışı)
button_hesapla_satir_sayisi = tk.Button(root, text="Satır Sayısını Hesapla", command=hesapla_satir_sayisi, state=tk.DISABLED)
button_hesapla_satir_sayisi.pack(pady=10)

# Satır sayısını gösterecek etiket
label_satir_sayisi_sonuc = tk.Label(root, text="")
label_satir_sayisi_sonuc.pack(pady=5)

# Proje tipini seçme alanı
secim_proje_tipi = tk.StringVar()
secim_proje_tipi.set("Ayrık Projeler")  # Başlangıçta Ayrık Projeler seçili olarak göster

label_proje_tipi = tk.Label(root, text="Proje Tipini Seçin:")
label_proje_tipi.pack()

# Seçenekleri içeren açılır menüyü oluştur
menu_proje_tipi = tk.OptionMenu(root, secim_proje_tipi, "Ayrık Projeler", "Yarı Gömülü Projeler", "Gömülü Projeler")
menu_proje_tipi.pack()

# K değerini hesapla butonu
button_hesapla_K_degeri = tk.Button(root,text="K Değerini Hesapla", command=hesapla_K_degeri)
button_hesapla_K_degeri.pack(pady=10)

# K değerini gösterecek etiket
label_K_sonuc = tk.Label(root, text="")
label_K_sonuc.pack(pady=5)

# İleri butonu
button_ileri = tk.Button(root, text="İleri", command=ac_maliyet)
button_ileri.pack(pady=5)

# Yeni pencereyi aç
root.mainloop()
