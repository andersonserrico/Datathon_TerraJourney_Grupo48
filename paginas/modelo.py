import streamlit as st
import pandas as pd

from utils.componentes import carregar_estilos

from utils.questionarios import (
    PERGUNTAS_IAA,
    OPCOES_IAA_INICIAL,
    OPCOES_IAA_AVANCADO,
    PERGUNTAS_IPS,
    PERGUNTAS_IPP,
    RECOMENDACOES_IPP,
    PERGUNTAS_IPV
)


carregar_estilos()

# -----------------------------------------------------
# IDA
# -----------------------------------------------------
def calcular_ida():

    st.markdown(
        '#### IDA — Indicador de Desempenho Acadêmico'
    )

    col_portugues, col_matematica, col_ingles = st.columns(3)

    with col_portugues:

        portugues = st.number_input(
            'Português:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
        )


    with col_matematica:

        matematica = st.number_input(
            'Matemática:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
        )


    with col_ingles:

        ingles = st.number_input(
            'Inglês:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0'
        )

    st.divider()

    if (
        portugues is not None
        and matematica is not None
    ):

        if ingles is None:

            calculo_ida = (
                portugues
                + matematica
            ) / 2

        else:

            calculo_ida = (
                portugues
                + matematica
                + ingles
            ) / 3


        return round(
                calculo_ida,
                3
            )

    return None


# -----------------------------------------------------
# IEG
# -----------------------------------------------------
def calcular_ieg():

    st.markdown(
        '#### IEG — Indicador de Engajamento'
    )

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
            min_value=0,
            max_value=25,
            value=5,
            step=1
        )

    st.divider()

    if atividades_entregues > atividades_solicitadas:
        erros.append(
            'A quantidade de atividades entregues não pode '
            'ser maior que a quantidade de atividades solicitadas.'
        )
    else:

        return round(
            (
                atividades_entregues
                / atividades_solicitadas
                * 10
            ),
            3
        )


    return None

# ---------------------------------------------------------
# IAA — Indicador de Autoavaliação
# ---------------------------------------------------------
def calcular_iaa(idade):

    st.markdown(
        '#### IAA — Indicador de Autoavaliação'
    )
    respostas_iaa = []

    if idade <= 11:

        for codigo, pergunta in PERGUNTAS_IAA.items():

            resposta = st.radio(
                pergunta,
                options=list(
                    OPCOES_IAA_INICIAL.keys()
                ),
                index=None,
                horizontal=True,
                key=f'iaa_{codigo}'
            )

            if resposta is not None:
                respostas_iaa.append(
                    OPCOES_IAA_INICIAL[resposta]
                )

    else:

        for codigo, pergunta in PERGUNTAS_IAA.items():

            resposta = st.radio(
                pergunta,
                options=list(
                    OPCOES_IAA_AVANCADO[codigo].keys()
                ),
                index=None,
                key=f'iaa_{codigo}'
            )

            if resposta is not None:
                respostas_iaa.append(
                    OPCOES_IAA_AVANCADO[codigo][resposta]
                )

    st.divider()

    if len(respostas_iaa) == 6:
        return round(
            sum(respostas_iaa),
            3
        )

    return None

# ---------------------------------------------------------
# IPS — Indicador de Aspectos Psicossociais
# ---------------------------------------------------------
def calcular_ips():

    st.markdown(
        '#### IPS — Indicador de Aspectos Psicossociais'
    )

    respostas_ips = []

    for codigo, configuracao in PERGUNTAS_IPS.items():

        resposta = st.radio(
            configuracao['pergunta'],
            options=list(
                configuracao['opcoes'].keys()
            ),
            index=None,
            key=f'ips_{codigo}'
        )

        if resposta is not None:
            respostas_ips.append(
                configuracao['opcoes'][resposta]
            )
    st.divider()

    if len(respostas_ips) == 4:
        return round(
            sum(respostas_ips),
            3
        )

    return None

# ---------------------------------------------------------
# IPP — Indicador de Aspectos Psicopedagógicos
# ---------------------------------------------------------

