# 📊 Datathon FIAP – Análise Educacional

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte do **Datathon FIAP**, utilizando dados da **Associação Passos Mágicos** para analisar o desempenho acadêmico, indicadores educacionais e fatores que influenciam a evolução dos alunos.

A aplicação foi construída com **Streamlit**, permitindo a exploração interativa dos dados por meio de análises, dashboards e modelos de Machine Learning.

---

## 🎯 Objetivos

- Realizar o tratamento e padronização da base de dados.
- Explorar os indicadores educacionais.
- Responder às perguntas de negócio propostas pelo Datathon.
- Construir dashboards interativos.
- Desenvolver modelo preditivo para apoio à tomada de decisão.

---

# 🚀 Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- XGBoost

---

# 📂 Estrutura do Projeto

```text
Datathon/
│
├── app.py
├── README.md
├── requirements.txt
│
├── assets/
│
├── dados/
│
├── notebooks/
│
├── pages/
│   ├── home.py
│   ├── analise_exploratoria.py
│   ├── dashboard.py
│   └── modelos.py
│
└── utils/
```

---

# 🖥️ Estrutura da Aplicação

A aplicação está organizada em quatro páginas principais.

## 🏠 Home

A página inicial apresenta uma visão geral do projeto.

Ela contém:

- Contexto do desafio;
- Objetivos;
- Descrição da base de dados;
- Tecnologias utilizadas;
- Organização da aplicação.

---

## 📈 Análise Exploratória

Nesta página são apresentadas as análises realizadas sobre a base de dados.

Entre elas:

- Estatísticas descritivas;
- Distribuições das variáveis;
- Correlações;
- Evolução dos indicadores;
- Comparações entre grupos;
- Respostas às perguntas analíticas do Datathon.

---

## 📊 Dashboard

O Dashboard apresenta uma visão consolidada dos principais indicadores do projeto.

Nesta página são disponibilizados gráficos interativos para análise de:

- Quantidade de alunos;
- Distribuição por gênero;
- Distribuição por idade;
- Instituições de ensino;
- Indicadores educacionais;
- Evolução dos resultados;
- Demais métricas relevantes.

Todos os gráficos permitem interação utilizando Plotly.

---

## 🤖 Modelos

Esta página apresenta os modelos de Machine Learning desenvolvidos durante o projeto.

São apresentados:

- Pré-processamento dos dados;
- Engenharia de atributos;
- Modelos treinados;
- Processo de treinamento;
- Métricas de avaliação;
- Comparação dos resultados.

---

# 🧭 Navegação

A estrutura da navegação no Streamlit está organizada da seguinte forma:

```text
Projeto
└── 🏠 Home

Análises
├── 📈 Análise Exploratória
└── 📊 Dashboard

Modelos
└── 🤖 Modelos
```

---

# ▶️ Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

## 2. Entre na pasta do projeto

```bash
cd Datathon
```

## 3. Crie um ambiente virtual (opcional)

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## 5. Execute a aplicação

```bash
streamlit run app.py
```

Após a execução, o Streamlit abrirá automaticamente a aplicação no navegador.

---

# 📌 Funcionalidades

- Interface desenvolvida em Streamlit;
- Navegação por múltiplas páginas;
- Análise Exploratória de Dados (EDA);
- Dashboard interativo;
- Visualizações utilizando Plotly;
- Modelos de Machine Learning;
- Código organizado de forma modular.

---

# 👥 Equipe

Projeto desenvolvido como parte do **Datathon FIAP**, aplicando técnicas de Ciência de Dados, Visualização de Dados e Machine Learning para análise de indicadores educacionais.