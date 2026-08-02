import streamlit as st
import pandas as pd

from utils.componentes import carregar_estilos

carregar_estilos()

def calcular_iaa(idade):

    perguntas_iaa = {
        'Q1': 'Como você se sente consigo mesmo?',
        'Q2': 'Como você se sente na hora de estudar?',
        'Q3': 'Como você se sente quando está com sua família?',
        'Q4': 'Como você se sente quando está com amigos?',
        'Q5': 'Como você se sente quando está no Passos Mágicos?',
        'Q6': 'Como você se sente sobre seus Professores na Passos Mágicos?'
    }

    respostas_iaa = []

    if idade <= 11:

        opcoes_iaa_inicial = {
            '😄 Animado': 1.667,
            '🙂 Bem': 1.167,
            '😔 Triste': 0.583
        }

        for codigo, pergunta in perguntas_iaa.items():

            resposta = st.radio(
                pergunta,
                options=list(opcoes_iaa_inicial.keys()),
                index=None,
                horizontal=True,
                key=f'iaa_{codigo}'
            )

            if resposta is not None:
                respostas_iaa.append(
                    opcoes_iaa_inicial[resposta]
                )

    else:

        opcoes_iaa_avancado = {
            '😊': 1.667,
            '🙂': 1.250,
            '😐': 0.833,
            '😟': 0.417
        }

        st.caption(
            '😊 Muito positivo  |  '
            '🙂 Positivo  |  '
            '😐 Pouco positivo  |  '
            '😟 Negativo'
        )

        for codigo, pergunta in perguntas_iaa.items():

            resposta = st.radio(
                pergunta,
                options=list(opcoes_iaa_avancado.keys()),
                index=None,
                horizontal=True,
                key=f'iaa_{codigo}'
            )

            if resposta is not None:
                respostas_iaa.append(
                    opcoes_iaa_avancado[resposta]
                )

    if len(respostas_iaa) == 6:
        iaa = round(
            sum(respostas_iaa),
            3
        )

    else:
        iaa = None

    return iaa


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
    st.title('Modelo de Riscos de Desenvolvimento Infantil')

'''
### Questionario de Identificaçao

   Identificar se a criança já é cadastrada ou não no Programa
'''

#Verifica se a criança já é um aluno cadastrado
aluno_cadastrado = st.radio(
    'A criança já tem um RA cadastrado?',
    options=['Sim', 'Não'],
    index=None,
    horizontal=True
)
questionario_identificacao = False

if aluno_cadastrado == 'Sim':

    ra = st.number_input(
        'Informe o RA da criança:',
        min_value=0,
        step=1,
        value=None,
        placeholder='RA99999'
    )

elif aluno_cadastrado == 'Não':

    col_idade, col_genero, col_instituicao = st.columns(3)

    with col_idade:
        idade = st.slider(
            'Idade:',
            min_value=7,
            max_value=30,
            value=7,
            step=1
        )

    with col_genero:
        genero = st.selectbox(
            'Gênero:',
            options=[
                'Masculino',
                'Feminino'
            ],
            index=None,
            placeholder='Selecione'
        )

    with col_instituicao:
        instituicao = st.selectbox(
            'Instituição:',
            options=[
                'Pública',
                'Bolsista',
                'Privado',
                'Outros'
            ],
            index=None,
            placeholder='Selecione'
        )

    questionario_identificacao = True
else:
    st.warning('Selecione uma opção para continuar.')

st.divider()

if questionario_identificacao:
    '''
    ### Questionarios de Avaliação
    '''

    '''
     IDA - Indicador de desempenho Acadêmico
    '''
    #Calculo IDA com base nas notas de Português, Matemática e Inglês
    col_portugues, col_matematica, col_ingles = st.columns(3)

    with col_portugues:
        portugues = st.number_input(
            'Português:',
            min_value=0.0,
            max_value=10.0,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
    )

    with col_matematica:
        matematica = st.number_input(
            'Matemática:',
            min_value=0.0,
            max_value=10.0,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
        )

    with col_ingles:
        ingles = st.number_input(
            'Inglês:',
            min_value=0.0,
            max_value=10.0,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
    )

    if ingles is None:
        calculo_ida = (portugues + matematica) / 2
    else:
        calculo_ida = (portugues + matematica + ingles) / 3

    '''
     IEG - Indicador de Engajamento
    '''

    col_solicitadas, col_entregues = st.columns(2)

    with col_solicitadas:
        atividades_solicitadas = st.slider(
            'Atividades solicitadas:',
            min_value=10,
            max_value=25,
            value=10,
            step=1
            )

    with col_entregues:
        atividades_entregues = st.slider(
            'Atividades entregues:',
            min_value=5,
            max_value=25,
            value=5,
            step=1
            )

    if atividades_solicitadas < atividades_entregues:
        st.warning(
            'A quantidade de atividades solicitadas deve ser maior ou igual '
            'à quantidade de atividades entregues.'
            )
    else:
        calculo_ieg = (
            atividades_entregues
            / atividades_solicitadas
            * 10
            )

    
    '''
     IAA - Indicador de Autoavaliação
    '''
    calculo_iaa = calcular_iaa(idade)