import streamlit as st
import pandas as pd
import os

st.title("📊 Visão Geral da Distribuição Geográfica")

@st.cache_data
def carregar_dados():
    caminho = os.path.join("data", "populacao_ibge.csv")
    if os.path.exists(caminho):
        return pd.read_csv(caminho)
    else:
        return pd.DataFrame({
            'Municipio': ['São Paulo', 'Rio de Janeiro', 'Brasília'],
            'Regiao': ['Sudeste', 'Sudeste', 'Centro-Oeste'],
            'UF': ['SP', 'RJ', 'DF'],
            'Populacao': [12396372, 6775561, 3055149],
            'IDHM': [0.805, 0.799, 0.824]
        })

df = carregar_dados()

# Upload opcional de arquivo customizado
uploaded_file = st.sidebar.file_uploader("Upload de arquivo CSV (opcional)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# Filtros laterais
regioes = ["Todas"] + list(df['Regiao'].unique())
regiao_sel = st.sidebar.selectbox("Filtrar por Região", regioes)

if regiao_sel != "Todas":
    df_filtrado = df[df['Regiao'] == regiao_sel]
else:
    df_filtrado = df

# KPIs principais
col1, col2, col3 = st.columns(3)
col1.metric("Total de Municípios", len(df_filtrado))
col2.metric("População Total", f"{df_filtrado['Populacao'].sum():,}")
col3.metric("Média IDHM", f"{df_filtrado['IDHM'].mean():.3f}")

st.divider()

st.subheader("Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

st.subheader("Distribuição por Região")
st.bar_chart(df_filtrado.groupby("Regiao")["Populacao"].sum())
