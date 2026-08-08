import streamlit as st


st.set_page_config(
    page_title='TerraJourney',
    page_icon='🌎',
    layout='wide',
    initial_sidebar_state='expanded'
)


pagina_home = st.Page(
    'paginas/home.py',
    title='Home',
    icon='🏠',
    default=True
)

pagina_analises = st.Page(
    'paginas/analises.py',
    title='Análises',
    icon='📊'
)

pagina_modelo = st.Page(
    'paginas/modelo.py',
    title='Modelo',
    icon='🤖'
)


navegacao = st.navigation(
    {
        'TerraJourney': [
            pagina_home
        ],
        'Projeto': [
            pagina_analises,
            pagina_modelo
        ]
    }
)

with st.sidebar:
    st.divider()

    st.markdown(
        '''
        <div style="text-align: center; color: gray; font-size: 14px; line-height: 1.6; transform: translateX(-8px);">
            <strong>FIAP Datathon 2026</strong><br><br>
            TerraJourney - Grupo 48</strong><br>
            Anderson: RM368309<br>
            Maike: RM367843<br>
            Rafaell: RM368753
        </div>
        ''',
        unsafe_allow_html=True
    )

navegacao.run()