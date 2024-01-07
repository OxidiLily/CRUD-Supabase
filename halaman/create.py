import streamlit as st
from supabase import create_client, Client
import os

def create():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    nama = st.text_input('Nama')
    nim =st.text_input('Nim')
    if st.button('Save'):
        data = supabase.table("mahasiswa").insert({"nama":nama,"nim":nim}).execute()

    
    datalis = supabase.table('mahasiswa').select('*').execute().data
    
    col1,col2,col3= st.columns(3);
    with col1:
        st.write("")
    with col2:
        st.write("Data dari Supabase")
        st.dataframe(datalis)
    with col3:
        st.write("")