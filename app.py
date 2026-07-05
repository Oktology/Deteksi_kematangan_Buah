# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Fruit Ripeness AI",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# GEMINI API
# ==========================================================

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []
if "result" not in st.session_state:
    st.session_state.result = None
# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Background utama */
.stApp{
    background: background: linear-gradient(135deg, #1E1F29, #15161E);

}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#1E1E2E;
}

/* Semua tulisan default */
html, body, [class*="css"]{
    color:#FFFFFF;
}

/* Judul */
h1,h2,h3,h4,h5,h6{
    color:#1B5E20 !important;
    font-weight:bold;
}

/* Card */
.card{
    background:#1E1E2E;
    padding:20px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}

/* Metric */
[data-testid="stMetric"]{
    background:#1E1E2E;
    border-radius:15px;
    padding:15px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}

/* Tombol */
.stButton>button{
    background:#2E7D32;
    color:#1E1E2E;
    border:none;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1B5E20;
}

/* Progress */
.stProgress > div > div > div{
    background:#4CAF50;
}

/* Hilangkan menu Streamlit */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# FUNCTION
# ==========================================================

def clean_json(text):

    """
    Membersihkan markdown ```json dari Gemini
    """

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    start = text.find("{")
    end = text.rfind("}") + 1

    return json.loads(text[start:end])
# ==========================================================
# FUNCTION ANALISIS GEMINI
# ==========================================================

def analyze_image(image_bytes):
    """
    Mengirim gambar ke Gemini dan mengembalikan hasil JSON
    """

    prompt = """
Kamu adalah seorang ahli hortikultura dan quality control buah.

Analisis gambar buah yang diberikan.

Balas HANYA dalam format JSON valid.

JANGAN menggunakan markdown.
JANGAN menggunakan ```json.
JANGAN menambahkan penjelasan.

Format JSON WAJIB:

{
    "buah":"Nama Buah",
    "tingkat_kematangan":"Mentah/Setengah Matang/Matang/Terlalu Matang",
    "persentase_kematangan":80,
    "confidence":95,
    "warna":"Deskripsi warna buah",
    "tekstur":"Deskripsi tekstur kulit buah",
    "kualitas":"Baik/Cukup/Kurang Baik",
    "saran":"Saran penyimpanan atau konsumsi"
}
"""

    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/jpeg",
                "data": image_bytes,
            },
        ],
        generation_config=genai.GenerationConfig(
            temperature=0.2
        ),
    )

    result = clean_json(response.text)

    return result
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🍎 Fruit AI")

    st.success("Gemini 2.5 Flash")

    st.write("")

    st.markdown("### 📊 Statistik")

    st.metric(
        "Jumlah Analisis",
        len(st.session_state.history)
    )

    st.write("")

    st.markdown("### 📜 Riwayat")

    if len(st.session_state.history) == 0:

        st.info("Belum ada analisis")

    else:

        for item in st.session_state.history[::-1]:

            st.write(
                f"• {item['buah']} ({item['tingkat_kematangan']})"
            )

    st.write("")

    if st.button(
        "🗑 Bersihkan Riwayat",
        use_container_width=True
    ):

        st.session_state.history = []

        st.rerun()

# ==========================================================
# HEADER
# ==========================================================
col1,col2,col3 = st.columns(3)

with col1:
    st.info("🤖 Gemini 2.5 Flash")

with col2:
    st.info("📷 Vision AI")

with col3:
    st.info("⚡ Real Time Analysis")
col1, col2 = st.columns([5,1])

with col1:

    st.markdown("""
<div class='card'>

<div class='title'>
🍎 Fruit Ripeness Detection AI
</div>

<div class='subtitle'>
Deteksi tingkat kematangan buah menggunakan Google Gemini Vision AI.
</div>

</div>
""", unsafe_allow_html=True)

    st.markdown(
        "<div class='subtitle'>Analisis kematangan buah menggunakan Google Gemini Vision AI.</div>",
        unsafe_allow_html=True
    )

with col2:

    st.info(
        datetime.now().strftime("%d/%m/%Y")
    )

st.divider()

# ==========================================================
# PILIH SUMBER GAMBAR
# ==========================================================

st.subheader("📸 Masukkan Gambar Buah")

