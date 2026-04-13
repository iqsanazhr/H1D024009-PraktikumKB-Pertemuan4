# Sistem Pakar Diagnosa Kerusakan Komputer/Laptop (GUI Tkinter)

Program ini adalah sebuah implementasi **Sistem Pakar** berbasis antarmuka grafis (GUI) menggunakan **Tkinter** pada Python. Program ini digunakan untuk mendiagnosa kerusakan perangkat keras (hardware) pada komputer atau laptop. Program memberikan kemudahan kepada pengguna dengan menyediakan daftar kumpulan gejala berbentuk *checkbox*, sehingga pengguna hanya perlu mencentang gejala yang dialami untuk mendapatkan hasil diagnosa berupa letak kerusakan dan anjuran solusinya.

## Komponen Utama Kode

Kode pada `tugas_sistem_pakar.py` terdiri dari beberapa komponen utama yang membentuk sistem pakar:

### 1. *Knowledge Base* (Basis Pengetahuan)
Basis pengetahuan disimpan dalam dictionary `database_kerusakan`. Dictionary ini berisi kumpulan jenis kerusakan umum pada komputer, di mana setiap jenis kerusakan memiliki dua atribut:
- **`gejala`**: Himpunan (*set*) dari kode-kode gejala yang menjadi prasyarat indikasi kerusakan tersebut.
- **`solusi`**: Teks solusi atau anjuran perbaikan.

Contoh kerusakan dalam basis pengetahuan antara lain: RAM Rusak, PSU Lemah, Overheat, VGA Bermasalah, dan Hardisk/SSD Corrupt.

### 2. Daftar Gejala (*Working Memory Data*)
Disimpan dalam dictionary `semua_gejala`, yang bertugas memetakan kode gejala (contoh: `"komputer_berbunyi_beep"`) menjadi kalimat penjabaran gejala yang ditampilkan di layar aplikasi GUI.

### 3. Antarmuka Grafis (GUI) dan Modul Akuisisi Fakta
Aplikasi ini membungkus alur kerjanya menggunakan pustaka `tkinter` (pada kelas `SistemPakarGUI`):
- Menampilkan seluruh gejala ke dalam layar menggunakan format widget *Checkbutton*.
- Setiap *Checkbutton* dihubungkan dengan *variable state* boolean. Jika pengguna mencentangnya, berarti nilainya *True*.
- Saat tombol **"Diagnosa Kerusakan"** ditekan, program akan menelusuri semua gejala yang tercentang (*True*) dan menambahkannya secara otomatis ke himpunan memori aktif bernama `gejala_pasien` untuk dianalisis.

### 4. Mesin Inferensi (*Inference Engine*)
Proses inferensi (pengambilan keputusan) dilakukan bersamaan di dalam metode `diagnosa()`:
```python
if gejala_syarat.issubset(gejala_pasien):
    penyakit_terdeteksi.append((nama_penyakit, data["solusi"]))
```
Logika yang digunakan merupakan pendekatan **Forward Chaining** sederhana berbasis pengecekan himpunan bagian (*Subset Check*). Mesin ini akan mengiterasi setiap jenis kerusakan di dalam *database* aturan, lalu memvalidasi apakah **keseluruhan** syarat gejala pada kerusakan tersebut telah terpenuhi (dicentang) oleh pengguna (`gejala_pasien`). 
Jika sebuah himpunan syarat gejala dari satu penyakit adalah *subset* dari daftar gejala yang dialami, penyakit tersebut masuk ke daftar terdeteksi.

### 5. Dialog Keputusan (Output)
Hasil deteksi nantinya ditembakkan dalam bentuk *Message Box* (jendela *pop-up* dialog pada Tkinter):
- Kategori Sukses: Jika kerusakan diketahui, program akan mencetak *pop-up* info berisi daftar kerusakan beserta solusinya.
- Kategori Peringatan (*Warning*): Jika kombinasi gejala tidak menunjukkan kerusakan tertentu pada aturan/basis pengetahuan, maka aplikasi memunculkan jendela teguran yang menyarankan *user* membawa perangkat ke tempat servis profesional.

## Cara Menjalankan Program

Posisikan *terminal* atau *command prompt* pada selasar folder `tugas`, lalu jalankan perintah berikut:
```bash
python tugas_sistem_pakar.py
```
Aplikasi (*window*) GUI akan terbuka. Anda cukup mencentang berbagai gejala yang relevan dengan keluhan, kemudian klik tombol **Diagnosa Kerusakan**. Hasil akan tampil dalam pesan dialog (*pop-up box*).

## Tampilan Program
Aplikasi dibuat sesederhana mungkin agar mudah dipahami:

![Tampilan GUI Sistem Pakar](output/gui.png)

![Tampilan Hasil Diagnosa](output/hasil.png)
