import streamlit as st
import pandas as pd
import joblib
import numpy as np

from scipy.stats import gaussian_kde

from pathlib import Path

from utils.componentes import carregar_estilos
from utils.graficos import criar_grafico
from utils.tema import (
    COR_PRIMARIA,
    COR_SECUNDARIA,
    COR_TERCIARIA
)

carregar_estilos()


# ---------------------------------------------------------
# Carregamento do artefato do modelo
# ---------------------------------------------------------

@st.cache_resource
def carregar_artefato_modelo():
    caminho_modelo = (
        Path(__file__).resolve().parents[1]
        / 'modelo'
        / 'modelo_risco.pkl'
    )

    return joblib.load(caminho_modelo)

artefato_modelo = carregar_artefato_modelo()

carregar_estilos()

# Inserção do Logo ao lado do Título
col_logo, col_titulo = st.columns([1, 6])

with col_logo:
    st.image(
        'https://raw.githubusercontent.com/andersonserrico/'
        'Datathon_TerraJourney_Grupo48/main/extrainfo/'
        'TerraJourney_logo_branco.svg',
        width=120
    )

with col_titulo:
    st.title('Análises dos Indicadores Educacionais')


st.write(
    '''
    Visão consolidada dos principais indicadores educacionais,
    permitindo acompanhar o perfil dos estudantes e a evolução
    dos resultados ao longo dos anos.
    '''
)


# Leitura da Base de Dados
github = (
    'https://raw.githubusercontent.com/andersonserrico/'
    'Datathon_TerraJourney_Grupo48/main/dados/'
    'PEDE_Dados_Unificados.csv'
)

dados = pd.read_csv(
    github,
    sep=',',
    encoding='utf-8-sig'
)

#==============================================================
# Funções das análises
#--------------------------------------------------------------
#
# Cada função realiza o tratamento dos dados, cria os gráficos
# e apresenta os resultados de um indicador educacional.
#
#==============================================================


# -------------------------------------------------------------
# 1. Defasagem Escolar — IAN
# -------------------------------------------------------------
def analise_ian(dados):

    st.subheader('Defasagem Escolar — IAN')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            O perfil de defasagem evoluiu de forma muito positiva: os alunos no nível <strong>Adequado</strong>
            saltaram de <strong>30% em 2022</strong> para a maioria absoluta (<strong>54% em 2024</strong>).
            A <strong>Defasagem Severa</strong> foi reduzida a patamares mínimos, passando de
            <strong>28 para apenas 3 alunos</strong>.<br><br>
            O desafio atual da ONG é continuar tracionando os <strong>46% (531 alunos)</strong>
            que ainda permanecem na defasagem moderada.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção do indicador
    df_analise1 = dados[
        ['Ano_Referencia', 'IAN']
    ].copy()


    # Criação das Categorias de Defasagem
    df_analise1['Categoria'] = pd.cut(
        df_analise1['IAN'],
        bins=[
            0,
            2.5,
            5,
            10
        ],
        labels=[
            'Defasagem Severa',
            'Defasagem Moderada',
            'Adequado (Em Fase)'
        ],
        include_lowest=True,
        right=True
    )


    # Quantidade de alunos por Ano de Referência e Categoria
    df_analise1 = (
        df_analise1
        .groupby(
            ['Ano_Referencia', 'Categoria'],
            observed=True
        )
        .size()
        .reset_index(
            name='Quantidade'
        )
    )


    # Criação do Primeiro Gráfico
    fig1 = criar_grafico(
        tipo='bar',
        dados=df_analise1,
        x='Ano_Referencia',
        y='Quantidade',
        color='Categoria',
        titulo='Volume de Alunos por Perfil da Defasagem',
        texto='Quantidade',
        mostrar_legenda=False,
        color_map={
            'Adequado (Em Fase)': COR_PRIMARIA,
            'Defasagem Moderada': COR_SECUNDARIA,
            'Defasagem Severa': COR_TERCIARIA
        }
    )


    # Cálculo do percentual por Ano de Referência
    df_pct = df_analise1.copy()

    df_pct['Percentual'] = (
        df_pct['Quantidade']
        / df_pct.groupby(
            'Ano_Referencia'
        )['Quantidade'].transform('sum')
        * 100
    ).round(1)


    # Formatação do percentual para exibição
    df_pct['Percentual_Texto'] = (
        df_pct['Percentual']
        .map(
            lambda valor: f'{valor:.1f}%'
        )
    )


    # Criação do Segundo Gráfico
    fig2 = criar_grafico(
        tipo='bar_horizontal',
        dados=df_pct,
        x='Percentual',
        y='Ano_Referencia',
        color='Categoria',
        titulo='Evolução Proporcional da Defasagem',
        texto='Percentual_Texto',
        mostrar_legenda=True,
        modo_barra='stack',
        color_map={
            'Adequado (Em Fase)': COR_PRIMARIA,
            'Defasagem Moderada': COR_SECUNDARIA,
            'Defasagem Severa': COR_TERCIARIA
        }
    )


    # Percentuais dentro das barras
    fig2.update_traces(
        textposition='inside'
    )


    # Exibição dos Gráficos em colunas
    col_grafico1, col_grafico2 = st.columns(2)

    with col_grafico1:
        st.plotly_chart(
            fig1,
            width='stretch'
        )

    with col_grafico2:
        st.plotly_chart(
            fig2,
            width='stretch'
        )

