from streamlit_option_menu import option_menu
import streamlit as st

from halaman.create import create
from halaman.read import read
from halaman.update import update
from halaman.delete import delete


def menu():
    page_names_to_funcs = {
    "Create": create,
    "Read": read,
    "Update": update,
    "Delete": delete
    }

    demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()