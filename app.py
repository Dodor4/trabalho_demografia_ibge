import streamlit as st

st.set_page_config(
    page_title="Dashboard IBGE | Consultoria Pública",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização visual (Estilo Startup / Consultoria)
st.markdown("""
    <style>
        .main-header { font-size: 2.2rem; font-weight: 700; color: #1e3d59; }
        .sub-header { font-size: 1.1rem; color: #576574; margin-bottom: 2rem; }
        .card-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1.5rem;
            border-left: 5px solid #1f77b4;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">Painel Unificado - Distribuição Geográfica IBGE</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Consultoria de Inteligência de Dados aplicada a Decisões Públicas e Políticas Regionais.</p>', unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card-box">
        <h3>1. Tratamento e ETL</h3>
        <p>Coleta, higienização e estruturação de dados do IBGE via Pandas e NumPy.</p>
        <ul>
            <li>Upload de dados (CSV/XLSX)</li>
            <li>Filtros dinâmicos por UF e região</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-box">
        <h3>2. Análise Estatística</h3>
        <p>Cálculo de tendência central e dispersão para extrair insights reais.</p>
        <ul>
            <li>Média, Mediana, IQR, Desvio Padrão</li>
            <li>Detecção rigorosa de Outliers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-box">
        <h3>3. Atuação de Startup</h3>
        <p>Apresentação de achados para pessoas e gestores públicos.</p>
        <ul>
            <li>Roda de conversa executiva</li>
            <li>Respostas a perguntas de negócio</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.title("Navegação")
st.sidebar.info("Utilize o menu acima para alternar entre a Visão Geral, Análise Estatística e Relatório de Consultoria.")
