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
# HEADER COM FOTO
# =========================
with st.container():
    col_foto, col_info = st.columns([1, 4])

    with col_foto:
        st.image(
            "fotomike.jpg",
            width=160
        )

    with col_info:
        st.title("Mike Vinicius Viana Gonçalves Castor")
        st.markdown(
            "**Analista de Dados | Business Intelligence | SQL | Python | Power Platform**"
        )
        st.write(
            """
            Profissional em formação em **Análise e Desenvolvimento de Sistemas pela Universidade Presbiteriana Mackenzie**,
            com atuação prática em **dados, automação de processos e inteligência analítica**.
            
            Atualmente **Analista de PCM Pleno na STAHL**, com forte foco em **eficiência operacional, dashboards executivos
            e integração de sistemas**.
            """
        )
        st.markdown(
            "🔗 [LinkedIn](https://www.linkedin.com/in/mike-castor-55267b172)  |  📧 mike12345191@gmail.com | 📞 (11) 9 6872-5870"
        )

# =========================
# SOBRE MIM
# =========================
with st.container():
    st.write("---")
    st.header("Sobre o profissional")
    st.write(
        """
        Atuo com foco em **análise de dados, automação e melhoria contínua**, desenvolvendo soluções que reduzem esforço
        operacional, aumentam a confiabilidade das informações e suportam a tomada de decisão estratégica.

        Possuo perfil analítico, pensamento estruturado e experiência prática em ambientes operacionais e corporativos,
        com facilidade para transitar entre áreas técnicas e de negócio.

        Meu objetivo profissional é consolidar carreira na **área de tecnologia e dados**, com direcionamento ao
        **mercado financeiro e grandes organizações**.
        """
    )