# ---------------------------------------------------------
# 2. Desempenho Escolar — IDA
# ---------------------------------------------------------
def analise_ida(dados):

    st.subheader('Desempenho Escolar — IDA')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            O desempenho (<strong>IDA</strong>) apresenta uma melhora geral, apesar das flutuações.
            Ao longo das fases, o índice inicialmente cai (até a <strong>Fase 3</strong>), mas se recupera
            e melhora significativamente nas fases finais. Ao longo dos anos, também há melhora, com
            <strong>2023 e 2024</strong> registrando médias superiores a <strong>2022</strong> na maior
            parte do gráfico.
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Seleção das colunas necessárias
    df_analise = dados[
        [
            'Ano_Referencia',
            'Fase',
            'IDA'
        ]
    ].copy()


    # Padronização da Fase
    df_analise['Fase_Padronizada'] = (
        df_analise['Fase']
        .astype(str)
        .str.extract(r'(\d+)')[0]
    )

    df_analise['Fase_Padronizada'] = (
        'Fase ' + df_analise['Fase_Padronizada']
    )


    # Ordem correta das Fases
    ordem_fases = [
        'Fase 0',
        'Fase 1',
        'Fase 2',
        'Fase 3',
        'Fase 4',
        'Fase 5',
        'Fase 6',
        'Fase 7',
        'Fase 8'
    ]

    df_analise['Fase_Padronizada'] = pd.Categorical(
        df_analise['Fase_Padronizada'],
        categories=ordem_fases,
        ordered=True
    )


    # Média do IDA por Ano e Fase
    df_analise = (
        df_analise
        .groupby(
            [
                'Ano_Referencia',
                'Fase_Padronizada'
            ],
            observed=True
        )['IDA']
        .mean()
        .reset_index()
    )


    # Ordenação
    df_analise = df_analise.sort_values(
        [
            'Ano_Referencia',
            'Fase_Padronizada'
        ]
    )


    # Criação do Gráfico
    fig = criar_grafico(
        tipo='line',
        dados=df_analise,
        x='Fase_Padronizada',
        y='IDA',
        color='Ano_Referencia',
        titulo='Evolução do Desempenho Acadêmico por Fase e Ano',
        mostrar_legenda=True
    )


    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )

def analise_ieg(dados):

    # ---------------------------------------------------------
    # 3. Engajamento — IEG
    # ---------------------------------------------------------

    st.subheader('Engajamento — IEG')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            O <strong>Engajamento (IEG)</strong> possui uma relação direta e positiva tanto com o
            <strong>Desempenho (IDA)</strong> quanto com o <strong>Ponto de Virada (IPV)</strong>.
            As linhas de tendência ascendentes em ambos os gráficos de dispersão confirmam visualmente
            essa correlação, indicando que o aumento no engajamento do aluno está associado a resultados
            superiores nos dois indicadores.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção dos indicadores
    df_analise = dados[
        [
            'IEG',
            'IDA',
            'IPV'
        ]
    ].copy()


    # Remoção de valores nulos necessários para os gráficos
    df_analise = df_analise.dropna(
        subset=[
            'IEG',
            'IDA',
            'IPV'
        ]
    )

    # ---------------------------------------------------------
    # Gráfico 1 - IEG x IDA
    # ---------------------------------------------------------

    fig1 = criar_grafico(
        tipo='scatter',
        dados=df_analise,
        x='IEG',
        y='IDA',
        titulo='Impacto do Engajamento (IEG) no Desempenho (IDA)',
        trendline='ols'
    )

    fig1.data[-1].update(
        line_color=COR_SECUNDARIA
        )
    
    # ---------------------------------------------------------
    # Gráfico 2 - IEG x IPV
    # ---------------------------------------------------------
    fig2 = criar_grafico(
        tipo='scatter',
        dados=df_analise,
        x='IEG',
        y='IPV',
        titulo='Impacto do Engajamento (IEG) no Ponto de Virada (IPV)',
        trendline='ols'
        )
    
    fig2.data[-1].update(
        line_color=COR_SECUNDARIA
        )

    # ---------------------------------------------------------
    # Exibição dos Gráficos
    # ---------------------------------------------------------

    col_grafico1, col_grafico2 = st.columns(2)

    with col_grafico1:
        st.plotly_chart(
            fig1,
            width='stretch'
        )

    with col_grafico2:
        st.plotly_chart(
            fig2,
            width='stretch'
        )

def analise_iaa(dados):

    # ---------------------------------------------------------
    # 4. Autoavaliação — IAA
    # ---------------------------------------------------------

    st.subheader('Autoavaliação — IAA')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            A <strong>Autoavaliação (IAA)</strong> apresenta baixa coerência
            com o desempenho e o engajamento. Analisando o gráfico abaixo,
            notamos que as correlações são muito fracas: apenas
            <strong>0,12 com o IDA</strong> e <strong>0,13 com o IEG</strong>.
            Isso indica que a percepção dos alunos sobre si mesmos não reflete
            fortemente seus resultados reais e participação.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção dos indicadores
    df_analise = dados[
        [
            'IAA',
            'IDA',
            'IEG',
            'IPV'
        ]
    ].copy()


    # Remoção dos valores nulos
    df_analise = df_analise.dropna()


    # Criação da Matriz de Correlação
    df_corr = df_analise.corr()


    # Criação do Heatmap
    fig = criar_grafico(
        tipo='heatmap',
        dados=df_corr,
        titulo='Matriz de Correlação: Coerência da Autoavaliação (IAA)'
    )


    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )

def analise_ips(dados):

    # ---------------------------------------------------------
    # 5. Aspectos Psicossociais — IPS
    # ---------------------------------------------------------

    st.subheader('Aspectos Psicossociais — IPS')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            Os gráficos em <strong>boxplots</strong> confirmam a existência de padrões psicossociais
            associados ao <strong>IPS</strong>. Alunos que sofreram queda no desempenho
            (<strong>IDA</strong>) ou no engajamento (<strong>IEG</strong>) apresentam medianas
            menores no IPS do ano anterior. A distribuição também revela que grande parte desse grupo
            já possuía notas mais baixas de IPS. Portanto, resultados psicossociais inferiores antecedem
            e podem sinalizar quedas acadêmicas e de participação futuras.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção das colunas necessárias
    df_analise = dados[
        [
            'RA',
            'Ano_Referencia',
            'IPS',
            'IDA',
            'IEG'
        ]
    ].copy()


    # Remoção dos valores nulos
    df_analise = df_analise.dropna(
        subset=[
            'RA',
            'Ano_Referencia',
            'IPS',
            'IDA',
            'IEG'
        ]
    )


    # Ordenação do histórico de cada aluno
    df_analise = df_analise.sort_values(
        by=[
            'RA',
            'Ano_Referencia'
        ]
    )


    # IPS do ano anterior
    df_analise['IPS_Anterior'] = (
        df_analise
        .groupby('RA')['IPS']
        .shift(1)
    )


    # Variação do desempenho
    df_analise['Delta_IDA'] = (
        df_analise
        .groupby('RA')['IDA']
        .diff()
    )


    # Variação do engajamento
    df_analise['Delta_IEG'] = (
        df_analise
        .groupby('RA')['IEG']
        .diff()
    )


    # Mantém apenas alunos com histórico disponível
    df_analise = df_analise.dropna(
        subset=[
            'IPS_Anterior',
            'Delta_IDA',
            'Delta_IEG'
        ]
    ).copy()


    # ---------------------------------------------------------
    # Classificação da evolução do IDA
    # ---------------------------------------------------------

    df_analise['Status_IDA'] = (
        df_analise['Delta_IDA']
        .apply(
            lambda valor:
                'Queda no IDA'
                if valor < 0
                else 'Manteve ou Melhorou'
        )
    )


    # Quantidade por grupo
    contagem_ida = (
        df_analise['Status_IDA']
        .value_counts()
    )


    # Label com quantidade de alunos
    df_analise['Label_IDA'] = (
        df_analise['Status_IDA']
        .apply(
            lambda status:
                f'{status} (n={contagem_ida.get(status, 0)})'
        )
    )


    # ---------------------------------------------------------
    # Classificação da evolução do IEG
    # ---------------------------------------------------------

    df_analise['Status_IEG'] = (
        df_analise['Delta_IEG']
        .apply(
            lambda valor:
                'Queda no IEG'
                if valor < 0
                else 'Manteve ou Melhorou'
        )
    )


    # Quantidade por grupo
    contagem_ieg = (
        df_analise['Status_IEG']
        .value_counts()
    )


    # Label com quantidade de alunos
    df_analise['Label_IEG'] = (
        df_analise['Status_IEG']
        .apply(
            lambda status:
                f'{status} (n={contagem_ieg.get(status, 0)})'
        )
    )


    # ---------------------------------------------------------
    # Gráfico 1 - IPS anterior x evolução do IDA
    # ---------------------------------------------------------

    fig1 = criar_grafico(
        tipo='box',
        dados=df_analise,
        x='Label_IDA',
        y='IPS_Anterior',
        color='Status_IDA',
        titulo='O IPS Antecipa Quedas no Desempenho?',
        mostrar_legenda=False,
        color_map={
            'Manteve ou Melhorou': COR_PRIMARIA,
            'Queda no IDA': COR_TERCIARIA
        }
    )


    # ---------------------------------------------------------
    # Gráfico 2 - IPS anterior x evolução do IEG
    # ---------------------------------------------------------

    fig2 = criar_grafico(
        tipo='box',
        dados=df_analise,
        x='Label_IEG',
        y='IPS_Anterior',
        color='Status_IEG',
        titulo='O IPS Antecipa Quedas no Engajamento?',
        mostrar_legenda=False,
        color_map={
            'Manteve ou Melhorou': COR_PRIMARIA,
            'Queda no IEG': COR_TERCIARIA
        }
    )


    # ---------------------------------------------------------
    # Exibição dos Gráficos
    # ---------------------------------------------------------

    col_grafico1, col_grafico2 = st.columns(2)

    with col_grafico1:
        st.plotly_chart(
            fig1,
            width='stretch'
        )

    with col_grafico2:
        st.plotly_chart(
            fig2,
            width='stretch'
        )


