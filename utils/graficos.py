import plotly.express as px

from utils.tema import (
    PALETA_PLOTLY,
    COR_PRIMARIA,
    COR_PRIMARIA_ESCURA,
    COR_PRIMARIA_CLARA,
    COR_SECUNDARIA_CLARA
)


def criar_grafico(
    tipo: str,
    dados,
    x: str | None = None,
    y: str | list[str] | None = None,
    color: str | None = None,
    titulo: str | None = None,
    texto: str | None = None,
    color_map: dict | None = None,
    paleta: list[str] | None = None,
    mostrar_legenda: bool = False,
    titulo_eixo_x: str | None = None,
    titulo_eixo_y: str | None = None,
    modo_barra: str = 'group',
    trendline: str | None = None
):
    df = dados.copy()

    # -----------------------------------------------------
    # Configuração padrão
    # -----------------------------------------------------

    configuracao = {
        'data_frame': df
    }

    if x is not None:
        configuracao['x'] = x

    if y is not None:
        configuracao['y'] = y

    if color is not None:
        configuracao['color'] = color

    if texto is not None:
        configuracao['text'] = texto


    # -----------------------------------------------------
    # Cores
    # -----------------------------------------------------

    if color_map is not None:
        configuracao['color_discrete_map'] = color_map

    elif paleta is not None:
        configuracao['color_discrete_sequence'] = paleta

    else:
        configuracao['color_discrete_sequence'] = PALETA_PLOTLY


    # -----------------------------------------------------
    # Tipo de gráfico
    # -----------------------------------------------------

    if tipo == 'bar':
        fig = px.bar(
            **configuracao,
            barmode=modo_barra
        )

    elif tipo == 'bar_horizontal':
        fig = px.bar(
            **configuracao,
            orientation='h',
            barmode=modo_barra
        )

    elif tipo == 'line':
        fig = px.line(
            **configuracao,
            markers=True
        )

    elif tipo == 'box':
        fig = px.box(
            **configuracao,
            points='all'
        )

    elif tipo == 'scatter':
        fig = px.scatter(
            **configuracao,
            color_continuous_scale=[
                COR_PRIMARIA_ESCURA,
                COR_PRIMARIA,
                COR_PRIMARIA_CLARA
            ],           
            trendline=trendline
        )

    elif tipo == 'hist':
        fig = px.histogram(
            **configuracao
        )

    elif tipo == 'heatmap':
        fig = px.imshow(
            df,
            text_auto='.2f',
            aspect='auto',
            color_continuous_scale=[
                COR_PRIMARIA_CLARA,
                COR_PRIMARIA,
                COR_PRIMARIA_ESCURA
            ],
            zmin=-1,
            zmax=1
        )

    else:
        raise ValueError(
            f'Tipo de gráfico não suportado: {tipo}'
        )


    # -----------------------------------------------------
    # Layout padrão
    # -----------------------------------------------------

    fig.update_layout(
        showlegend=mostrar_legenda,
        xaxis_title=titulo_eixo_x,
        yaxis_title=titulo_eixo_y,
        margin=dict(
            l=20,
            r=20,
            t=70 if titulo is not None else 30,
            b=20
        )
    )


    # -----------------------------------------------------
    # Título opcional
    # -----------------------------------------------------

    if titulo is not None:
        fig.update_layout(
            title={
                'text': titulo,
                'font': {
                    'color': COR_SECUNDARIA_CLARA
                }
            }
        )


    # -----------------------------------------------------
    # Texto nas barras
    # -----------------------------------------------------

    if (
        tipo in ['bar', 'bar_horizontal']
        and texto is not None
    ):
        fig.update_traces(
            textposition='outside'
        )


    return fig