def calcular_ipp():

    st.markdown(
        '#### IPP — Indicador de Aspectos Psicopedagógicos'
    )

    respostas_ipp = []

    for codigo, configuracao in PERGUNTAS_IPP.items():

        resposta = st.radio(
            configuracao['pergunta'],
            options=list(
                configuracao['opcoes'].keys()
            ),
            index=None,
            key=f'ipp_{codigo}'
        )

        if resposta is not None:
            respostas_ipp.append(
                configuracao['opcoes'][resposta]
            )

    st.radio(
        (
            '5) Baseado na sua experiência com o estudante, '
            'que recomendação você daria para a Associação?'
        ),
        options=RECOMENDACOES_IPP,
        index=None,
        key='ipp_q5'
    )

    st.divider()

    if len(respostas_ipp) == 4:
        return round(
            sum(respostas_ipp),
            3
        )

    return None


# ---------------------------------------------------------
# IPV — Indicador de Ponto de Virada
# ---------------------------------------------------------

def calcular_ipv():

    st.markdown(
        '#### IPV — Indicador de Ponto de Virada'
    )

    respostas_ipv = []

    for codigo, configuracao in PERGUNTAS_IPV.items():

        resposta = st.radio(
            configuracao['pergunta'],
            options=list(
                configuracao['opcoes'].keys()
            ),
            index=None,
            key=f'ipv_{codigo}'
        )

        if resposta is not None:
            respostas_ipv.append(
                configuracao['opcoes'][resposta]
            )

    st.divider()

    if len(respostas_ipv) == 9:
        return round(
            sum(respostas_ipv),
            3
        )

    return None

def calcular_inde(
    idade,
    ida,
    ieg,
    iaa,
    ips,
    ipp,
    ipv
):

    # -----------------------------------------------------
    # IAN simulado pela idade
    # -----------------------------------------------------

    if idade <= 9:
        ian = 8.5

    elif idade < 18:
        ian = 7.1

    else:
        ian = 5.5


    # -----------------------------------------------------
    # Agrupamento 1
    # Idade < 18
    # Equivalente à composição das Fases 0 a 7
    # -----------------------------------------------------

    if idade < 18:

        indicadores = [
            ida,
            ieg,
            iaa,
            ips,
            ipp,
            ipv
        ]

        if any(
            valor is None
            for valor in indicadores
        ):
            return None

        inde = (
            (ian * 0.1)
            + (ida * 0.2)
            + (ieg * 0.2)
            + (iaa * 0.1)
            + (ips * 0.1)
            + (ipp * 0.1)
            + (ipv * 0.2)
        )


    # -----------------------------------------------------
    # Agrupamento 2
    # Idade >= 18
    # Equivalente à composição da Fase 8
    # -----------------------------------------------------

    else:

        indicadores = [
            ida,
            ieg,
            iaa,
            ips
        ]

        if any(
            valor is None
            for valor in indicadores
        ):
            return None

        inde = (
            (ian * 0.1)
            + (ida * 0.4)
            + (ieg * 0.2)
            + (iaa * 0.1)
            + (ips * 0.2)
        )


    return round(
        inde,
        3
    )

# ---------------------------------------------------------
# Reset do Questionário
# ---------------------------------------------------------

def resetar_questionario():

    prefixos = (
        'iaa_',
        'ips_',
        'ipp_',
        'ipv_'
    )

    chaves = [
        'idade',
        'genero',
        'instituicao',
        'portugues',
        'matematica',
        'ingles',
        'atividades_solicitadas',
        'atividades_entregues'
    ]

    for chave in list(st.session_state.keys()):

        if (
            chave in chaves
            or chave.startswith(prefixos)
        ):
            del st.session_state[chave]


# ---------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------

col_logo, col_titulo = st.columns([1, 6])

with col_logo:
    st.image(
        'https://raw.githubusercontent.com/andersonserrico/'
        'Datathon_TerraJourney_Grupo48/main/extrainfo/'
        'TerraJourney_logo_branco.svg',
        width=120
    )

with col_titulo:
    st.title(
        'Modelo de Riscos de Desenvolvimento Infantil'
    )


# ---------------------------------------------------------
# Identificação
# ---------------------------------------------------------

st.subheader('Identificação')

st.write(
    'Identifique se o aluno já está cadastrado no programa.'
)

aluno_cadastrado = st.radio(
    'O aluno já tem um RA cadastrado?',
    options=[
        'Sim',
        'Não'
    ],
    index=None,
    horizontal=True,
    key='aluno_cadastrado',
    on_change=resetar_questionario
)


