import streamlit as st
import plotly.express as px
import pandas as pd
from utils.componentes import carregar_estilos
from utils.tema import PALETA_PLOTLY

carregar_estilos()


# Inserção do Logo ao lado do Título
col_logo, col_titulo = st.columns([1, 6])
with col_logo:
    st.image('https://raw.githubusercontent.com/andersonserrico/Datathon_TerraJourney_Grupo48/main/extrainfo/TerraJourney_logo_branco.svg', width=120)
with col_titulo:
    st.title('Dashboard Geral de Dados')

st.write(
    '''
    Visão consolidada dos principais indicadores educacionais,
    permitindo acompanhar o perfil dos estudantes e a evolução
    dos resultados ao longo dos anos.
    '''
)

st.divider()

#Leitura da Base de Dados
github =  'https://raw.githubusercontent.com/andersonserrico/Datathon_TerraJourney_Grupo48/main/dados/PEDE_Dados_Unificados.csv'

dados = pd.read_csv(
    github,
    sep=',',
    encoding='utf-8-sig'
)

df_grafico = (
    dados['Instituicao_Ensino']
    .value_counts(dropna=False)
    .reset_index()
)

# Renomeando as colunas
df_grafico.columns = ['Instituicao_Ensino', 'Quantidade']

# Gráfico
fig = px.bar(
    df_grafico,
    x='Instituicao_Ensino',
    y='Quantidade',
    title='Quantidade de alunos por Instituição de Ensino',
    text='Quantidade'
)

# Header do Gráfico
st.header('Graficos Iterativos pelo Plotly')
st.plotly_chart(fig)