def analise_ipp(dados):

    # ---------------------------------------------------------
    # 6. Aspectos Psicopedagógicos — IPP
    # ---------------------------------------------------------

    st.subheader('Aspectos Psicopedagógicos — IPP')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            As notas do <strong>IPP</strong> acompanham a classificação do
            <strong>IAN</strong>. Conforme a defasagem se agrava de
            <strong>Adequado</strong> para <strong>Severa</strong>, nota-se
            uma queda nas medianas e no limite inferior das caixas. Portanto,
            avaliações psicopedagógicas mais baixas refletem de forma coerente
            os maiores níveis de defasagem dos alunos.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção dos indicadores
    df_analise = dados[
        [
            'IAN',
            'IPP'
        ]
    ].copy()


    # Garantindo que IPP seja numérico
    df_analise['IPP'] = pd.to_numeric(
        df_analise['IPP'],
        errors='coerce'
    )


    # Criação das categorias do IAN
    df_analise['Categoria'] = pd.cut(
        df_analise['IAN'],
        bins=[
            0,
            2.5,
            5,
            10
        ],
        labels=[
            'Defasagem Severa',
            'Defasagem Moderada',
            'Adequado (Em Fase)'
        ],
        include_lowest=True,
        right=True
    )


    # Remoção dos valores nulos
    df_analise = df_analise.dropna(
        subset=[
            'Categoria',
            'IPP'
        ]
    )


    # Quantidade de alunos por Categoria
    contagem = (
        df_analise['Categoria']
        .value_counts()
    )


    # Label das categorias com quantidade de alunos
    df_analise['Categoria_Label'] = (
        df_analise['Categoria']
        .apply(
            lambda categoria:
                f'{categoria} (n={contagem.get(categoria, 0)})'
        )
    )


    # Ordem das categorias
    ordem_categorias = [
        'Adequado (Em Fase)',
        'Defasagem Moderada',
        'Defasagem Severa'
    ]


    # Ordem dos labels
    ordem_labels = [
        f'{categoria} (n={contagem.get(categoria, 0)})'
        for categoria in ordem_categorias
    ]


    # Transformação em categoria ordenada
    df_analise['Categoria_Label'] = pd.Categorical(
        df_analise['Categoria_Label'],
        categories=ordem_labels,
        ordered=True
    )


    # Ordenação do DataFrame
    df_analise = df_analise.sort_values(
        'Categoria_Label'
    )


    # Criação do Gráfico
    fig = criar_grafico(
        tipo='box',
        dados=df_analise,
        x='Categoria_Label',
        y='IPP',
        color='Categoria',
        titulo='Avaliação Psicopedagógica (IPP) vs Defasagem (IAN)',
        mostrar_legenda=True,
        color_map={
            'Adequado (Em Fase)': COR_PRIMARIA,
            'Defasagem Moderada': COR_SECUNDARIA,
            'Defasagem Severa': COR_TERCIARIA
        }
    )


    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )

# ---------------------------------------------------------
# 7. Ponto de Virada — IPV
# ---------------------------------------------------------
def analise_ipv(dados):

    st.subheader('Ponto de Virada — IPV')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            Os comportamentos que mais influenciam o <strong>IPV</strong> são o
            <strong>Engajamento (IEG)</strong> e o <strong>Desempenho Acadêmico (IDA)</strong>, 
            com um impacto forte e idêntico (ambos com <strong>0,56</strong>). Em seguida, vem o 
            <strong>Psicopedagógico (IPP)</strong> com um impacto bem relevante <strong>0,52</strong>). 
            Indicadores como <strong>IAN</strong>, <strong>Autoavaliação (IAA)</strong> e
            <strong>Psicossociais (IPS)</strong> têm influência mínima ou negativa
            no ponto de virada.
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Seleção dos indicadores
    colunas = [
        'IPV',
        'IDA',
        'IEG',
        'IPS',
        'IPP',
        'IAA',
        'IAN'
    ]

    df_analise = dados[
        colunas
    ].copy()

    # Garantindo valores numéricos
    df_analise = df_analise.apply(
        pd.to_numeric,
        errors='coerce'
    )

    # Correlação dos indicadores com o IPV
    df_analise = (
        df_analise
        .corr()[['IPV']]
        .drop(
            index='IPV'
        )
        .dropna()
        .reset_index()
        .rename(
            columns={
                'index': 'Indicador',
                'IPV': 'Correlacao'
            }
        )
        .sort_values(
            by='Correlacao',
            ascending=True
        )
    )

    # Texto das correlações
    df_analise['Correlacao_Texto'] = (
        df_analise['Correlacao']
        .map(
            lambda valor: f'{valor:.2f}'
        )
    )

    # Criação do Gráfico
    fig = criar_grafico(
        tipo='bar_horizontal',
        dados=df_analise,
        x='Correlacao',
        y='Indicador',
        texto='Correlacao_Texto',
        titulo='O que mais influencia o Ponto de Virada (IPV)?',
        paleta=[
            COR_PRIMARIA
        ]
    )

    # Texto dentro das barras
    fig.update_traces(
        textposition='inside'
    )

    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )
