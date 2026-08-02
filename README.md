<div align="center">
  <img src="https://raw.githubusercontent.com/andersonserrico/Datathon_TerraJourney_Grupo48/main/extrainfo/TerraJourney_logo_branco.svg" alt="TerraJourney" width="350">
</div>

🌎 TerraJourney — Plataforma de Inteligência Educacional

FIAP Datathon 2026 • Grupo 48

O TerraJourney é uma plataforma de inteligência educacional desenvolvida para o Datathon FIAP 2026, utilizando dados da Associação Passos Mágicos.

O projeto transforma dados educacionais em informações estratégicas por meio de tratamento e análise de dados, visualizações interativas e técnicas de Machine Learning, permitindo compreender a trajetória dos estudantes e identificar fatores relacionados ao seu desenvolvimento acadêmico.

⸻

🎯 Missão

Impulsionar a Jornada do Conhecimento por meio da análise de dados educacionais, transformando informações em conhecimento estratégico para identificar oportunidades de desenvolvimento e fortalecer iniciativas que ampliem o impacto da educação na vida dos estudantes.

⸻

🔭 Visão

Conduzir a jornada do dado ao conhecimento, promovendo análises eficientes e inovadoras que apoiem decisões mais assertivas e ampliem as oportunidades de desenvolvimento dos estudantes.

⸻

📊 Indicadores Educacionais

As análises do TerraJourney exploram os principais indicadores disponibilizados pela Associação Passos Mágicos:

Indicador	Descrição
IAN	Indicador de Adequação de Nível
IDA	Indicador de Desempenho Acadêmico
IEG	Indicador de Engajamento
IAA	Indicador de Autoavaliação
IPS	Indicador Psicossocial
IPP	Indicador Psicopedagógico
IPV	Indicador de Ponto de Virada
INDE	Índice do Desenvolvimento Educacional

⸻

🔎 Análises Desenvolvidas

A plataforma apresenta análises voltadas às principais questões educacionais propostas pelo Datathon.

1. Defasagem Escolar — IAN

Análise da evolução da adequação dos estudantes às suas respectivas fases escolares, classificando-os em:

* Adequado (Em Fase);
* Defasagem Moderada;
* Defasagem Severa.

2. Desempenho Acadêmico — IDA

Avaliação da evolução do desempenho acadêmico dos estudantes ao longo das fases e dos anos.

3. Engajamento — IEG

Análise da relação entre o engajamento dos estudantes e:

* Desempenho Acadêmico (IDA);
* Ponto de Virada (IPV).

4. Autoavaliação — IAA

Avaliação da coerência entre a percepção dos estudantes sobre si mesmos e seus resultados acadêmicos e de engajamento.

5. Aspectos Psicossociais — IPS

Análise longitudinal para identificar se resultados psicossociais podem anteceder quedas futuras no desempenho ou no engajamento.

6. Aspectos Psicopedagógicos — IPP

Comparação das avaliações psicopedagógicas com os níveis de defasagem identificados pelo IAN.

7. Ponto de Virada — IPV

Análise dos indicadores que apresentam maior associação com o Ponto de Virada dos estudantes.

8. Nota Global — INDE

Avaliação da relação dos diferentes indicadores educacionais com o INDE.

9. Efetividade do Programa

Análise da progressão da Nota Global (INDE) ao longo das fases do programa, permitindo observar a evolução dos estudantes durante sua jornada educacional.

⸻

📈 Dashboard

O TerraJourney possui um dashboard interativo desenvolvido com Streamlit e Plotly.

O dashboard permite explorar visualmente informações da base educacional por meio de gráficos interativos e indicadores consolidados.

As visualizações seguem uma identidade visual própria do TerraJourney e foram estruturadas através de uma pipeline reutilizável de gráficos.

⸻

🤖 Modelo Preditivo

A plataforma também prevê uma área dedicada à aplicação de técnicas de Machine Learning.

O objetivo é utilizar os indicadores educacionais para desenvolver modelos capazes de apoiar a identificação de padrões e oportunidades de intervenção na trajetória dos estudantes.

⸻

🛠️ Tecnologias Utilizadas

O projeto utiliza principalmente:

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-learn
* Statsmodels
* OpenPyXL

⸻

📂 Estrutura do Projeto

Datathon_TerraJourney_Grupo48/

├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   └── style.css
│
├── dados/
│   ├── BASE_DATATHON_2024.xlsx
│   └── PEDE_Dados_Unificados.csv
│
├── extrainfo/
│   └── TerraJourney_logo_branco.svg
│
├── notebooks/
│   └── Tratamento_base.ipynb
│
├── paginas/
│   ├── home.py
│   ├── analises.py
│   ├── dashboard.py
│   └── modelo.py
│
└── utils/
├── init.py
├── componentes.py
├── graficos.py
└── tema.py

⸻

🖥️ Estrutura da Aplicação

A aplicação está organizada em quatro áreas principais:

🏠 Home

Apresentação do TerraJourney, contexto do projeto, missão, visão e principais funcionalidades da plataforma.

📊 Análises

Exploração dos indicadores educacionais e respostas às questões analíticas propostas pelo Datathon.

📈 Dashboard

Visualizações interativas que facilitam a exploração e interpretação dos dados educacionais.

🤖 Modelo Preditivo

Área destinada à aplicação e apresentação das técnicas de Machine Learning utilizadas no projeto.

⸻

▶️ Como executar o projeto

1. Clone o repositório

git clone https://github.com/andersonserrico/Datathon_TerraJourney_Grupo48.git

2. Entre no diretório

cd Datathon_TerraJourney_Grupo48

3. Crie um ambiente virtual

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv
.venv\Scripts\activate

4. Instale as dependências

pip install -r requirements.txt

5. Execute o Streamlit

streamlit run app.py

⸻

📦 Dependências

As principais dependências estão definidas no arquivo requirements.txt:

* streamlit
* pandas
* plotly
* numpy
* openpyxl
* scikit-learn
* statsmodels

⸻

👥 Equipe

FIAP Datathon 2026 — Grupo 48

* Anderson — RM368309
* Júlia — RM367721
* Maike — RM367843
* Rafaell — RM368753

⸻

🌎 TerraJourney

Da jornada do dado ao conhecimento.