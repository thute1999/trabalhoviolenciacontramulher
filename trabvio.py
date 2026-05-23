import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Dashboard Violência Contra a Mulher - Teresina",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título Principal
st.title("📊 Monitoramento da Violência Contra a Mulher - Teresina")
st.markdown("Análise de indicadores de violência doméstica e feminicídios baseados em dados oficiais da SSP-PI.")

st.divider()

# --- SEÇÃO 1: MÉTRICAS EM DESTAQUE ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Média de Notificações/Dia (THE)", value="~88", delta="Casos diários")
with col2:
    st.metric(label="Feminicídios na Capital", value="24.3%", delta="Do total do PI")
with col3:
    st.metric(label="Vítimas Sem B.O. Prévio", value="78.4%", delta="Subnotificação", delta_color="inverse")
with col4:
    st.metric(label="Ocorrências na Residência", value="59.5%", delta="Espaço Doméstico")

st.divider()

# --- SEÇÃO 2: GRÁFICOS NATIVOS DO STREAMLIT ---
st.header("👤 Perfil das Vítimas e Fatores Relacionados")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Distribuição por Raça/Cor (%)")
    
    # Dados estruturados para o gráfico de barras do Streamlit
    dados_raca = pd.DataFrame({
        "Percentual": [78.4, 13.5, 8.1]
    }, index=["Pardas", "Brancas", "Pretas"])
    
    # O gráfico nativo adota automaticamente o visual moderno do Streamlit
    st.bar_chart(dados_raca)

with col_graf2:
    st.subheader("Vínculo do Autor com a Vítima (%)")
    
    dados_vinculo = pd.DataFrame({
        "Casos (%)": [24.3, 24.3, 16.2, 8.1, 27.1]
    }, index=["Ex-Companheiro", "Parentes/Familiares", "Companheiro Atual", "Cônjuge", "Outros"])
    
    st.bar_chart(dados_vinculo)

st.divider()

# --- SEÇÃO 3: RECURSOS DE AJUDA ---
st.header("📞 Canais de Denúncia e Apoio em Teresina")
st.markdown("""
Este painel também serve como ferramenta de utilidade pública. Canais de acolhimento locais:
*   **Casa da Mulher Brasileira (Teresina):** (86) 99412-2719
*   **Guarda Municipal de Teresina:** 153
*   **Delegacia da Mulher (Centro):** (86) 3222-2323
*   **Polícia Militar (Urgência):** 190
""")