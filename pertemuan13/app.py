import streamlit as st

# Side Bar Direktory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
Nabung = st.Page("./fitur/nabung.py", title="Nabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
        "Dashboard": [dashboard],
        "Nabung": [Nabung],
        "Penarikan": [penarikan]
    }
)

#Menjalankan Navigasi
pg.run()

if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []
