import streamlit as st
from supabase import create_client, Client
import pandas as pd
import os


def read():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    datalis = supabase.table('mahasiswa').select('*').execute().data

    

    df = pd.DataFrame(columns=["NO ID","Nama","Nim"])
    for i in range(0,len(datalis)):
        currentItem=datalis[i]
        df.loc[i] = [datalis[i]["id"],datalis[i]["nama"],datalis[i]["nim"]]


    cari = st.text_input('Cari Data')
    if st.button('Cari nama'):
        data = supabase.table("mahasiswa").select('*').eq('nama',cari).execute().data
        st.write("Data nama yang dicari")
        st.dataframe(data)
    if st.button('Cari Nim'):
        data = supabase.table("mahasiswa").select('*').eq('nim',cari).execute().data
        st.write("Data nim yang dicari")
        st.dataframe(data)
        
    col1,col2,col3= st.columns(3);
    with col1:
        st.write("")
    with col2:
        st.write("Data dari Supabase")
        st.dataframe(datalis)
    with col3:
        st.write("")
    