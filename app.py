import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Heat Transfer Lab UTHM",
    page_icon="🔥",
    layout="wide"
)

# 2. Suntikan CSS untuk Gaya (Styling)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .hero-section {
        background: linear-gradient(135deg, #003366 0%, #00509d 100%);
        padding: 3rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .icon-box {
        font-size: 50px;
        margin-bottom: 10px;
    }
    .module-card {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        border-top: 5px solid #003366;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
        text-align: center;
        transition: transform 0.3s;
    }
    .module-card:hover {
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hero Section (Ganti Imej dengan Ikon Besar)
st.markdown("""
    <div class="hero-section">
        <div style="font-size: 70px;">🌡️</div>
        <h1>Portal Pembelajaran Interaktif Heat Transfer</h1>
        <p>Fakulti Kejuruteraan Mekanikal dan Pembuatan, UTHM</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Pengenalan Ringkas
st.write("<br>", unsafe_allow_html=True)
col_intro, col_tips = st.columns([2, 1])

with col_intro:
    st.subheader("Selamat Datang!")
    st.write("""
    Aplikasi ini menyediakan simulasi digital untuk membantu anda memahami 
    mekanisme pemindahan haba secara praktikal. Sila navigasi ke modul 
    pilihan anda melalui menu di sebelah kiri.
    """)

with col_tips:
    st.info("💡 **Tips:** Anda boleh menukar parameter input dalam setiap modul untuk melihat kesan perubahan suhu secara real-time.")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Bahagian Modul (Ikonik Cards)
st.subheader("🚀 Modul Tersedia")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="module-card">
        <div class="icon-box">🔥</div>
        <h3>Modul 1</h3>
        <p><b>Hukum Fourier</b></p>
        <hr>
        <p>Analisis konduksi satu dimensi bagi bahan tunggal.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="module-card">
        <div class="icon-box">🧱</div>
        <h3>Modul 2</h3>
        <p><b>Dinding Berlapis</b></p>
        <hr>
        <p>Simulasi bahan komposit dan rintangan terma bersiri.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="module-card">
        <div class="icon-box">💨</div>
        <h3>Modul 3</h3>
        <p><b>Perolakan</b></p>
        <hr>
        <p>Pengiraan pekali pemindahan haba permukaan (h).</p>
    </div>
    """, unsafe_allow_html=True)

# 6. Footer
st.markdown("""
    <br><br><br>
    <div style="text-align: center; color: #888;">
        <hr>
        <p>Sistem Simulasi Terma Digital UTHM | 2026</p>
    </div>
    """, unsafe_allow_html=True)