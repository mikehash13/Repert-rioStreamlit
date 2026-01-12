import streamlit as st
import pandas as pd

# python -m streamlit run meu_app.py
# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Portfólio | Mike Castor",
    page_icon="📊",
    layout="wide"
)

# =========================
# FUNÇÃO PARA CARREGAR DADOS
# =========================
@st.cache_data
def carregar_dados():
    return pd.read_csv("cursos.csv", sep=";")

# =========================
# HEADER
# =========================
with st.container():
    st.title("Mike Vinicius Viana Gonçalves Castor")
    st.subheader(
        "Analista de Dados | Business Intelligence | SQL | Python | Automação | Power Platform"
    )
    st.write(
        """
        Analista de Desenvolvimento de Sistemas em formação pela **Universidade Presbiteriana Mackenzie**,
        atualmente **Analista de PCM Pleno na STAHL** com forte atuação em **dados, automação e inovação de processos**.
        """
    )
    st.markdown(
        "🔗 [LinkedIn](https://www.linkedin.com/in/mike-castor-55267b172)  |  📧 mike.gb11@outlook.com"
    )

# =========================
# SOBRE MIM
# =========================
with st.container():
    st.write("---")
    st.header("👨‍💻 Sobre mim")
    st.write(
        """
        Atuo com foco em **dados, automação e inovação de processos**, desenvolvendo soluções para
        redução de atividades operacionais e aumento da eficiência.

        Possuo alta capacidade analítica, experiência em programação, vivência acadêmica e profissional,
        além de facilidade para conduzir trabalhos em equipe e atingir metas agressivas.

        Estou empenhado em seguir carreira na **tecnologia do mercado financeiro**, aplicando dados
        e inteligência analítica para apoiar a tomada de decisão.
        """
    )

# =========================
# HABILIDADES TÉCNICAS
# =========================
with st.container():
    st.write("---")
    st.header("🛠️ Habilidades Técnicas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Dados & Programação**
        - Python
        - SQL
        - Pandas
        - APIs
        """)

    with col2:
        st.markdown("""
        **BI & Analytics**
        - Power BI
        - DAX
        - Modelagem de Dados
        - KPIs e Indicadores
        """)

    with col3:
        st.markdown("""
        **Automação & Plataformas**
        - Power Apps
        - Power Automate
        - Power Platform
        - Excel Avançado
        """)

# =========================
# PROJETOS
# =========================
with st.container():
    st.write("---")
    st.header("📂 Projetos em Destaque")

    st.subheader("🚀 Automação de Orçamentos com Power Platform + IA")
    st.write(
        """
        **Objetivo:** Reduzir retrabalho, padronizar informações e acelerar o fluxo de solicitações.

        - Assistente técnico com **ChatGPT**
        - Aplicativo em **Power Apps**
        - Automação com **Power Automate**
        - Integração via **API (SGMAN)**
        - Dashboard em **Power BI**

        **Resultado:** Processo mais rápido, confiável e rastreável.
        """
    )

    st.subheader("📊 Cronograma Multicliente de Manutenção Preventiva")
    st.write(
        """
        - Cronograma em 12 ciclos
        - Status em tempo real por TAG
        - Alertas de atraso
        - KPIs de preventivas em dia

        **Impacto:** Aumento da previsibilidade e redução de riscos.
        """
    )

    st.subheader("🛠️ Dashboard de Performance de Manutenção (PCM)")
    st.write(
        """
        - Breakdown (h)
        - MTBF
        - MTTR
        - Confiabilidade em 100 dias
        - Total de TAGs monitorados
        """
    )

    st.subheader("🚗 Monitoramento de Frota e Custos Operacionais")
    st.write(
        """
        - Consumo e gasto por motorista
        - Rotas com mapa interativo
        - Ranking de ocorrências
        - Tendências mensais de custo
        """
    )

# =========================
# EXPERIÊNCIA PROFISSIONAL
# =========================
with st.container():
    st.write("---")
    st.header("💼 Experiência Profissional")

    st.subheader("STAHL Equipamentos — Analista de PCM Pleno")
    st.write(
        """
        **Mai/2022 – Atual**

        - Modelagem de dados em SQL  
        - Dashboards em Power BI (DAX)  
        - Automação e Power Apps  
        - Integrações via API  
        """
    )

    st.subheader("Fábrica de Ideias — Assistente de Manutenção")
    st.write(
        """
        **Jul/2021 – Mar/2022**

        - Manutenção preventiva e corretiva  
        - Análise de falhas  
        - Dados operacionais
        """
    )

# =========================
# FORMAÇÃO
# =========================
with st.container():
    st.write("---")
    st.header("🎓 Formação Acadêmica")

    st.write(
        """
        **Análise e Desenvolvimento de Sistemas**  
        Universidade Presbiteriana Mackenzie  
        *Jan/2026 – Jun/2028*

        **Técnico em Eletroeletrônica**  
        SENAI  
        *Jul/2019 – Jun/2021*
        """
    )

# =========================
# CURSOS E IDIOMAS
# =========================
with st.container():
    st.write("---")
    st.header("📚 Cursos & Idiomas")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - Power BI
        - Python
        - SQL
        - Power Platform
        - Cloud Fundamentals
        - Big Data & Analytics (FIAP)
        """)

    with col2:
        st.markdown("""
        - Inglês: Leitura técnica  
        - Espanhol: Leitura técnica
        """)

