import pickle
import os
import streamlit as st

# Fungsi validasi input
def validasi_input(Nama, Email, pesan):
    if not Nama or not Email or not pesan:
        raise ValueError("Semua kolom harus diisi.")

# Kelas Guest
class Guest:
    def __init__(self, Nama, Email, pesan):
        self.Nama = Nama
        self.Email = Email
        self.pesan = pesan

    def display_info(self):
        return f"Nama: {self.Nama}, Email: {self.Email}, Pesan: {self.pesan}"

# Fungsi menyimpan tamu
def save_guests_to_file(guests_list, filename='guests.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(guests_list, file)

# Fungsi memuat tamu dari file
def load_guests_from_file(filename='guests.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return []

# Memuat daftar tamu dari file
guests_list = load_guests_from_file()

# Fungsi untuk menambah tamu
def add_guest(Nama, Email, pesan):
    new_guest = Guest(Nama, Email, pesan)
    guests_list.append(new_guest)
    save_guests_to_file(guests_list)

# Fungsi untuk menampilkan tamu
def display_guests():
    if guests_list:
        for guest in guests_list:
            st.write(guest.display_info())
    else:
        st.write("Belum ada tamu.")

# Fungsi untuk menangani input
def handle_input(Nama, Email, pesan):
    try:
        validasi_input(Nama, Email, pesan)
        add_guest(Nama, Email, pesan)
        st.success("Tamu berhasil ditambahkan")
    except ValueError as e:
        st.error(f"Error: {e}")


