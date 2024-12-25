import streamlit as st

st.title("Halaman Dashboard")

# Fungsi Untuk Menghitung dan Menyimpan Total Nabung
def total():
    total_nabung = sum(t['Jumlah'] for t in st.session_state ['jumlah'] if t['Tipe'] == 'Menabung')

    return f"Total Nabung Anda {total_nabung}"

st.write(total())