# =========================
# HABILIDADES TÉCNICAS
# =========================
with st.container():
    st.write("---")
    st.header("Competências Técnicas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Dados & Programação**
        - Python
        - SQL
        - Pandas
        - Consumo de APIs
        """)

    with col2:
        st.markdown("""
        **Business Intelligence**
        - Power BI
        - DAX
        - Modelagem de Dados
        - KPIs Executivos
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
    st.header("Projetos Relevantes")

    st.subheader("Automação de Orçamentos com Power Platform e IA")
    st.write(
        """
        **Objetivo:** Otimizar o fluxo de solicitações comerciais, reduzindo retrabalho e erros manuais.

        - Assistente técnico com IA generativa (ChatGPT)
        - Aplicação em Power Apps
        - Fluxos automatizados com Power Automate
        - Integração via API com sistema SGMAN
        - Dashboard gerencial em Power BI

        **Resultado:** Processo padronizado, rastreável e significativamente mais ágil.
        """
    )

    st.subheader("Cronograma Multicliente de Manutenção Preventiva")
    st.write(
        """
        - Planejamento em ciclos anuais
        - Acompanhamento por TAG
        - Indicadores de atraso e aderência
        - Visão executiva de preventivas em dia
        """
    )

    st.subheader("Dashboard de Performance de Manutenção (PCM)")
    st.write(
        """
        - MTBF e MTTR
        - Horas de breakdown
        - Indicadores de confiabilidade
        - Monitoramento de ativos
        """
    )

    st.subheader("Monitoramento de Frota e Custos Operacionais")
    st.write(
        """
        - Custos por motorista
        - Análise de consumo
        - Tendências mensais
        - Ranking de ocorrências
        """
    )

# =========================
# EXPERIÊNCIA PROFISSIONAL
# =========================
with st.container():
    st.write("---")
    st.header("Experiência Profissional")

    st.subheader("STAHL Equipamentos — Analista de PCM Pleno")
    st.write(
        """
        **Mai/2022 – Atual**

        - Análise e modelagem de dados em SQL  
        - Desenvolvimento de dashboards em Power BI  
        - Automação de processos operacionais  
        - Integração de sistemas via API  
        """
    )

    st.subheader("Fábrica de Ideias — Assistente de Manutenção")
    st.write(
        """
        **Jul/2021 – Mar/2022**

        - Manutenção preventiva e corretiva  
        - Análise de falhas  
        - Tratamento de dados operacionais  
        """
    )

# =========================
# FORMAÇÃO
# =========================
with st.container():
    st.write("---")
    st.header("Formação Acadêmica")

    st.write(
        """
        **Análise e Desenvolvimento de Sistemas**  
        Universidade Presbiteriana Mackenzie  
        *2026 – 2028*

        **Técnico em Eletroeletrônica**  
        SENAI  
        *2019 – 2021*
        """
    )

# =========================
# CURSOS E IDIOMAS
# =========================

with st.container(): 
	st.write("---") 
	st.header("Cursos e Idiomas") 

	col1, col2 = st.columns(2) 

	with col1: 
		st.markdown("""
		- Power BI | Fundação Bradesco 
		- Python | SENAI 
		- Python | Universidade Presbiteriana Mackenzie 
		- SQL para Data Science - Power Platform (PL-900) 
		- Cloud Fundamentals | FIAP 
		- Big Data & Analytics | FIAP 
		""") 

with col2: 
	st.markdown("""
	- Inglês: leitura técnica 
	- Espanhol: leitura técnica 
	""")


# =========================
# EVOLUÇÃO DE ESTUDOS
# =========================
with st.container():
    st.write("---")
    st.header("Evolução de Estudos")

    try:
        dados = carregar_dados()

        mapa_meses = {
            "jan": 1, "fev": 2, "mar": 3, "abr": 4,
            "mai": 5, "jun": 6, "jul": 7, "ago": 8,
            "set": 9, "out": 10, "nov": 11, "dez": 12
        }

        # -------------------------
        # Converter datas
        # -------------------------
        def converter_mes_ano(valor):
            mes = mapa_meses[valor[:3].lower()]
            ano = int("20" + valor[-2:])
            return pd.Timestamp(year=ano, month=mes, day=1)

        dados["data_inicio"] = dados["dataone"].apply(converter_mes_ano)
        dados["data_fim"] = dados["datatwo"].apply(converter_mes_ano)

        # -------------------------
        # Expandir cursos por mês
        # -------------------------
        linhas = []

        for _, row in dados.iterrows():
            meses = pd.date_range(
                start=row["data_inicio"],
                end=row["data_fim"],
                freq="MS"
            )

            duracao_mensal = row["duracao"] / len(meses)

            for mes in meses:
                linhas.append({
                    "data": mes,
                    "instituicao": row["instituicao"],
                    "duracao": duracao_mensal
                })

        dados_mensais = pd.DataFrame(linhas)

        # -------------------------
        # Filtro de período
        # -------------------------
        qtd_dias = st.selectbox(
            "Período de análise",
            ["365", "1825", "3650"],
            index=2
        )

        num_dias = int(qtd_dias)
        data_max = dados_mensais["data"].max()
        data_min = data_max - pd.Timedelta(days=num_dias)

        dados_filtrados = dados_mensais[
            dados_mensais["data"].between(data_min, data_max)
        ].copy()
        dados_filtrados["ano"] = dados_filtrados["data"].dt.year

        # -------------------------
        # GRÁFICOS
        # -------------------------
        st.subheader("Carga horária anual de estudos")

        st.bar_chart(
            dados_filtrados
            .groupby("ano")["duracao"]
            .sum()
            .sort_index()
        )

        st.subheader("Carga horária por instituição")
        st.area_chart(
            dados_filtrados
            .groupby("instituicao")["duracao"]
            .sum()
        )

    except Exception as e:
        st.warning("Erro ao processar os dados de evolução de estudos.")


# =========================
# RODAPÉ
# =========================
with st.container():
    st.write("---")
    st.write("© 2026 | Mike Castor | Portfólio Profissional em Python & Streamlit")

