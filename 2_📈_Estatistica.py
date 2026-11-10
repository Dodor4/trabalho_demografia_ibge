import streamlit as st
import pandas as pd
import os
from utils.metrics import calcular_estatisticas

st.title("📈 Análise Estatística Detalhada")

@st.cache_data
def carregar_dados():
    caminho = os.path.join("data", "populacao_ibge.csv")
    if os.path.exists(caminho):
        return pd.read_csv(caminho)
    return pd.DataFrame()

df = carregar_dados()

regiao_sel = st.sidebar.selectbox("Filtrar por Região para Análise", ["Todas"] + list(df['Regiao'].unique()))
if regiao_sel != "Todas":
    df_filtrado = df[df['Regiao'] == regiao_sel]
else:
    df_filtrado = df

stats = calcular_estatisticas(df_filtrado, 'Populacao')

st.subheader("Medidas Estatísticas (População)")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média", f"{stats['media']:,.0f}")
col2.metric("Mediana", f"{stats['mediana']:,.0f}")
col3.metric("Desvio Padrão", f"{stats['desvio_padrao']:,.0f}")
col4.metric("IQR (Interquartil)", f"{stats['iqr']:,.0f}")

st.divider()

col_out1, col_out2 = st.columns(2)
with col_out1:
    st.markdown("### 🔍 Identificação de Outliers")
    st.write(f"**Total de Outliers:** {stats['outliers_count']}")
    st.write(f"**Limite Superior (Regra 1.5xIQR):** {stats['limite_superior']:,.0f}")

with col_out2:
    st.markdown("### 📊 Quartis (Q1, Q2, Q3)")
    st.write(f"**Q1 (25%):** {stats['q1']:,.0f}")
    st.write(f"**Q2 (Mediana):** {stats['mediana']:,.0f}")
    st.write(f"**Q3 (75%):** {stats['q3']:,.0f}")

st.info("""
**Análise da Consultoria:** A grande diferença entre a Média e a Mediana evidencia a assimetria dos dados provocada pelas grandes metrópoles (outliers). 
Para a alocação per capita de recursos públicos básicos, a **Mediana** é o parâmetro mais representativo.
""")
