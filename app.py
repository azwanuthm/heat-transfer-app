import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Heat Transfer Lab - UTHM", layout="wide")

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("🖼️ Navigasi Modul")
modul = st.sidebar.radio(
    "Pilih Modul Pembelajaran:",
    ["Laman Utama", "Modul 1: Hukum Fourier", "Modul 2: Dinding Berlapis"]
)

st.sidebar.markdown("---")
st.sidebar.info("Dibangunkan untuk pengajaran subjek Heat Transfer.")

# --- PAGE 1: LAMAN UTAMA ---
if modul == "Laman Utama":
    st.title("🎓 Portal Pembelajaran Interaktif Heat Transfer")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Heat_transfer_mechanisms.png/640px-Heat_transfer_mechanisms.png", caption="Mekanisme Pemindahan Haba: Konduksi, Perolakan, & Sinaran")
    
    st.markdown("""
    Selamat datang ke aplikasi pengajaran digital. Sila pilih modul di bar sisi (sidebar) untuk memulakan sesi pengiraan dan simulasi:
    
    * **Modul 1: Hukum Fourier** - Fokus kepada pengiraan konduksi satu lapisan.
    * **Modul 2: Dinding Berlapis** - Mengira rintangan terma bagi bahan komposit.
    * **Modul 3: Perolakan** (Akan Datang).
    """)

# --- PAGE 2: MODUL 1 (FOURIER) ---
elif modul == "Modul 1: Hukum Fourier":
    st.title("🔥 Modul 1: Konduksi (Hukum Fourier)")
    st.latex(r"q = kA \frac{\Delta T}{L}")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Parameter")
        k = st.number_input("Kekonduksian Terma, k (W/m·K)", value=15.0)
        A = st.number_input("Luas Permukaan, A (m²)", value=1.0)
        dT = st.number_input("Perbezaan Suhu, ΔT (K)", value=50.0)
        L = st.number_input("Ketebalan Dinding, L (m)", value=0.02)
        
    with col2:
        st.subheader("Hasil Pengiraan")
        if L > 0:
            q = (k * A * dT) / L
            st.metric(label="Kadar Pemindahan Haba (q)", value=f"{q:.2f} Watt")
            st.write(f"Bagi bahan dengan k={k} W/m·K, haba mengalir sebanyak {q:.2f} Joules setiap saat.")
        else:
            st.error("Ketebalan (L) mestilah lebih besar daripada 0.")

# --- PAGE 3: MODUL 2 (DINDING BERLAPIS) ---
elif modul == "Modul 2: Dinding Berlapis":
    st.title("🧱 Modul 2: Dinding Berlapis (Composite Walls)")
    st.write("Analogi Rintangan Terma: $q = \Delta T / \sum R_{th}$")
    
    # Input Suhu
    c1, c2 = st.columns(2)
    t1 = c1.number_input("Suhu Dalam, T1 (°C)", value=250.0)
    t3 = c2.number_input("Suhu Luar, T3 (°C)", value=35.0)
    
    st.markdown("---")
    
    # Input Lapisan
    lap1, lap2 = st.columns(2)
    
    with lap1:
        st.subheader("Lapisan A (Dinding)")
        k_a = st.number_input("k_a (W/m·K)", value=0.8, key="ka")
        L_a = st.number_input("Ketebalan L_a (m)", value=0.2, key="la")
        R_a = L_a / (k_a * 1.0)
        st.caption(f"Rintangan A: {R_a:.4f} K/W")

    with lap2:
        st.subheader("Lapisan B (Penebat)")
        k_b = st.number_input("k_b (W/m·K)", value=0.04, key="kb")
        L_b = st.number_input("Ketebalan L_b (m)", value=0.05, key="lb")
        R_b = L_b / (k_b * 1.0)
        st.caption(f"Rintangan B: {R_b:.4f} K/W")

    # Keputusan
    R_total = R_a + R_b
    q_comp = (t1 - t3) / R_total
    t2 = t1 - (q_comp * R_a)
    
    st.markdown("---")
    res1, res2 = st.columns(2)
    res1.success(f"### Kadar Haba: {q_comp:.2f} W/m²")
    res2.info(f"### Suhu Antara (T2): {t2:.2f} °C")
