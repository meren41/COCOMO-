import tkinter as tk
from tkinter import ttk

def hesapla():
    try:
        # Kullanıcı girişlerini al
        kloc = float(kloc_entry.get())
        karmaşıklık = karmaşıklık_combobox.get()

        # Karmaşıklık seviyesine göre katsayıları belirle
        if karmaşıklık == "Ayrık":
            a_katsayısı, b_katsayısı, c_katsayısı, d_katsayısı = 2.4, 1.05, 2.50, 0.38
        elif karmaşıklık == "Yarı Gömülü":
            a_katsayısı, b_katsayısı, c_katsayısı, d_katsayısı = 3.0, 1.12, 2.50, 0.35
        elif karmaşıklık == "Gömülü":
            a_katsayısı, b_katsayısı, c_katsayısı, d_katsayısı = 3.6, 1.20, 2.50, 0.32

        # İş gücü hesapla
        iş_gücü = a_katsayısı * (kloc ** b_katsayısı)
        iş_gücü_label.config(text=f"İş Gücü: {iş_gücü:.2f} Kişi-Ay")

        # Geliştirme süresi hesapla
        geliştirme_süresi = c_katsayısı * (iş_gücü ** d_katsayısı)
        geliştirme_süresi_label.config(text=f"Geliştirme Süresi: {geliştirme_süresi:.2f} Ay")

        sonuç_label.config(text="")
    except ValueError:
        sonuç_label.config(text="Hatalı giriş! Lütfen sayıları doğru girin.")

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("Temel Model")

# Etiketler ve giriş kutularını oluştur
kloc_label = tk.Label(root, text="KLOC:")
kloc_label.grid(row=4, column=0, padx=10, pady=5)
kloc_entry = tk.Entry(root)
kloc_entry.grid(row=4, column=1, padx=10, pady=5)

karmaşıklık_label = tk.Label(root, text="Proje Karmaşıklığı:")
karmaşıklık_label.grid(row=5, column=0, padx=10, pady=5)
karmaşıklık_combobox = ttk.Combobox(root, values=["Ayrık", "Yarı Gömülü", "Gömülü"])
karmaşıklık_combobox.grid(row=5, column=1, padx=10, pady=5)

hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Sonuç etiketlerini oluştur
sonuç_label = tk.Label(root, text="")
sonuç_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

iş_gücü_label = tk.Label(root, text="")
iş_gücü_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

geliştirme_süresi_label = tk.Label(root, text="")
geliştirme_süresi_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# Uygulamayı başlat
root.mainloop()