# ---------------------------------------------------------
# 8. Nota Global — INDE
# ---------------------------------------------------------

def analise_inde(dados):

    st.subheader('Nota Global — INDE')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            A melhor combinação para elevar o <strong>INDE</strong> é alavancar os indicadores de
            <strong>Desempenho (IDA)</strong> e <strong>Engajamento (IEG)</strong>. O IDA atua como
            o principal motor da nota global, possuindo a correlação individual mais forte
            (<strong>0,79</strong>). O IEG é o segundo maior influenciador
            (<strong>0,75</strong>), complementado pelo impacto moderado do aspecto psicopedagógico
            (<strong>IPV, com 0,71</strong>). O indicador psicossocial (<strong>IPS</strong>) fica
            fora da combinação ideal, pois apresenta influência muito baixa no resultado final
            (<strong>0,20</strong>).
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção dos indicadores
    colunas = [
        'INDE',
        'IAN',
        'IDA',
        'IEG',
        'IAA',
        'IPS',
        'IPP',
        'IPV'
    ]

    df_analise = dados[
        colunas
    ].copy()


    # Garantindo valores numéricos
    df_analise = df_analise.apply(
        pd.to_numeric,
        errors='coerce'
    )


    # Correlação dos indicadores com o INDE
    df_analise = (
        df_analise
        .corr()[['INDE']]
        .drop(
            index='INDE'
        )
        .dropna()
        .reset_index()
        .rename(
            columns={
                'index': 'Indicador',
                'INDE': 'Correlacao'
            }
        )
        .sort_values(
            by='Correlacao',
            ascending=True
        )
    )


    # Formatação dos valores para exibição
    df_analise['Correlacao_Texto'] = (
        df_analise['Correlacao']
        .map(
            lambda valor: f'{valor:.2f}'
        )
    )


    # Criação do Gráfico
    fig = criar_grafico(
        tipo='bar_horizontal',
        dados=df_analise,
        x='Correlacao',
        y='Indicador',
        texto='Correlacao_Texto',
        titulo='O que mais eleva a Nota Global — INDE',
        paleta=[
            COR_PRIMARIA
        ]
    )


    # Valores dentro das barras
    fig.update_traces(
        textposition='inside'
    )


    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )

