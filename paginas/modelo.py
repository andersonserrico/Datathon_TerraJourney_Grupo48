import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

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


# =========================================================
# Carregamento do Modelo
# =========================================================

@st.cache_resource
def carregar_artefato_modelo():
    caminho_modelo = (
        Path(__file__).resolve().parents[1]
        / 'modelo'
        / 'modelo_risco.pkl'
        )

    return joblib.load(
        caminho_modelo
    )


artefato_modelo = carregar_artefato_modelo()

modelo_risco = artefato_modelo[
    'modelo'
]

limiar_risco = (
    artefato_modelo[
        'avaliacao'
    ][
        'limiar_classificacao'
    ]
)


# =========================================================
# Leitura da Base de Dados
# =========================================================

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


# =========================================================
# IDA — Indicador de Desempenho Acadêmico
# =========================================================

def calcular_ida():

    st.markdown(
        '#### IDA — Indicador de Desempenho Acadêmico'
    )

    col_portugues, col_matematica, col_ingles = (
        st.columns(3)
    )

    with col_portugues:

        portugues = st.number_input(
            'Português:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0',
            key='portugues'
        )

    with col_matematica:

        matematica = st.number_input(
            'Matemática:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0',
            key='matematica'
        )

    with col_ingles:

        ingles = st.number_input(
            'Inglês:',
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.5,
            format='%.3f',
            placeholder='6.0',
            key='ingles'
        )

    st.divider()

    if (
        portugues is None
        or matematica is None
    ):
        return None

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


# =========================================================
# IEG — Indicador de Engajamento
# =========================================================

def calcular_ieg():

    st.markdown(
        '#### IEG — Indicador de Engajamento'
    )

    col_solicitadas, col_entregues = (
        st.columns(2)
    )

    with col_solicitadas:

        atividades_solicitadas = st.slider(
            'Atividades solicitadas:',
            min_value=10,
            max_value=25,
            value=10,
            step=1,
            key='atividades_solicitadas'
        )

    with col_entregues:

        atividades_entregues = st.slider(
            'Atividades entregues:',
            min_value=0,
            max_value=25,
            value=5,
            step=1,
            key='atividades_entregues'
        )

    st.divider()

    if (
        atividades_entregues
        > atividades_solicitadas
    ):
        return None

    calculo_ieg = (
        atividades_entregues
        / atividades_solicitadas
        * 10
    )

    return round(
        calculo_ieg,
        3
    )


# =========================================================
# IAA — Indicador de Autoavaliação
# =========================================================

def calcular_iaa(idade):

    st.markdown(
        '#### IAA — Indicador de Autoavaliação'
    )

    respostas_iaa = []

    if idade <= 11:

        for codigo, pergunta in (
            PERGUNTAS_IAA.items()
        ):

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
                    OPCOES_IAA_INICIAL[
                        resposta
                    ]
                )

    else:

        for codigo, pergunta in (
            PERGUNTAS_IAA.items()
        ):

            resposta = st.radio(
                pergunta,
                options=list(
                    OPCOES_IAA_AVANCADO[
                        codigo
                    ].keys()
                ),
                index=None,
                key=f'iaa_{codigo}'
            )

            if resposta is not None:

                respostas_iaa.append(
                    OPCOES_IAA_AVANCADO[
                        codigo
                    ][
                        resposta
                    ]
                )

    st.divider()

    if len(respostas_iaa) != 6:
        return None

    return round(
        sum(respostas_iaa),
        3
    )


# =========================================================
# IPS — Indicador de Aspectos Psicossociais
# =========================================================

def calcular_ips():

    st.markdown(
        '#### IPS — Indicador de Aspectos Psicossociais'
    )

    respostas_ips = []

    for codigo, configuracao in (
        PERGUNTAS_IPS.items()
    ):

        resposta = st.radio(
            configuracao[
                'pergunta'
            ],
            options=list(
                configuracao[
                    'opcoes'
                ].keys()
            ),
            index=None,
            key=f'ips_{codigo}'
        )

        if resposta is not None:

            respostas_ips.append(
                configuracao[
                    'opcoes'
                ][
                    resposta
                ]
            )

    st.divider()

    if len(respostas_ips) != 4:
        return None

    return round(
        sum(respostas_ips),
        3
    )


