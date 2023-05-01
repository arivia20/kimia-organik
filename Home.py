import streamlit as st
import PIL as Image


st.header('kimia organik')
st.subheader('anak kimia bngt')
st.caption ("Yok belajar")

gambar1 = Image.open("image/logo sds + bg.png")
st.image(gambar1)
