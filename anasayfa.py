import tkinter as tk
import subprocess

def run_temel_model():
    # Temel model dosyasını çalıştır
    subprocess.run(["python", "temelModel.py"])

def run_ara_model():
    # Ara model dosyasını çalıştır
    subprocess.run(["python", "olcumParametre.py"])

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("Maliyet Hesaplama")

# Üstteki satır
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Üstteki yazı
header_label = tk.Label(top_frame, text="Hangi model ile hesaplama yapmak istersiniz?", fg="black")
header_label.pack()

# Altta yanyana sıralanan butonlar için bir frame oluştur
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Temel Model butonu
temel_model_button = tk.Button(button_frame, text="Temel Model", command=run_temel_model)
temel_model_button.pack(side="left", padx=5)

# Ara Model butonu
ara_model_button = tk.Button(button_frame, text="Ara Model", command=run_ara_model)
ara_model_button.pack(side="left", padx=5)

# Sonuç etiketi
result_label = tk.Label(root, text="", fg="green")
result_label.pack(pady=10)

# Uygulamayı başlat
root.mainloop()