tab_camera, tab_upload = st.tabs(
    [
        "📷 Kamera",
        "🖼 Upload"
    ]
)

photo = None

with tab_camera:

    photo = st.camera_input(
        "Ambil foto buah"
    )

with tab_upload:

    uploaded = st.file_uploader(
        "Upload gambar",
        type=["jpg","jpeg","png"]
    )

    if uploaded is not None:

        photo = uploaded

# ==========================================================
# PREVIEW
# ==========================================================

if photo is not None:

    st.divider()

    st.subheader("🖼 Preview Buah")

    st.image(
        photo,
        caption="Gambar yang akan dianalisis",
        use_container_width=True
    )

    if st.button(
        "🚀 Analisis Tingkat Kematangan",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner("🧠 Gemini AI sedang menganalisis gambar..."):

            try:
                image_bytes = photo.getvalue()

                result = analyze_image(image_bytes)

                # Simpan ke history
                st.session_state.history.append(result)

                # Simpan hasil agar bisa ditampilkan
                st.session_state.result = result

                st.success("✅ Analisis berhasil!")
                st.balloons()

            except Exception as e:

                st.error(f"Terjadi kesalahan:\n\n{e}")
# ==========================================================
# TAMPILKAN HASIL ANALISIS
# ==========================================================

if st.session_state.result is not None:

    result = st.session_state.result

    buah = result.get("buah", "-")
    tingkat = result.get("tingkat_kematangan", "-")
    persentase = int(result.get("persentase_kematangan", 0))
    confidence = int(result.get("confidence", 0))
    warna = result.get("warna", "-")
    tekstur = result.get("tekstur", "-")
    kualitas = result.get("kualitas", "-")
    saran = result.get("saran", "-")

    st.divider()

    st.header("📊 Hasil Analisis AI")

    # ==========================================
    # STATUS
    # ==========================================

    status = tingkat.lower()

    if status == "mentah":
        st.info("🟦 Buah Masih Mentah")

    elif "setengah" in status:
        st.warning("🟨 Buah Setengah Matang")

    elif status == "matang":
        st.success("🟩 Buah Sudah Matang")

    else:
        st.error("🟥 Buah Terlalu Matang")

    # ==========================================
    # METRIC
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🍎 Nama Buah",
            buah
        )

    with col2:
        st.metric(
            "📈 Kematangan",
            f"{persentase}%"
        )

    with col3:
        st.metric(
            "🎯 Confidence",
            f"{confidence}%"
        )

    # ==========================================
    # PROGRESS BAR
    # ==========================================

    st.write("### 📊 Tingkat Kematangan")

    st.progress(persentase)

    # ==========================================
    # DETAIL
    # ==========================================

    kiri, kanan = st.columns(2)

    with kiri:

        st.markdown("### 🎨 Warna")

        st.info(warna)

        st.markdown("### 🍃 Tekstur")

        st.info(tekstur)

    with kanan:

        st.markdown("### ⭐ Kualitas")

        if kualitas.lower() == "baik":

            st.success(kualitas)

        elif kualitas.lower() == "cukup":

            st.warning(kualitas)

        else:

            st.error(kualitas)

        st.markdown("### 💡 Saran")

        st.write(saran)

    # ==========================================
    # RINGKASAN
    # ==========================================

    st.divider()

    st.subheader("📄 Ringkasan")

    st.write(
        f"""
Buah berhasil dikenali sebagai **{buah}**.

AI memperkirakan tingkat kematangan **{tingkat}**
dengan persentase **{persentase}%**.

Model memiliki tingkat keyakinan
**{confidence}%**.

Kondisi buah dinilai **{kualitas}**.
"""
    )

    # ==========================================
    # DOWNLOAD JSON
    # ==========================================

    st.download_button(
        label="📥 Download Hasil JSON",
        data=json.dumps(result, indent=4, ensure_ascii=False),
        file_name=f"{buah}.json",
        mime="application/json",
        use_container_width=True
    )

    # ==========================================
    # JSON DEBUG
    # ==========================================

    with st.expander("📄 Lihat JSON dari Gemini"):

        st.json(result)
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<hr>

<center>

### 🍎 Fruit Ripeness Detection AI

Powered by **Google Gemini 2.5 Flash**

Developed with ❤️ using Streamlit

</center>
""", unsafe_allow_html=True)