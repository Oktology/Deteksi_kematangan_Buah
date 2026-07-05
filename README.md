 🌿 Deteksi Penyakit Daun

Aplikasi web berbasis Streamlit yang memanfaatkan Groq Vision API (Llama 3.2 90B Vision Preview) untuk menganalisis kondisi daun tanaman dari gambar yang diambil menggunakan kamera. Aplikasi ini dapat membantu mengidentifikasi apakah daun dalam kondisi sehat atau mengalami penyakit serta memberikan rekomendasi perawatan.

 📌 Fitur

* Landing page sederhana dan mudah digunakan.
* Mengambil gambar daun menggunakan kamera (`st.camera_input`).
* Preview gambar sebelum dianalisis.
* Analisis gambar menggunakan Gemini.
* Menampilkan hasil identifikasi dalam format yang mudah dibaca.
* Informasi yang ditampilkan meliputi:

  * Nama tanaman
  * Status tanaman (Sehat/Sakit)
  * Nama penyakit (jika ada)
  * Deskripsi tekstur daun
  * Rekomendasi perawatan
* Penanganan error untuk kegagalan API maupun parsing JSON.

---

🛠️ Teknologi yang Digunakan

* Python
* Streamlit
* Gemini API
* gemini-2.5-flash
* JSON

---

📂 Struktur Proyek

```text
Deteksi-Penyakit-Daun/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

---

 🚀 Instalasi

Clone repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Masuk ke folder proyek:

```bash
cd REPOSITORY
```

Buat virtual environment:

Windows

```bash
python -m venv venv
```

Aktifkan virtual environment:

Command Prompt

```bash
venv\Scripts\activate
```

Install dependensi:

```bash
pip install -r requirements.txt
```

---

🔑 Konfigurasi API Key

Buat folder `.streamlit`, kemudian buat file `secrets.toml`.

Isi file tersebut dengan API Key Gemini:

```toml
GEMINI_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

▶️ Menjalankan Aplikasi

Jalankan perintah berikut:

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```

---

📖 Cara Menggunakan

1. Jalankan aplikasi.
2. Klik tombol Mulai Deteksi.
3. Ambil foto daun menggunakan kamera.
4. Pastikan gambar sudah jelas.
5. Klik Analisis Daun.
6. Tunggu hingga proses analisis selesai.
7. Hasil analisis akan menampilkan:

   * Nama tanaman
   * Status kesehatan
   * Penyakit (jika ada)
   * Deskripsi tekstur daun
   * Rekomendasi perawatan

---
📸 Tampilan Aplikasi

Tambahkan screenshot aplikasi pada folder repository, misalnya:

```
images/
├── landing-page.png
├── camera-page.png
└── result-page.png
```

Kemudian tampilkan pada README:

```markdown
Halaman Analisis

![Analisis](images/halaman%20analisis.png)

Hasil Deteksi

![Hasil](images/hasil%20analisis.png)
```

---

📦 Dependencies

streamlit
Gemini

Seluruh dependensi dapat diinstal menggunakan:

```bash
pip install -r requirements.txt
```

👨‍💻 Pengembang

Nama: Octoryo Qoffanus Shidqi

Program Studi: Informatika

Universitas: Universitas Pancasakti Tegal

📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan tugas akademik.
