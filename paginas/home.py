from textwrap import dedent
from utils.componentes import (
    carregar_estilos,
    exibir_hero,
    exibir_card,
    exibir_descricao,
    exibir_rodape
)

import streamlit as st


LOGO_URL = (
    'https://raw.githubusercontent.com/'
    'andersonserrico/Datathon_TerraJourney_Grupo48/'
    'main/extrainfo/TerraJourney_logo_branco.svg'
)


carregar_estilos()


exibir_hero(
    logo=LOGO_URL,
    subtitulo='Plataforma de Inteligência Educacional',
    largura=320
)


st.divider()


coluna_missao, coluna_visao = st.columns(2)


with coluna_missao:
    with st.container(border=True):
        st.subheader('🎯 Missão')

        st.write(
            '''
            Impulsionar a Jornada do Conhecimento por meio da análise 
            de dados educacionais, transformando informações em 
            conhecimento estratégico para identificar oportunidades de
            desenvolvimento e fortalecer iniciativas que ampliem o 
            impacto da educação na vida dos estudantes.
            '''
        )


with coluna_visao:
    with st.container(border=True):
        st.subheader('🔭 Visão')

        st.write(
            '''
            Conduzir a jornada do dado ao conhecimento, promovendo 
            análises eficientes e inovadoras que apoiem decisões 
            mais assertivas e ampliem as oportunidades de 
            desenvolvimento dos estudantes.
                     
            '''
        )


st.divider()


exibir_descricao(
    titulo='Bem-vindo ao TerraJourney',
    paragrafos=[
        (
            'Esta plataforma apresenta análises dos indicadores '
            'educacionais da Associação Passos Mágicos e modelos '
            'desenvolvidos para apoiar a compreensão do desempenho '
            'e da trajetória dos alunos.'
        ),
        (
            'Utilize o menu lateral para navegar pelas análises '
            'exploratórias, pelo dashboard e pelos modelos '
            'preditivos do projeto.'
        )
    ]
)


st.divider()


coluna_analises, coluna_dashboard, coluna_modelo = st.columns(3)


with coluna_analises:
    exibir_card(
        icone='📊',
        titulo='Análises',
        texto=(
            'Explore os indicadores acadêmicos, psicossociais e '
            'psicopedagógicos dos estudantes ao longo dos anos.'
        )
    )


with coluna_dashboard:
    exibir_card(
        icone='📈',
        titulo='Dashboards',
        texto=(
            'Visualizações interativas para facilitar a interpretação '
            'dos dados e apoiar a tomada de decisões.'
        )
    )


with coluna_modelo:
    exibir_card(
        icone='🤖',
        titulo='Modelo Preditivo',
        texto=(
            'Aplicação de técnicas de Machine Learning para identificar '
            'padrões e apoiar análises preditivas.'
        )
    )


st.divider()


exibir_rodape(
    projeto='Grupo Terra',
    equipe=[
        'Terra Wine • Terra Invest • Terra Healthy • Terra Fit  • Terra Journey'
    ],
    versao='1.0'
)