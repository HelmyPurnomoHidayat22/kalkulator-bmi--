import streamlit as st
import matplotlib.pyplot as plt

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    tinggi_m = tinggi / 100  # Konversi tinggi ke meter
    bmi = berat / (tinggi_m ** 2)
    return bmi

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kekurangan berat badan"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25.0 <= bmi < 29.9:
        return "Berat badan berlebih"
    else:
        return "Obesitas"

# Fungsi untuk menghitung berat ideal
def berat_ideal(tinggi):
    tinggi_m = tinggi / 100
    bmi_min = 18.5
    bmi_max = 24.9
    berat_min = bmi_min * (tinggi_m ** 2)
    berat_max = bmi_max * (tinggi_m ** 2)
    return berat_min, berat_max

# Aplikasi Streamlit
st.title("Kalkulator BMI dengan Grafik")
st.write("Masukkan berat badan dan tinggi badan Anda untuk menghitung BMI, mengetahui kategori, dan mendapatkan rekomendasi berat ideal.")

# Input dari pengguna
berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1, max_value=200, value=70)
tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=50, max_value=250, value=170)

# Hitung BMI
if st.button("Hitung BMI"):
    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)
    berat_min, berat_max = berat_ideal(tinggi)

    # Tampilkan hasil
    st.subheader("Hasil BMI")
    st.write(f"BMI Anda: **{bmi:.2f}**")
    st.write(f"Kategori: **{kategori}**")
    st.write(f"Berat badan ideal: **{berat_min:.2f} kg - {berat_max:.2f} kg**")

    # Visualisasi menggunakan Matplotlib
    fig, ax = plt.subplots()
    labels = ["Berat Anda", "Berat Ideal Min", "Berat Ideal Max"]
    values = [berat, berat_min, berat_max]
    colors = ["blue", "green", "orange"]

    ax.bar(labels, values, color=colors)
    ax.set_title("Perbandingan Berat Badan")
    ax.set_ylabel("Kilogram (kg)")
    st.pyplot(fig)

    # Rekomendasi BMI
    st.write("Rekomendasi: Pertahankan BMI di rentang 18.5 - 24.9 untuk kesehatan optimal.")

