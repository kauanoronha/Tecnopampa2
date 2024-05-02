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
    # se o arquivo der certo 
    try:
        #Nome do cliente 
        st.title(nome1)
        #leitura das tabelas do db 
        dados = pd.read_excel(uploaded_file)
        db = pd.read_excel("DB.xlsx")
        #junta os arquivos, de referencias + database
        df_merged = pd.merge(dados, db, on= 'Atributo')
        # Cria o novo arquivo 
        df_agrupado = df_merged.to_excel('Dados2.xlsx', index=False)
        # Le o novo arquivo
        df = pd.read_excel('Dados2.xlsx')
        #df1 = df.drop(index=22)
        df2 = df.to_csv('data.csv', index=False)
        #ler o arquivo csv 
        df3 = pd.read_csv('data.csv')
        #Limpa a linha da classe textural 
        df4 = df3[df3['Atributo'] != 'Classe Textural']
        #setando atributo como index
        df4.set_index("Atributo", inplace=True)
        #transformando em float as colunas
        df4['Zona 1'] = df4['Zona 1'].astype(float)
        df4['Zona 2'] = df4['Zona 2'].astype(float)
        df4['Zona 3'] = df4['Zona 3'].astype(float)
        df4['Max_ideal'] = df4['Max_ideal'].astype(float)
        df4['Min_ideal'] = df4['Min_ideal'].astype(float)
        #calculando a media 
        df4['media'] = (df4['Min_ideal'] + df4['Max_ideal']) / 2
        
        #funcoes para definir o calulo das zonas 
        def calcula_nivel_z1_indic(df4):

            if df4['Zona 1'] < df4['Min_ideal']:
               return '🔴'
            elif df4['Zona 1']  >= (df4['media'] * 0.85) and df4['Zona 1'] <= (df4['media'] * 1.15):
               return  '🟢'
            elif df4['Zona 1']  > (df4['Min_ideal'] ) or df4['Zona 1'] < (df4['Max_ideal'] ):
               return  '🟡'
            else:
                return  '🔴'   
            
        def calcula_nivel_z2_indic(df4):

            if df4['Zona 2'] < df4['Min_ideal']:
               return '🔴'
            elif df4['Zona 2']  >= (df4['media'] * 0.85) and df4['Zona 2'] <= (df4['media'] * 1.15):
               return  '🟢'
            elif df4['Zona 2']  > (df4['Min_ideal'] ) or df4['Zona 2'] < (df4['Max_ideal'] ):
               return  '🟡'
            else:
                return  '🔴'   
            
        def calcula_nivel_z3_indic(df4):

            if df4['Zona 3'] < df4['Min_ideal']:
               return '🔴'
            elif df4['Zona 3']  >= (df4['media'] * 0.85) and df4['Zona 3'] <= (df4['media'] * 1.15):
               return  '🟢'
            elif df4['Zona 3']  > (df4['Min_ideal'] ) or df4['Zona 3'] < (df4['Max_ideal'] ):
               return  '🟡'
            else:
                return  '🔴'   

        def calcula_nivel_z1(df4):

            if df4['Zona 1'] < df4['Min_ideal']:
                return 'Abaixo'
            elif df4['Zona 1']  >= (df4['media'] * 0.85) and df4['Zona 1'] <= (df4['media'] * 1.15):
               return  'Ideal'
            elif df4['Zona 1'] > df4['Min_ideal'] or df4['Zona 2'] < df4['Max_ideal']:
                return  'Média'
            else:
                return  'Acima'    


        def calcula_nivel_z2(df4):

            if df4['Zona 2'] < df4['Min_ideal']:
                return 'Abaixo'
            elif df4['Zona 2']  >= (df4['media'] * 0.85) and df4['Zona 2'] <= (df4['media'] * 1.15):
               return  'Ideal'
            elif df4['Zona 2'] > df4['Min_ideal'] or df4['Zona 2'] < df4['Max_ideal']:
                return  'Média'
            else:
                return  'Acima'       
        
        def calcula_nivel_z3(df4):
            if df4['Zona 3'] < df4['Min_ideal']:
                return 'Abaixo'
            elif df4['Zona 3']  >= (df4['media'] * 0.85) and df4['Zona 3'] <= (df4['media'] * 1.15):
               return  'Ideal'
            elif df4['Zona 3'] > df4['Min_ideal'] or df4['Zona 3'] < df4['Max_ideal']:
                return  'Média'
            else:
                return  'Acima'      
      
        #criando a coluna para insercao das analises
        df4['Analise_Z1'] = df4.apply(calcula_nivel_z1, axis=1)
        df4['Analise_Z2'] = df4.apply(calcula_nivel_z2, axis=1)
        df4['Analise_Z3'] = df4.apply(calcula_nivel_z3, axis=1)
        df4['Analise_Z1_indic'] = df4.apply(calcula_nivel_z1_indic, axis=1)
        df4['Analise_Z2_indic'] = df4.apply(calcula_nivel_z2_indic, axis=1)
        df4['Analise_Z3_indic'] = df4.apply(calcula_nivel_z3_indic, axis=1)

        def normaliza_z1(df4):
            if (df4['Max_ideal'] - df4['Min_ideal']) <= 0:
                return 0 
            else:      
                if df4['Analise_Z1'] == "Abaixo" or df4['Analise_Z1'] == "Acima" :
                    return 0
                elif df4['Analise_Z1'] == "Média" or df4['Analise_Z1'] == "Ideal":
                    return ((df4['Zona 1'] - df4['Min_ideal']) / (df4['Max_ideal'] - df4['Min_ideal'])) * 100
        
        def normaliza_z2(df4):
            if (df4['Max_ideal'] - df4['Min_ideal']) <= 0:
                return 0 
            else:      
                if df4['Analise_Z2'] == "Abaixo" or df4['Analise_Z2'] == "Acima" :
                    return 0
                elif df4['Analise_Z2'] == "Média" or df4['Analise_Z2'] == "Ideal":
                    return ((df4['Zona 2'] - df4['Min_ideal']) / (df4['Max_ideal'] - df4['Min_ideal'])) * 100
        
        def normaliza_z3(df4):
            if (df4['Max_ideal'] - df4['Min_ideal']) <= 0:
                return 0 
            else:      
                if df4['Analise_Z3'] == "Abaixo" or df4['Analise_Z3'] == "Acima" :
                    return 0
                elif df4['Analise_Z3'] == "Média" or df4['Analise_Z3'] == "Ideal":
                    return ((df4['Zona 3'] - df4['Min_ideal']) / (df4['Max_ideal'] - df4['Min_ideal'])) * 100
   
        df4['normalizado_Z1'] = df4.apply(normaliza_z1, axis=1)
        df4['normalizado_Z2'] = df4.apply(normaliza_z2, axis=1)
        df4['normalizado_Z3'] = df4.apply(normaliza_z3, axis=1)
        

        columns_z1 = [ 'Zona 1', 'Analise_Z1', 'Analise_Z1_indic', 'normalizado_Z1'
                   ]
        columns_z2 = [ 'Zona 2', 'Analise_Z2', 'Analise_Z2_indic', 'normalizado_Z2'
                       ]
        columns_z3 = [ 'Zona 3', 'Analise_Z3', 'Analise_Z3_indic', 'normalizado_Z3'
                       ]
        col1, col2, col3 = st.columns(3)

        df_filterz1 = df4[columns_z1]
        st.dataframe(df_filterz1, column_config={
            "normalizado_Z1":st.column_config.ProgressColumn(
                "Percentual Zona 1",format='%d',  min_value=0, max_value=100
            )
        }) 

        df_filterz2 = df4[columns_z2]
        st.dataframe(df_filterz2, column_config={
            "normalizado_Z2":st.column_config.ProgressColumn(
                "Percentual Zona 2",format='%d',  min_value=0, max_value=100
            )
        }) 
        df_filterz3 = df4[columns_z3]
        st.dataframe(df_filterz3.head(29), column_config={
            "normalizado_Z3":st.column_config.ProgressColumn(
                "Percentual Zona 3",format='%d',  min_value=0, max_value=100, 
            )
        }) 



        col1 = df_filterz1
        col2 = df_filterz2
        col3 = df_filterz3
        st.write('importar a planilha dos nomes dos agrupamentos, e criar filtros delas no sidebar')





    except Exception as e:
        st.error(f"Erro ao ler o arquivo excel: {e}")