# =========================
# GRÁFICOS COM FILTRO DE PERÍODO
# =========================
with st.container():
    st.write("---")
    st.header("📈 Evolução de Estudos")

    try:
        dados = carregar_dados()

        # -------------------------
        # TRATAMENTO DE DATA
        # -------------------------
        mapa_meses = {
            "jan": "01", "fev": "02", "mar": "03", "abr": "04",
            "mai": "05", "jun": "06", "jul": "07", "ago": "08",
            "set": "09", "out": "10", "nov": "11", "dez": "12"
        }

        dados["data"] = dados["data"].str.lower()
        dados["mes"] = dados["data"].str[:3].map(mapa_meses)
        dados["ano"] = "20" + dados["data"].str[-2:]
        dados["data_formatada"] = pd.to_datetime(
            dados["ano"] + "-" + dados["mes"] + "-01"
        )

        # -------------------------
        # SELETOR DE PERÍODO
        # -------------------------
        qtd_dias = st.selectbox(
            "Selecione o período de análise",
            ["7D", "30D", "90D", "365", "1825", "3650"],
            index=1
        )

        num_dias = int(qtd_dias.replace("D", ""))

        data_max = dados["data_formatada"].max()
        data_min = data_max - pd.Timedelta(days=num_dias)

        dados_filtrados = dados[
            dados["data_formatada"].between(data_min, data_max)
        ]

        # -------------------------
        # GRÁFICO POR INSTITUIÇÃO
        # -------------------------
        duracao_por_instituicao = (
            dados_filtrados
            .groupby("instituicao")["duracao"]
            .sum()
            .reset_index()
        )

        st.subheader("Carga horária por instituição")
        st.area_chart(
            duracao_por_instituicao,
            x="instituicao",
            y="duracao"
        )

        # -------------------------
        # GRÁFICO MENSAL
        # -------------------------
        dados_agrupados = (
            dados_filtrados
            .groupby("data_formatada")["duracao"]
            .sum()
            .reset_index()
        )

        st.subheader("Carga horária de estudos por mês")
        st.bar_chart(
            dados_agrupados,
            x="data_formatada",
            y="duracao"
        )

    except Exception as e:
        st.warning("Erro ao carregar os dados de cursos.")

# =========================
# RODAPÉ
# =========================
with st.container():
    st.write("---")
    st.write("© 2026 | Desenvolvido por Mike Castor | Portfólio em Python & Streamlit")
