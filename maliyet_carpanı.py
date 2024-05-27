import tkinter as tk
from tkinter import ttk

def hesapla_maliyet_carpimi():
    # K değerini dosyadan oku
    with open("k_degeri.txt", "r") as k_file:
        K_degeri = float(k_file.read().strip())
        
    secilen_degerler = {
        "RELY": combo_rely.get(),
        "DATA": combo_data.get(),
        "CPLX": combo_cplx.get(),
        "TIME": combo_time.get(),
        "STOR": combo_stor.get(),
        "VIRT": combo_virt.get(),
        "TURN": combo_turn.get(),
        "ACAP": combo_acap.get(),
        "AEXP": combo_aexp.get(),
        "PCAP": combo_pcap.get(),
        "VEXP": combo_vexp.get(),
        "LEXP": combo_lexp.get(),
        "MODP": combo_modp.get(),
        "TOOL": combo_tool.get(),
        "SCED": combo_sced.get()
    }

    carpanlar = {
        "RELY": {"Çok Düşük": 0.75, "Düşük": 0.88, "Normal": 1.00, "Yüksek": 1.15, "Çok Yüksek": 1.40, "Oldukça Yüksek": 1.00},
        "DATA": {"Çok Düşük": 1.00, "Düşük": 0.94, "Normal": 1.00, "Yüksek": 1.08, "Çok Yüksek": 1.16, "Oldukça Yüksek": 1.00},
        "CPLX": {"Çok Düşük": 0.70, "Düşük": 0.85, "Normal": 1.00, "Yüksek": 1.15, "Çok Yüksek": 1.30, "Oldukça Yüksek": 1.65},
        "TIME": {"Çok Düşük": 1.00, "Düşük": 1.00, "Normal": 1.00, "Yüksek": 1.11, "Çok Yüksek": 1.30, "Oldukça Yüksek": 1.66},
        "STOR": {"Çok Düşük": 1.00, "Düşük": 1.00, "Normal": 1.00, "Yüksek": 1.06, "Çok Yüksek": 1.21, "Oldukça Yüksek": 1.56},
        "VIRT": {"Çok Düşük": 1.00, "Düşük": 0.87, "Normal": 1.00, "Yüksek": 1.15, "Çok Yüksek": 1.30, "Oldukça Yüksek": 1.00},
        "TURN": {"Çok Düşük": 1.00, "Düşük": 0.87, "Normal": 1.00, "Yüksek": 1.07, "Çok Yüksek": 1.15, "Oldukça Yüksek": 1.00},
        "ACAP": {"Çok Düşük": 1.46, "Düşük": 0.19, "Normal": 1.00, "Yüksek": 0.86, "Çok Yüksek": 0.71, "Oldukça Yüksek": 1.00},
        "AEXP": {"Çok Düşük": 1.29, "Düşük": 1.13, "Normal": 1.00, "Yüksek": 0.91, "Çok Yüksek": 0.82, "Oldukça Yüksek": 1.00},
        "PCAP": {"Çok Düşük": 1.42, "Düşük": 1.17, "Normal": 1.00, "Yüksek": 0.86, "Çok Yüksek": 0.70, "Oldukça Yüksek": 1.00},
        "VEXP": {"Çok Düşük": 1.21, "Düşük": 1.10, "Normal": 1.00, "Yüksek": 0.90, "Çok Yüksek": 1.00, "Oldukça Yüksek": 1.00},
        "LEXP": {"Çok Düşük": 1.14, "Düşük": 1.07, "Normal": 1.00, "Yüksek": 0.95, "Çok Yüksek": 1.00, "Oldukça Yüksek": 1.00},
        "MODP": {"Çok Düşük": 1.24, "Düşük": 1.10, "Normal": 1.00, "Yüksek": 0.91, "Çok Yüksek": 0.82, "Oldukça Yüksek": 1.00},
        "TOOL": {"Çok Düşük": 1.24, "Düşük": 1.10, "Normal": 1.00, "Yüksek": 0.91, "Çok Yüksek": 0.83, "Oldukça Yüksek": 1.00},
        "SCED": {"Çok Düşük": 1.23, "Düşük": 1.08, "Normal": 1.00, "Yüksek": 1.04, "Çok Yüksek": 1.10, "Oldukça Yüksek": 1.00}
    }

    maliyet_carpani = 1.0
    for etmen, deger in secilen_degerler.items():
        maliyet_carpani *= carpanlar[etmen][deger]
        label_sonuc.config(text=f"Maliyet Çarpanı: {maliyet_carpani:.2f}")
    
    
    # KD değerini hesapla ve ekrana yazdır
    Kd_degeri = K_degeri * maliyet_carpani
    label_sonuc.config(text=f"Maliyet Çarpanı: {maliyet_carpani:.2f}\nKd Değeri: {Kd_degeri:.2f}")


