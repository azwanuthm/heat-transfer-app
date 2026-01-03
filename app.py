import streamlit as st

st.title("🔥 Aplikasi Pembelajaran Heat Transfer")
st.subheader("Modul 1: Konduksi Haba (Hukum Fourier)")

st.write("Hukum Fourier menyatakan bahawa kadar pemindahan haba melalui bahan adalah berkadar terus dengan luas permukaan dan kecerunan suhu.")

st.latex(r"q = -kA \frac{dT}{dx}")

st.sidebar.header("Masukkan Pembolehubah:")
k = st.sidebar.number_input("Kekonduksian Terma, k (W/m.K)", value=15.0)
A = st.sidebar.number_input("Luas Permukaan, A (m²)", value=1.0)
dT = st.sidebar.number_input("Perbezaan Suhu, ΔT (K)", value=100.0)
dx = st.sidebar.number_input("Ketebalan Dinding, Δx (m)", value=0.05)

if dx > 0:
    q = (k * A * dT) / dx
    st.success(f"### Kadar Pemindahan Haba, q = {q:.2f} Watt")
else:
    st.error("Ketebalan (dx) tidak boleh sifar!")
