import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
)

dados = pd.read_excel('Dados.xlsx')
db = pd.read_excel("DB.xlsx")
df_merged = pd.merge(dados, db, on= 'Atributo')
df_agrupado = df_merged.to_excel('Dados2.xlsx', index=False)
df = pd.read_excel('Dados2.xlsx')
df1 = df.drop(index=22)
num = (df1['Zona 1'] - df1['Max_ideal'])
den = (df1['Zona 1'] - df1['Min_ideal'])

'''for i in df1:
    if num <= 0:
         df1["prog_z1"] = 0 
    else:
        df1["prog_z1"] = (( num / den ) * 100)  
df1''' 
col1, col2 = st.columns(2)
col1 = num
col2 = den
df1
#df['Progresso'] = ((df['Zona 1'] - df['Min_ideal']) / (df['Zona 1'] - df['Max_ideal'])) * 100

#columns = [ 'Progresso', 'Atributo', 'Zona 1']
'''final = st.dataframe(df_merged, column_order=columns, column_config={
    "Progresso": st.column_config.ProgressColumn(
        "Zona 1 "
        )
})'''
