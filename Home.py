import streamlit as st


st.header('kimia organik')
st.subheader('anak kimia bngt')
st.caption ("Yok belajar")

Soal = st.selectbox(
    'Pilih soal',
    ('Soal 1', 'Soal 2', 'Soal 3'))
if Soal == "Soal 1":
    st.write("2 + 2 adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1 = st.button("5")
        opsi2 = st.button("10")
    with col2:
        opsi3 = st.button("4")
        opsi1 = st.button("6")
    if opsi1:
        st.write("Salah")
    elif opsi2:
        st.write("Salah")
    elif opsi3:
        st.write("Benar")
        st.balloons()
    elif opsi1:
        st.write("Salah")
   
if Soal == "Soal 2":
    st.write("2 + 3 adalah...")