# =========================================================
# IPP — Indicador de Aspectos Psicopedagógicos
# =========================================================

def calcular_ipp():

    st.markdown(
        '#### IPP — Indicador de Aspectos Psicopedagógicos'
    )

    respostas_ipp = []

    for codigo, configuracao in (
        PERGUNTAS_IPP.items()
    ):

        resposta = st.radio(
            configuracao[
                'pergunta'
            ],
            options=list(
                configuracao[
                    'opcoes'
                ].keys()
            ),
            index=None,
            key=f'ipp_{codigo}'
        )

        if resposta is not None:

            respostas_ipp.append(
                configuracao[
                    'opcoes'
                ][
                    resposta
                ]
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

    if len(respostas_ipp) != 4:
        return None

    return round(
        sum(respostas_ipp),
        3
    )


# =========================================================
# IPV — Indicador de Ponto de Virada
# =========================================================

def calcular_ipv():

    st.markdown(
        '#### IPV — Indicador de Ponto de Virada'
    )

    respostas_ipv = []

    for codigo, configuracao in (
        PERGUNTAS_IPV.items()
    ):

        resposta = st.radio(
            configuracao[
                'pergunta'
            ],
            options=list(
                configuracao[
                    'opcoes'
                ].keys()
            ),
            index=None,
            key=f'ipv_{codigo}'
        )

        if resposta is not None:

            respostas_ipv.append(
                configuracao[
                    'opcoes'
                ][
                    resposta
                ]
            )

    st.divider()

    if len(respostas_ipv) != 9:
        return None

    return round(
        sum(respostas_ipv),
        3
    )


# =========================================================
# INDE — Indicador de Desenvolvimento Educacional
# =========================================================

def calcular_inde(
    idade,
    ian,
    ida,
    ieg,
    iaa,
    ips,
    ipp,
    ipv
):

    # -----------------------------------------------------
    # Agrupamento 1
    # Idade < 18
    # -----------------------------------------------------

    if idade < 18:

        indicadores = [
            ian,
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
    # -----------------------------------------------------

    else:

        indicadores = [
            ian,
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


# =========================================================
# Reset do Questionário
# =========================================================

def resetar_questionario():

    prefixos = (
        'iaa_',
        'ips_',
        'ipp_',
        'ipv_'
    )

    chaves = [
        'ra',
        'idade',
        'genero',
        'instituicao',
        'ian',
        'portugues',
        'matematica',
        'ingles',
        'atividades_solicitadas',
        'atividades_entregues'
    ]

    for chave in list(
        st.session_state.keys()
    ):

        if (
            chave in chaves
            or chave.startswith(
                prefixos
            )
        ):

            del st.session_state[
                chave
            ]


# =========================================================
# Cabeçalho
# =========================================================

col_logo, col_titulo = st.columns(
    [
        1,
        6
    ]
)

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


# =========================================================
# Identificação
# =========================================================

st.subheader(
    'Identificação'
)

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

idade = None
genero_modelo = None
instituicao_modelo = None


# =========================================================
# Aluno cadastrado
# =========================================================

if aluno_cadastrado == 'Sim':

    ra = st.number_input(
        'Informe o RA do aluno:',
        min_value=0,
        step=1,
        value=None,
        placeholder='RA99999',
        key='ra'
    )

    if ra is None:

        st.info(
            'Informe o RA para continuar.'
        )

    else:

        ra_busca = (
            f'RA-{int(ra)}'
        )

        registros_aluno = (
            dados[
                dados['RA'] == ra_busca
            ]
            .copy()
        )

        if registros_aluno.empty:

            st.error(
                f'O RA {ra_busca} não foi encontrado '
                f'na base de dados.'
            )

            questionario_identificacao = False

        else:

            # -------------------------------------------------
            # Histórico do aluno
            # -------------------------------------------------

            colunas_historico = [
                'Ano_Referencia',
                'Idade',
                'Genero',
                'IAN',
                'IDA',
                'IEG',
                'IPS',
                'IPP',
                'IAA',
                'IPV',
                'INDE',
                'Instituicao_Ensino'
            ]

            df_historico_aluno = (
                registros_aluno[
                    colunas_historico
                ]
                .copy()
                .sort_values(
                    'Ano_Referencia'
                )
            )

            # -------------------------------------------------
            # Visualização do histórico
            # -------------------------------------------------

            df_historico_exibicao = (
                df_historico_aluno
                .rename(
                    columns={
                        'Ano_Referencia': 'Ano',
                        'Instituicao_Ensino': 'Instituição'
                    }
                )
            )

            st.success(
                f'Aluno {ra_busca} localizado com sucesso.'
            )

            st.markdown(
                '#### Histórico do Aluno'
            )

            st.dataframe(
                df_historico_exibicao,
                width='stretch',
                hide_index=True
            )

            # -------------------------------------------------
            # Dados cadastrais mais recentes
            # -------------------------------------------------

            registro_atual = (
                df_historico_aluno
                .sort_values(
                    'Ano_Referencia'
                )
                .iloc[-1]
            )

            idade = registro_atual[
                'Idade'
            ]

            genero_modelo = registro_atual[
                'Genero'
            ]

            instituicao_modelo = registro_atual[
                'Instituicao_Ensino'
            ]

            # -------------------------------------------------
            # Validação dos dados necessários ao modelo
            # -------------------------------------------------

            if (
                pd.isna(idade)
                or pd.isna(genero_modelo)
                or pd.isna(instituicao_modelo)
            ):

                st.error(
                    'O registro mais recente do aluno não possui '
                    'todos os dados necessários para a previsão.'
                )

                questionario_identificacao = False

            else:

                idade = int(
                    idade
                )

                questionario_identificacao = True


# =========================================================
# Aluno não cadastrado
# =========================================================

elif aluno_cadastrado == 'Não':

    col_idade, col_genero, col_instituicao = (
        st.columns(3)
    )

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

        mapa_genero = {
            'Masculino': 'M',
            'Feminino': 'F'
        }

        mapa_instituicao = {
            'Pública': 'Publica',
            'Privado': 'Privada',
            'Bolsista': 'Bolsista',
            'Outros': 'Outros'
        }

        genero_modelo = (
            mapa_genero[
                genero
            ]
        )

        instituicao_modelo = (
            mapa_instituicao[
                instituicao
            ]
        )

        questionario_identificacao = True


# =========================================================
# Nenhuma opção selecionada
# =========================================================

else:

    st.warning(
        'Selecione uma opção para continuar.'
    )


st.divider()


# =========================================================
# Questionários
# =========================================================

if questionario_identificacao:

    st.subheader(
        'Questionários de Avaliação'
    )


    # -----------------------------------------------------
    # IAN
    # -----------------------------------------------------

    st.markdown(
        '#### IAN — Indicador de Adequação de Nível'
    )

    ian = st.select_slider(
        'Selecione o IAN:',
        options=[
            2.5,
            5.0,
            10.0
        ],
        value=5.0,
        key='ian'
    )

    ian = float(
        ian
    )

    st.divider()


    # -----------------------------------------------------
    # Demais indicadores
    # -----------------------------------------------------

    calculo_ida = calcular_ida()

    calculo_ieg = calcular_ieg()

    calculo_iaa = calcular_iaa(
        idade
    )

    calculo_ips = calcular_ips()

    calculo_ipp = calcular_ipp()

    calculo_ipv = calcular_ipv()


    # =====================================================
    # Botão de Validação
    # =====================================================

    if st.button(
        'Validar'
    ):

        erros = []


        # -------------------------------------------------
        # IDA
        # -------------------------------------------------

        if calculo_ida is None:

            erros.append(
                'Informe as notas de Português '
                'e Matemática.'
            )


        # -------------------------------------------------
        # IEG
        # -------------------------------------------------

        if calculo_ieg is None:

            erros.append(
                'A quantidade de atividades '
                'entregues não pode ser maior '
                'que a quantidade de atividades '
                'solicitadas.'
            )


        # -------------------------------------------------
        # IAA
        # -------------------------------------------------

        if calculo_iaa is None:

            erros.append(
                'Responda todas as questões '
                'do IAA.'
            )


        # -------------------------------------------------
        # IPS
        # -------------------------------------------------

        if calculo_ips is None:

            erros.append(
                'Responda todas as questões '
                'do IPS.'
            )


        # -------------------------------------------------
        # IPP
        # -------------------------------------------------

        if calculo_ipp is None:

            erros.append(
                'Responda todas as questões '
                'do IPP.'
            )


        # -------------------------------------------------
        # IPV
        # -------------------------------------------------

        if calculo_ipv is None:

            erros.append(
                'Responda todas as questões '
                'do IPV.'
            )


        # =================================================
        # Verificação
        # =================================================

        if erros:

            st.error(
                'Existem informações que precisam '
                'ser corrigidas antes da validação.'
            )

            for erro in erros:

                st.warning(
                    erro
                )

            st.stop()


        # =================================================
        # Cálculo do INDE
        # =================================================

        calculo_inde = calcular_inde(
            idade,
            ian,
            calculo_ida,
            calculo_ieg,
            calculo_iaa,
            calculo_ips,
            calculo_ipp,
            calculo_ipv
        )


        if calculo_inde is None:

            st.error(
                'Não foi possível calcular o INDE.'
            )

            st.stop()


        # =================================================
        # DataFrame Final
        # =================================================

        dados_aluno = {
            'INDE': calculo_inde,
            'IAN': ian,
            'IDA': calculo_ida,
            'IEG': calculo_ieg,
            'IPS': calculo_ips,
            'IPP': calculo_ipp,
            'IAA': calculo_iaa,
            'IPV': calculo_ipv,
            'Idade': idade,
            'Genero': genero_modelo,
            'Instituicao_Ensino': instituicao_modelo
        }


        df_validacao = pd.DataFrame(
            [
                dados_aluno
            ]
        )


        # =================================================
        # DataFrame para Predição
        # =================================================

        df_modelo = df_validacao.copy()

        # =================================================
        # Predição
        # =================================================

        probabilidade_risco = (
            modelo_risco
            .predict_proba(
                df_modelo
            )[0, 1]
        )


        risco_predito = (
            probabilidade_risco
            >= limiar_risco
        )


        # =================================================
        # Dataset Validado
        # =================================================

        st.success(
            'Dados validados com sucesso.'
        )


        st.dataframe(
            df_validacao,
            width='stretch',
            hide_index=True
        )


        st.divider()


        # =================================================
        # Resultado do Modelo
        # =================================================

        st.subheader(
            'Resultado da Avaliação de Risco'
        )


        col_probabilidade, col_classificacao = (
            st.columns(2)
        )


        with col_probabilidade:

            st.metric(
                'Probabilidade de Risco',
                (
                    f'{probabilidade_risco * 100:.1f}%'
                )
            )


        with col_classificacao:

            if risco_predito:

                st.metric(
                    'Classificação',
                    'Risco de Defasagem'
                )

            else:

                st.metric(
                    'Classificação',
                    'Baixo Risco'
                )


        # =================================================
        # Interpretação
        # =================================================

        if risco_predito:

            st.warning(
                f'O aluno apresentou uma probabilidade '
                f'de {probabilidade_risco * 100:.1f}% '
                f'de risco de defasagem, acima do '
                f'limiar de '
                f'{limiar_risco * 100:.0f}% definido '
                f'para o modelo.'
            )

        else:

            st.success(
                f'O aluno apresentou uma probabilidade '
                f'de {probabilidade_risco * 100:.1f}% '
                f'de risco de defasagem, abaixo do '
                f'limiar de '
                f'{limiar_risco * 100:.0f}% definido '
                f'para o modelo.'
            )