# ---------------------------------------------------------
# 9. Efetividade do Programa — Evolução do INDE
# ---------------------------------------------------------
def analise_efetividade(dados):

    st.subheader('Efetividade do Programa — Evolução do INDE')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            Nota-se uma melhora consistente e ininterrupta da
            <strong>Nota Global (INDE)</strong> através de todas as fases.
            O índice avança progressivamente de <strong>5,37</strong> na fase
            inicial (<strong>Quartzo</strong>) até atingir <strong>8,44</strong>
            na fase final (<strong>Topázio</strong>). Essa nítida trajetória
            ascendente comprova o impacto positivo e a efetividade real do
            programa no desenvolvimento contínuo dos alunos.
        </div>
        ''',
        unsafe_allow_html=True
    )


    # Seleção das colunas necessárias
    df_analise = dados[
        [
            'Pedra',
            'INDE'
        ]
    ].copy()


    # Garantindo que INDE seja numérico
    df_analise['INDE'] = pd.to_numeric(
        df_analise['INDE'],
        errors='coerce'
    )


    # Remoção dos valores nulos
    df_analise = df_analise.dropna(
        subset=[
            'Pedra',
            'INDE'
        ]
    )


    # Ordem das Pedras
    ordem_pedras = [
        'Quartzo',
        'Agata',
        'Ametista',
        'Topazio'
    ]


    # Definição da ordem das Pedras
    df_analise['Pedra'] = pd.Categorical(
        df_analise['Pedra'],
        categories=ordem_pedras,
        ordered=True
    )


    # Média do INDE por Pedra
    df_analise = (
        df_analise
        .groupby(
            'Pedra',
            observed=True
        )['INDE']
        .mean()
        .reset_index(
            name='Media_INDE'
        )
        .sort_values(
            'Pedra'
        )
    )

    # Formatação da média para exibição
    df_analise['Media_Texto'] = (
        df_analise['Media_INDE']
        .map(
            lambda valor: f'{valor:.2f}'
        )
    )

    # Criação do Gráfico
    fig = criar_grafico(
        tipo='line',
        dados=df_analise,
        x='Pedra',
        y='Media_INDE',
        texto='Media_Texto',
        titulo='Progressão da Nota Global (INDE) pelas Fases',
        paleta=[
            COR_SECUNDARIA
        ]
    )


    # Exibição dos valores acima dos pontos
    fig.update_traces(
        textposition='top center'
    )


    # Exibição do Gráfico
    st.plotly_chart(
        fig,
        width='stretch'
    )

# ---------------------------------------------------------
# 10. Modelo Preditivo — Risco de Defasagem
# ---------------------------------------------------------
def analise_modelo(artefato_modelo):

    st.subheader('Modelo Preditivo — Risco de Defasagem')

    st.markdown(
        '''
        <div class="analise-destaque">
            <span class="analise-titulo">Análise:</span>
            O modelo preditivo de <strong>risco futuro de defasagem</strong>
            utiliza os indicadores atuais do aluno para estimar a probabilidade
            de apresentar defasagem no período seguinte.
            As variáveis de maior importância no modelo são
            <strong>IPP</strong>, <strong>Idade</strong> e
            <strong>IAN</strong>.
            O score probabilístico permite identificar e priorizar alunos
            com maior risco, utilizando como referência o limiar de
            <strong>50%</strong>.
        </div>
        ''',
        unsafe_allow_html=True
    )

    # ---------------------------------------------------------
    # Gráfico 1 — Importância das Variáveis
    # ---------------------------------------------------------

    df_importancias = (
        artefato_modelo[
            'importancia_features'
        ]
        .copy()
    )

    # Renomeando a variável para exibição
    df_importancias[
        'Indicador'
    ] = (
        df_importancias[
            'Variavel'
        ]
    )

    # Conversão para percentual
    df_importancias[
        'Importancia_Percentual'
    ] = (
        df_importancias[
            'Importancia'
        ]
        * 100
    )

    # Texto para exibição
    df_importancias[
        'Importancia_Texto'
    ] = (
        df_importancias[
            'Importancia_Percentual'
        ]
        .map(
            lambda valor:
                f'{valor:.1f}%'
        )
    )

    # Identificação das 3 variáveis
    # mais importantes
    top3 = (
        df_importancias
        .nlargest(
            3,
            'Importancia'
        )[
            'Indicador'
        ]
        .tolist()
    )

    # Criação da categoria de destaque
    df_importancias[
        'Destaque'
    ] = np.where(
        df_importancias[
            'Indicador'
        ].isin(top3),
        'Top 3',
        'Demais'
    )

    # Ordenação para o gráfico horizontal
    df_importancias = (
        df_importancias
        .sort_values(
            'Importancia_Percentual',
            ascending=True
        )
        .copy()
    )

    # Criação do gráfico
    fig1 = criar_grafico(
        tipo='bar_horizontal',
        dados=df_importancias,
        x='Importancia_Percentual',
        y='Indicador',
        color='Destaque',
        texto='Importancia_Texto',
        titulo='Importância das Variáveis no Risco Futuro',
        mostrar_legenda=False,
        color_map={
            'Top 3': COR_SECUNDARIA,
            'Demais': COR_PRIMARIA
        }
    )

    # Texto dentro das barras
    fig1.update_traces(
        textposition='inside'
    )

    # ---------------------------------------------------------
    # Gráfico 2 — Distribuição das Probabilidades
    # ---------------------------------------------------------

    probabilidades = np.array(
        artefato_modelo[
            'avaliacao'
        ][
            'probabilidades_teste'
        ]
    ) * 100

    limiar = (
        artefato_modelo[
            'avaliacao'
        ][
            'limiar_classificacao'
        ]
        * 100
    )

    df_probabilidades = pd.DataFrame(
        {
            'Probabilidade': probabilidades
        }
    )

    # Histograma
    fig2 = criar_grafico(
        tipo='hist',
        dados=df_probabilidades,
        x='Probabilidade',
        titulo=(
            'Probabilidade de Alunos entrarem '
            'em Defasagem — Score de Risco'
        ),
        paleta=[
            COR_PRIMARIA
        ]
    )

    # ---------------------------------------------------------
    # Curva KDE
    # ---------------------------------------------------------

    kde = gaussian_kde(
        probabilidades
    )

    eixo_x = np.linspace(
        probabilidades.min(),
        probabilidades.max(),
        200
    )

    densidade = kde(
        eixo_x
    )

    numero_bins = 10

    largura_bin = (
        probabilidades.max()
        - probabilidades.min()
    ) / numero_bins

    densidade_ajustada = (
        densidade
        * len(probabilidades)
        * largura_bin
    )

    fig2.add_scatter(
        x=eixo_x,
        y=densidade_ajustada,
        mode='lines',
        name='Distribuição',
        line=dict(
            color=COR_SECUNDARIA,
            width=3
        )
    )

    # ---------------------------------------------------------
    # Linha do ponto de corte
    # ---------------------------------------------------------

    fig2.add_vline(
        x=limiar,
        line_dash='dash',
        line_color=COR_TERCIARIA,
        annotation_text=(
            f'Risco Crítico ({limiar:.0f}%)'
        ),
        annotation_position='top right'
    )

    # ---------------------------------------------------------
    # Ajustes visuais
    # ---------------------------------------------------------

    fig2.update_layout(
        xaxis_title=(
            'Probabilidade Calculada pela I.A. (%)'
        ),
        yaxis_title='Quantidade de Alunos',
        showlegend=True
    )

    # ---------------------------------------------------------
    # Gráfico 3 — Distribuição das Idades e Taxa de Risco
    # ---------------------------------------------------------

    df_idade = (
        artefato_modelo[
            'analise_idade'
        ]
        .copy()
    )

    # Texto da taxa de risco
    df_idade[
        'Taxa_Risco_Texto'
    ] = (
        df_idade[
            'Taxa_Risco'
        ]
        .map(
            lambda valor:
                f'{valor:.1f}%'
        )
    )

    # Barras com quantidade de alunos
    fig3 = criar_grafico(
        tipo='bar',
        dados=df_idade,
        x='Idade',
        y='Quantidade',
        titulo=(
            'Distribuição dos Alunos por Idade '
            'e Taxa de Risco'
        ),
        texto='Quantidade',
        paleta=[
            COR_PRIMARIA
        ]
    )

    # Linha da taxa de risco
    fig3.add_scatter(
        x=df_idade[
            'Idade'
        ],
        y=df_idade[
            'Taxa_Risco'
        ],
        mode='lines+markers',
        name='Taxa de Risco',
        line=dict(
            color=COR_SECUNDARIA,
            width=3
        ),
        marker=dict(
            size=8
        ),
        yaxis='y2'
    )

    # Segundo eixo Y
    fig3.update_layout(
        yaxis=dict(
            title='Quantidade de Alunos'
        ),
        yaxis2=dict(
            title='Taxa de Risco (%)',
            overlaying='y',
            side='right',
            range=[
                0,
                100
            ]
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        )
    )

    # ---------------------------------------------------------
    # Exibição dos Gráficos
    # ---------------------------------------------------------

    col_grafico1, col_grafico2 = (
        st.columns(2)
    )

    with col_grafico1:

        st.plotly_chart(
            fig1,
            width='stretch'
        )

    with col_grafico2:

        st.plotly_chart(
            fig2,
            width='stretch'
        )

    st.plotly_chart(
        fig3,
        width='stretch'
    )

#==============================================================
# Apresentação das análises
#--------------------------------------------------------------
#
# Cada função realiza o tratamento dos dados, cria os gráficos
# e apresenta os resultados de um indicador educacional.
#
#==============================================================

st.divider()

analise_ian(dados)

st.divider()

analise_ida(dados)

st.divider()

analise_ieg(dados)

st.divider()

analise_iaa(dados)

st.divider()

analise_ips(dados)

st.divider()

analise_ipp(dados)

st.divider()

analise_ipv(dados)

st.divider()

analise_inde(dados)

st.divider()

analise_efetividade(dados)


st.divider()

analise_modelo(
    artefato_modelo
)

st.divider()