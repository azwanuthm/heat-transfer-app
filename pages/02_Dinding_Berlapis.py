import streamlit as st
import plotly.graph_objects as go

# Tajuk Modul
st.title("🧱 Modul 2: Dinding Berlapis (Composite Walls)")
st.write(r"Analogi Rintangan Terma: $q = \frac{T_1 - T_3}{R_{total}}$")

# --- BAHAGIAN 1: INPUT ---
st.header("1. Input Parameter")
c1, c2 = st.columns(2)
with c1:
    t1 = st.number_input("Suhu Permukaan Dalam, T1 (°C)", value=250.0)
with c2:
    t3 = st.number_input("Suhu Permukaan Luar, T3 (°C)", value=35.0)

st.markdown("---")

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Lapisan A (Dinding)")
    k_a = st.number_input("Kekonduksian k_a (W/m·K)", value=0.8, key="ka")
    L_a = st.number_input("Ketebalan L_a (m)", value=0.2, key="la")
    R_a = L_a / (k_a * 1.0) # Luas A = 1 m^2
    st.caption(f"Rintangan R_a: {R_a:.4f} K/W")

with col_b:
    st.subheader("Lapisan B (Penebat)")
    k_b = st.number_input("Kekonduksian k_b (W/m·K)", value=0.04, key="kb")
    L_b = st.number_input("Ketebalan L_b (m)", value=0.05, key="lb")
    R_b = L_b / (k_b * 1.0)
    st.caption(f"Rintangan R_b: {R_b:.4f} K/W")

# --- BAHAGIAN 2: PENGIRAAN ---
R_total = R_a + R_b
q_comp = (t1 - t3) / R_total
t2 = t1 - (q_comp * R_a)

# --- BAHAGIAN 3: VISUALISASI GRAF ---
st.header("2. Profil Penurunan Suhu")
x_coords = [0, L_a, L_a + L_b]
y_temps = [t1, t2, t3]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_coords, 
    y=y_temps, 
    mode='lines+markers',
    line=dict(color='firebrick', width=4),
    marker=dict(size=10),
    name='Suhu (°C)'
))

fig.update_layout(
    xaxis_title="Kedudukan (m)",
    yaxis_title="Suhu (°C)",
    margin=dict(l=20, r=20, t=40, b=20),
    height=400
)
st.plotly_chart(fig, use_container_width=True)

# --- BAHAGIAN 4: KEPUTUSAN ---
st.header("3. Keputusan Analisis")
res1, res2 = st.columns(2)
res1.metric("Kadar Aliran Haba (q)", f"{q_comp:.2f} W/m²")
res2.metric("Suhu Pertemuan (T2)", f"{t2:.2f} °C")

st.info("💡 **Nota:** Perhatikan kecerunan graf. Lapisan dengan 'k' lebih rendah mempunyai kecerunan yang lebih curam (penurunan suhu lebih besar).")