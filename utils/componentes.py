
import streamlit as st

from html import escape
from textwrap import dedent
from typing import Iterable
from pathlib import Path

from utils.tema import obter_tema

def carregar_estilos(
    caminho_css: str = 'assets/style.css'
) -> None:
    caminho = Path(caminho_css)

    if not caminho.exists():
        st.warning(f'Arquivo de estilos não encontrado: {caminho_css}')
        return

    css = caminho.read_text(encoding='utf-8')

    for nome, cor in obter_tema().items():
        css = css.replace(f'{{{{{nome}}}}}', cor)

    st.markdown(
        f'<style>{css}</style>',
        unsafe_allow_html=True
    )


def exibir_hero(
    logo: str,
    subtitulo: str,
    largura: int = 420
) -> None:
    st.markdown(
        f'''
        <div class='hero'>
            <img
                src='{escape(logo)}'
                style='width: {largura}px; max-width: 85%; height: auto;'
                alt='Logo do projeto'
            >
            <div class='hero-subtitulo'>
                {escape(subtitulo)}
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )


def exibir_titulo_secao(
    titulo: str,
    texto: str
) -> None:
    st.markdown(
        f'''
        <div class='descricao-central'>
            <h2>{escape(titulo)}</h2>
            <p>{escape(texto)}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )


def exibir_card(
    icone: str,
    titulo: str,
    texto: str,
    destaque: bool = False
) -> None:
    classe = 'card card-destaque' if destaque else 'card'

    html_card = dedent(
        f'''
        <div class="{classe}">
            <div class="card-icone">{escape(icone)}</div>
            <div class="card-titulo">{escape(titulo)}</div>
            <div class="card-texto">{escape(texto)}</div>
        </div>
        '''
    ).strip()

    st.markdown(
        html_card,
        unsafe_allow_html=True
    )

def exibir_rodape(
    projeto: str,
    equipe: Iterable[str],
    versao: str
) -> None:
    integrantes = ' • '.join(escape(nome) for nome in equipe)

    st.markdown(
        f'''
        <div class='rodape'>
            <strong>{escape(projeto)}</strong>
            <br>
            {integrantes}
            <br><br>
            Versão {escape(versao)}
        </div>
        ''',
        unsafe_allow_html=True
    )

def exibir_descricao(
    titulo: str,
    paragrafos: list[str]
) -> None:
    conteudo_paragrafos = ''.join(
        f'<p>{escape(paragrafo)}</p>'
        for paragrafo in paragrafos
    )

    html = dedent(
        f'''
        <div class="descricao-central">
            <h2>{escape(titulo)}</h2>
            {conteudo_paragrafos}
        </div>
        '''
    ).strip()

    st.markdown(
        html,
        unsafe_allow_html=True
    )