questionario_identificacao = False


# ---------------------------------------------------------
# Aluno cadastrado
# ---------------------------------------------------------

if aluno_cadastrado == 'Sim':

    ra = st.number_input(
        'Informe o RA do aluno:',
        min_value=0,
        step=1,
        value=None,
        placeholder='RA99999',
        key='ra'
    )

    # Validação temporária do RA
    ra_validado = False

    if ra is not None:

        # Depois será substituído pela validação real
        # consultando a base de alunos.
        ra_validado = True

    if ra_validado:
        questionario_identificacao = True


# ---------------------------------------------------------
# Aluno não cadastrado
# ---------------------------------------------------------

elif aluno_cadastrado == 'Não':

    col_idade, col_genero, col_instituicao = st.columns(3)

    with col_idade:

        idade = st.slider(
            'Idade:',
            min_value=7,
            max_value=30,
            value=7,
            step=1,
            key='idade'
        )

    with col_genero:

        genero = st.selectbox(
            'Gênero:',
            options=[
                'Masculino',
                'Feminino'
            ],
            index=None,
            placeholder='Selecione',
            key='genero'
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
            placeholder='Selecione',
            key='instituicao'
        )

    if (
        idade is not None
        and genero is not None
        and instituicao is not None
    ):
        questionario_identificacao = True


else:

    st.warning(
        'Selecione uma opção para continuar.'
    )


st.divider()


# ---------------------------------------------------------
# Questionários
# ---------------------------------------------------------

if questionario_identificacao:

    st.subheader(
        'Questionários de Avaliação'
    )

    calculo_ida = calcular_ida()

    calculo_ieg = calcular_ieg()

    calculo_iaa = calcular_iaa(idade)

    calculo_ips = calcular_ips()
    
    calculo_ipp = calcular_ipp()

    calculo_ipv = calcular_ipv()

    # ---------------------------------------------------------
    # Validação dos Dados
    # ---------------------------------------------------------

    if st.button('Validar'):

        erros = []

        # -----------------------------------------------------
        # IDA
        # -----------------------------------------------------

        if calculo_ida is None:
            erros.append(
                'Informe as notas de Português e Matemática.'
            )

        # -----------------------------------------------------
        # IEG
        # -----------------------------------------------------

        if calculo_ieg is None:
            erros.append(
                'Não foi possível calcular o IEG.'
            )


        # -----------------------------------------------------
        # IAA
        # -----------------------------------------------------

        if calculo_iaa is None:
            erros.append(
                'Responda todas as questões do IAA.'
            )


        # -----------------------------------------------------
        # IPS
        # -----------------------------------------------------

        if calculo_ips is None:
            erros.append(
                'Responda todas as questões do IPS.'
            )


        # -----------------------------------------------------
        # IPP
        # -----------------------------------------------------

        if calculo_ipp is None:
            erros.append(
                'Responda todas as questões do IPP.'
            )


        # -----------------------------------------------------
        # IPV
        # -----------------------------------------------------

        if calculo_ipv is None:
            erros.append(
                'Responda todas as questões do IPV.'
            )


        # -----------------------------------------------------
        # Verificação
        # -----------------------------------------------------

        if erros:

            st.error(
                'Existem informações que precisam ser corrigidas '
                'antes da validação.'
            )

            for erro in erros:
                st.warning(erro)

            st.stop()


        # -----------------------------------------------------
        # Dataset para o Modelo
        # -----------------------------------------------------

        calculo_inde = calcular_inde(
            idade,
            calculo_ida,
            calculo_ieg,
            calculo_iaa,
            calculo_ips,
            calculo_ipp,
            calculo_ipv
)

        dados_aluno = {
            'Idade': idade,
            'Genero': genero,
            'Instituicao_Ensino': instituicao,
            'IDA': calculo_ida,
            'IEG': calculo_ieg,
            'IAA': calculo_iaa,
            'IPS': calculo_ips,
            'IPP': calculo_ipp,
            'IPV': calculo_ipv,
            'INDE': calculo_inde
        }

        df_validacao = pd.DataFrame(
            [dados_aluno]
        )

        st.success(
            'Dados validados com sucesso.'
        )

        st.dataframe(
            df_validacao,
            width='stretch',
            hide_index=True
        )