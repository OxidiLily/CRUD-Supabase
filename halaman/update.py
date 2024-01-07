import streamlit as st
from supabase import create_client, Client
import os

def update():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

   
    nim =st.text_input('Nim Lama')
    nimbaru =st.text_input('Nim Baru')
    if st.button('Update Nim'):
        data = supabase.table("mahasiswa").update({"nim":nimbaru}).eq("nim",nim).execute().data
        st.write("Data Setelah di Update")
        st.dataframe(data)

    nama = st.text_input('Nama Lama')
    namabaru =st.text_input('Nama Baru')
    if st.button('Update Nama'):
        data = supabase.table("mahasiswa").update({"nama":namabaru}).eq("nama",nama).execute().data
        st.write("Data Setelah di Update")
        st.dataframe(data)
        

    datalis = supabase.table('mahasiswa').select('*').execute().data
    
    col1,col2,col3= st.columns(3);
    with col1:
        st.write("")
    with col2:
        st.write("Data dari Supabase")
        st.dataframe(datalis)
    with col3:
        st.write("")