# Tugas Praktikum: Sistem Pakar Diagnosa Kerusakan Komputer/Laptop
import tkinter as tk
from tkinter import messagebox

# 1. Knowledge Base (Dictionary Aturan dan Solusi)
database_kerusakan = {
    "RAM Rusak atau Kotor": {
        "gejala": {"komputer_berbunyi_beep", "layar_blank_hitam", "sering_bluescreen"},
        "solusi": "Coba cabut RAM, bersihkan pin kuningnya dengan penghapus bersih, lalu pasang kembali."
    },
    "Power Supply (PSU) Lemah/Rusak": {
        "gejala": {"mati_mendadak_saat_berat", "bau_hangus", "mati_total"},
        "solusi": "Cek kabel power, coba gunakan PSU lain untuk memastikan, atau ganti PSU dengan daya yang memadai."
    },
    "Overheat (Prosesor Panas)": {
        "gejala": {"kipas_kencang", "mati_setelah_lama_menyala", "suhu_sangat_panas"},
        "solusi": "Bersihkan debu pada kipas atau heatsink prosesor, dan oleskan kembali thermal paste yang baru."
    },
    "VGA Bermasalah": {
        "gejala": {"garis_layar", "warna_kacau", "gambar_pecah"},
        "solusi": "Update driver VGA, pastikan kabel monitor terpasang kencang, bersihkan pin VGA, atau perbaiki ke tempat service."
    },
    "Hardisk/SSD Corrupt atau Rusak": {
        "gejala": {"booting_lambat", "bunyi_klik_disk", "pesan_boot_failure"},
        "solusi": "Ganti/periksa kabel SATA, jalankan Error Checking (chkdsk), dan segera backup data penting Anda selagi bisa."
    }
}

# 2. Daftar Pertanyaan Gejala yang terhubung dengan kode gejala
semua_gejala = {
    "komputer_berbunyi_beep": "Apakah komputer mengeluarkan bunyi beep berulang saat dinyalakan?",
    "layar_blank_hitam": "Apakah monitor/layar hanya blank hitam tanpa teks apapun?",
    "sering_bluescreen": "Apakah sistem sering mengalami hang atau Blue Screen of Death (BSOD)?",
    "mati_mendadak_saat_berat": "Apakah komputer sering mati tiba-tiba saat menjalankan aplikasi berat/game?",
    "bau_hangus": "Apakah tercium bau hangus atau komponen terbakar dari bagian casing?",
    "mati_total": "Apakah komputer tidak bereaksi sama sekali (mati total) saat tombol power ditekan?",
    "kipas_kencang": "Apakah suara kipas pendingin terdengar sangat bising atau berputar kencang?",
    "mati_setelah_lama_menyala": "Apakah komputer mati otomatis setelah beberapa saat digunakan (misal 15-30 menit)?",
    "suhu_sangat_panas": "Apakah suhu casing terasa panas yang tidak wajar?",
    "garis_layar": "Apakah muncul garis-garis aneh atau titik-titik (artifact) pada layar?",
    "warna_kacau": "Apakah warna layar menjadi kacau, pudar, atau tidak semestinya?",
    "gambar_pecah": "Apakah visual atau gambar menjadi patah-patah secara parah saat tes grafis/game?",
    "booting_lambat": "Apakah proses masuk ke sistem operasi (booting) terasa sangat lambat?",
    "bunyi_klik_disk": "Apakah terdengar bunyi 'klik' atau 'krek' terus-menerus pada media penyimpanan?",
    "pesan_boot_failure": "Apakah muncul pesan 'Disk boot failure' atau 'No bootable device' pada saat pertama kali menyala?"
}

class SistemPakarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Komputer")
        self.root.geometry("600x650")
        
        # Title Label
        title_lbl = tk.Label(root, text="Sistem Pakar Diagnosa Kerusakan Komputer", font=("Arial", 16, "bold"))
        title_lbl.pack(pady=10)
        
        inst_lbl = tk.Label(root, text="Centang gejala yang Anda alami pada komputer/laptop Anda:", font=("Arial", 10))
        inst_lbl.pack(pady=5)
        
        # Frame for checkboxes using Canvas and Scrollbar in case it exceeds window size
        container = tk.Frame(root)
        container.pack(fill="both", expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        
        self.scrollable_frame = tk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Variables to store checkbox states
        self.checkbox_vars = {}
        
        for kode, pertanyaan in semua_gejala.items():
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.scrollable_frame, text=pertanyaan, variable=var, font=("Arial", 10), wraplength=500, justify="left")
            chk.pack(anchor="w", pady=3)
            self.checkbox_vars[kode] = var
            
        # Button
        btn_diagnosa = tk.Button(root, text="Diagnosa Kerusakan", command=self.diagnosa, font=("Arial", 12, "bold"), bg="lightblue")
        btn_diagnosa.pack(pady=20)
        
    def diagnosa(self):
        gejala_pasien = set()
        for kode, var in self.checkbox_vars.items():
            if var.get():
                gejala_pasien.add(kode)
                
        penyakit_terdeteksi = []
        for nama_penyakit, data in database_kerusakan.items():
            gejala_syarat = data["gejala"]
            # Mengecek apakah seluruh syarat gejala suatu kerusakan terpenuhi oleh pengguna (Subset check)
            if gejala_syarat.issubset(gejala_pasien):
                penyakit_terdeteksi.append((nama_penyakit, data["solusi"]))
                
        if penyakit_terdeteksi:
            hasil_teks = "Berdasarkan gejala yang dipilih, terdeteksi:\n\n"
            for idx, (penyakit, solusi) in enumerate(penyakit_terdeteksi, 1):
                hasil_teks += f"{idx}. KERUSAKAN: {penyakit}\n   SOLUSI: {solusi}\n\n"
            messagebox.showinfo("Hasil Diagnosa", hasil_teks)
        else:
            msg = "Mohon maaf, sistem tidak dapat mendeteksi secara pasti kerusakan komputer Anda berdasarkan kombinasi gejala yang dimasukkan.\n\nSaran: Bawa komputer/laptop Anda ke tempat service terpercaya untuk pengecekan lebih lanjut."
            messagebox.showwarning("Hasil Diagnosa", msg)

def main():
    root = tk.Tk()
    app = SistemPakarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