root = tk.Tk()
root.title("Maliyet Çarpanı Hesaplama")

row = 0

# Ürün Özellikleri
tk.Label(root, text="Ürün Özellikleri").grid(row=row, columnspan=2)
row += 1

combo_rely = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_rely.grid(row=row, column=0)
combo_rely.current(0)
tk.Label(root, text="RELY").grid(row=row, column=1)
row += 1

combo_data = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_data.grid(row=row, column=0)
combo_data.current(0)
tk.Label(root, text="DATA").grid(row=row, column=1)
row += 1

combo_cplx = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_cplx.grid(row=row, column=0)
combo_cplx.current(0)
tk.Label(root, text="CPLX").grid(row=row, column=1)
row += 1

# Bilgisayar Özellikleri
tk.Label(root, text="Bilgisayar Özellikleri").grid(row=row, columnspan=2)
row += 1

combo_time = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_time.grid(row=row, column=0)
combo_time.current(0)
tk.Label(root, text="TIME").grid(row=row, column=1)
row += 1

combo_stor = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_stor.grid(row=row, column=0)
combo_stor.current(0)
tk.Label(root, text="STOR").grid(row=row, column=1)
row += 1

combo_virt = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_virt.grid(row=row, column=0)
combo_virt.current(0)
tk.Label(root, text="VIRT").grid(row=row, column=1)
row += 1

combo_turn = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_turn.grid(row=row, column=0)
combo_turn.current(0)
tk.Label(root, text="TURN").grid(row=row, column=1)
row += 1

# Personel Özellikleri
tk.Label(root, text="Personel Özellikleri").grid(row=row, columnspan=2)
row += 1

combo_acap = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_acap.grid(row=row, column=0)
combo_acap.current(0)
tk.Label(root, text="ACAP").grid(row=row, column=1)
row += 1

combo_aexp = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_aexp.grid(row=row, column=0)
combo_aexp.current(0)
tk.Label(root, text="AEXP").grid(row=row, column=1)
row += 1

combo_pcap = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_pcap.grid(row=row, column=0)
combo_pcap.current(0)
tk.Label(root, text="PCAP").grid(row=row, column=1)
row += 1

combo_vexp = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_vexp.grid(row=row, column=0)
combo_vexp.current(0)
tk.Label(root, text="VEXP").grid(row=row, column=1)
row += 1

combo_lexp = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_lexp.grid(row=row, column=0)
combo_lexp.current(0)
tk.Label(root, text="LEXP").grid(row=row, column=1)
row += 1

# Proje Özellikleri
tk.Label(root, text="Proje Özellikleri").grid(row=row, columnspan=2)
row += 1

combo_modp = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_modp.grid(row=row, column=0)
combo_modp.current(0)
tk.Label(root, text="MODP").grid(row=row, column=1)
row += 1

combo_tool = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_tool.grid(row=row, column=0)
combo_tool.current(0)
tk.Label(root, text="TOOL").grid(row=row, column=1)
row += 1

combo_sced = ttk.Combobox(root, values=("Çok Düşük", "Düşük", "Normal", "Yüksek", "Çok Yüksek", "Oldukça Yüksek"))
combo_sced.grid(row=row, column=0)
combo_sced.current(0)
tk.Label(root, text="SCED").grid(row=row, column=1)
row += 1

# Hesapla düğmesi
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla_maliyet_carpimi)
button_hesapla.grid(row=row, columnspan=2)
row += 1

# Sonuç etiketi
label_sonuc = tk.Label(root, text="")
label_sonuc.grid(row=row, columnspan=2)

root.mainloop()
