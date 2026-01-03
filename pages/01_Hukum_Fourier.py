import streamlit as st

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
    else:
        st.error("L mestilah > 0")