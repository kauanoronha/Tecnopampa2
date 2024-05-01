import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
)
uploaded_file = st.file_uploader("Escolha seu arquivo",
                                 type=['xlsx'],
                                 )
if uploaded_file is not None:
    # To read file as bytes:
    try:
        dados = pd.read_excel(uploaded_file)
        db = pd.read_excel("DB.xlsx")
        df_merged = pd.merge(dados, db, on= 'Atributo')
        df_agrupado = df_merged.to_excel('Dados2.xlsx', index=False)
        df = pd.read_excel('Dados2.xlsx')
        df1 = df.drop(index=22)
        df1
    except Exception as e:
        st.error(f"Erro ao ler o arquivo excel: {e}")