import streamlit as st
import pandas as pd

#define configs da pagina
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
)
#insercao dos dados do cliente 
nome1 = st.sidebar.text_input("Nome do cliente")

#uploader do stream
uploaded_file = st.sidebar.file_uploader("Escolha seu arquivo",
                                 type=['xlsx'],
                                 )
#valida o arquivo 
if uploaded_file is not None:
    # To read file as bytes:
    try:
        st.title(nome1)
        dados = pd.read_excel(uploaded_file)
        db = pd.read_excel("DB.xlsx")
        df_merged = pd.merge(dados, db, on= 'Atributo')
        df_agrupado = df_merged.to_excel('Dados2.xlsx', index=False)
        df = pd.read_excel('Dados2.xlsx')
        df1 = df.drop(index=22)
        df1
    except Exception as e:
        st.error(f"Erro ao ler o arquivo excel: {e}")