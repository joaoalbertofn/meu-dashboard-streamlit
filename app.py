import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Dashboard de Teste - Streamlit Cloud",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("📊 Dashboard de Teste - Streamlit Community Cloud")
st.markdown("Esta é uma aplicação simples para testar o deploy no **Streamlit Community Cloud**.")

# Sidebar filters
st.sidebar.header("Filtros")
num_points = st.sidebar.slider("Número de pontos de dados", min_value=10, max_value=200, value=100, step=10)
chart_color = st.sidebar.color_picker("Escolha a cor do gráfico", "#FF4B4B")

# Generate mock data
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=num_points, freq="D")
values = np.random.randn(num_points).cumsum()
df = pd.DataFrame({"Data": dates, "Vendas": values})

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de Vendas (Acumulado)", value=f"{values[-1]:.2f}", delta=f"{values[-1] - values[-2]:.2f}")
with col2:
    st.metric(label="Melhor Dia", value=f"{values.max():.2f}")
with col3:
    st.metric(label="Pior Dia", value=f"{values.min():.2f}")

st.markdown("---")

# Layout columns for chart and table
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Tendência de Vendas ao Longo do Tempo")
    st.line_chart(df.set_index("Data"), color=chart_color)

with col_right:
    st.subheader("Dados Brutos")
    st.dataframe(df, use_container_width=True, height=300)

st.success("Tudo pronto! Siga os passos no chat para realizar o deploy desta aplicação.")
