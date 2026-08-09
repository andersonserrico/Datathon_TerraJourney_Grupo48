<div align="center">
  <img src="https://raw.githubusercontent.com/andersonserrico/Datathon_TerraJourney_Grupo48/main/extrainfo/TerraJourney_logo_branco.svg" alt="Logo TerraJourney" width="250">
</div>


# TerraJourney --- FIAP Datathon 2026

Plataforma de Inteligência Educacional desenvolvida pelo **Grupo 48**
para o Datathon da FIAP, utilizando dados da **Associação Passos
Mágicos**.

O projeto transforma dados educacionais em análises, insights e um
modelo preditivo voltado à identificação de estudantes com **risco
futuro de defasagem**, apoiando a tomada de decisão e a priorização de
ações de acompanhamento.

## Links

🔗 **Acesse a aplicação em produção:** [Clique aqui para abrir o Sistema](https://datathonterrajourneygrupo48-ezv3pfwsutzlalyxhqhfkv.streamlit.app)

🔗 **Apresentação do Modelo, Análises e Aplicação:** [Clique aqui para o link do video](https://drive.google.com/file/d/1EhtkhEnFg0ps6NX0QnUPJhZy4WXtSoBy/view?usp=share_link)

---

## Sobre o projeto

O TerraJourney foi desenvolvido para apoiar a análise da trajetória
educacional dos estudantes atendidos pela Associação Passos Mágicos.

A solução reúne duas frentes principais:

1.  **Análises dos Indicadores Educacionais** --- exploração dos
    indicadores acadêmicos, psicossociais e psicopedagógicos, além de
    insights complementares sobre a evolução dos alunos.
2.  **Modelo Preditivo** --- estimativa da probabilidade de risco futuro
    de defasagem a partir das informações disponíveis no período atual.

### Missão

Impulsionar a Jornada do Conhecimento por meio da análise de dados
educacionais, transformando informações em conhecimento estratégico para
identificar oportunidades de desenvolvimento e fortalecer iniciativas
que ampliem o impacto da educação na vida dos estudantes.

### Visão

Conduzir a jornada do dado ao conhecimento, promovendo análises
eficientes e inovadoras que apoiem decisões mais assertivas e ampliem as
oportunidades de desenvolvimento dos estudantes.

## Estrutura da aplicação

A aplicação Streamlit está organizada atualmente em três páginas
principais:

### Home

Página inicial do TerraJourney, apresentando a proposta da plataforma,
missão, visão e acesso às principais áreas do projeto.

### Análises

Página dedicada à exploração dos indicadores educacionais e aos
principais insights obtidos a partir dos dados.

Entre as análises disponibilizadas estão:

-   **Defasagem Escolar --- IAN**
-   **Desempenho Escolar --- IDA**
-   **Engajamento --- IEG**
-   **Autoavaliação --- IAA**
-   **Aspectos Psicossociais --- IPS**
-   **Aspectos Psicopedagógicos --- IPP**
-   **Ponto de Virada --- IPV**
-   **Nota Global --- INDE**
-   **Efetividade do Programa --- Evolução do INDE**
-   **Modelo Preditivo --- Risco de Defasagem**
-   **Insights --- Disciplinas Impactadas**
-   **Insights --- Ponto de Virada**
-   **Insight --- Perfil de Risco Futuro**

As análises são selecionadas por meio de um menu, permitindo que o
usuário visualize somente o conteúdo desejado.

### Modelo

Página destinada à aplicação do modelo de risco.

Para alunos não cadastrados, a aplicação permite preencher informações
do estudante e responder aos questionários necessários para o cálculo
dos indicadores.

Para alunos cadastrados, o RA é utilizado para localizar o histórico
disponível na base de dados antes da continuidade da avaliação.

## Indicadores educacionais

O projeto utiliza os principais indicadores presentes na base da
Associação Passos Mágicos:

  Indicador   Descrição
  ----------- ------------------------------------------
  **IAN**     Indicador de Adequação de Nível
  **IDA**     Indicador de Desempenho Acadêmico
  **IEG**     Indicador de Engajamento
  **IAA**     Indicador de Autoavaliação
  **IPS**     Indicador de Aspectos Psicossociais
  **IPP**     Indicador de Aspectos Psicopedagógicos
  **IPV**     Indicador de Ponto de Virada
  **INDE**    Indicador de Desenvolvimento Educacional

## Modelo preditivo de risco futuro

O objetivo do modelo é estimar o **risco futuro de defasagem** do
estudante.

### Construção do target

O target `RISCO_FUTURO` foi construído exclusivamente a partir do **IAN
realmente observado no ano seguinte**.

A regra utilizada foi:

``` python
RISCO_FUTURO = 1 if IAN_FUTURO < 10 else 0
```

Dessa forma:
-   `0` representa estudante sem risco futuro segundo a regra definida;
-   `1` representa estudante com risco futuro de defasagem.

### Separação dos dados

A divisão entre treino e teste foi realizada por **RA**, evitando que
registros do mesmo estudante aparecessem simultaneamente nos dois
conjuntos.

A validação cruzada utilizou **StratifiedGroupKFold**, preservando tanto
a separação por estudante quanto a distribuição da variável alvo.

### Seleção do modelo

Diferentes algoritmos foram avaliados durante o desenvolvimento.

O **Gradient Boosting** apresentou o melhor equilíbrio entre as métricas
avaliadas, especialmente:

-   ROC AUC;
-   Recall;
-   F1-score.

O desempenho entre Cross-Validation e conjunto de teste também se
manteve semelhante, contribuindo para a escolha do modelo final.

### Features

O modelo utiliza informações educacionais e de perfil disponíveis no
período atual.

Entre as variáveis com maior importância no modelo estão:

-   **IPP**
-   **Idade**
-   **IAN**
-   **INDE**

A idade apresentou uma relação não linear com o risco: a taxa foi mais
elevada entre 7--9 anos, caiu entre 10--13 anos e voltou a aumentar
entre 14--17 anos. A faixa de 18 anos ou mais possui poucos registros e,
portanto, não permite conclusões robustas.

O artefato salvo também contém informações utilizadas pelas análises da
aplicação, incluindo importância das features, probabilidades do
conjunto de teste e análises de risco por idade, gênero e instituição de
ensino.


## Estrutura do projeto

``` text
Datathon_TerraJourney_Grupo48/
│
├── app.py
│
├── requirements.txt
│
├── assets/
│   └── style.css
│
├── dados/
│   └── Base_DATATHON_2024.xlsx
│   └── PEDE_Dados_Unificados.csv
│
├── modelo/
│   └── modelo_risco.pkl
│
├── notebooks/
│   └── Modelo_TerraJourney.ipynb
│   └── Tratamento_base.ipynb
│
├── paginas/
│   ├── home.py
│   ├── analises.py
│   └── modelo.py
│
├── utils/
│   ├── componentes.py
│   ├── graficos.py
│   ├── questionarios.py
│   └── tema.py
│
└── .streamlit/
    └── config.toml
```

## Requirements.txt
-   Streamlit
-   Pandas
-   Plotly
-   NumPy
-   openpyxl
-   Scikit-learn
-   Scypy
-   statsmodels
-   Joblib

## Equipe --- Grupo 48

-   **Anderson Serrico de Oliveira** --- RM368309
-   **Maike** --- RM367843
-   **Rafaell** --- RM368753

## FIAP Datathon 2026

Projeto desenvolvido como parte do **Datathon da Pós-Graduação FIAP ---
Data Analytics**, utilizando dados educacionais da Associação Passos
Mágicos.

------------------------------------------------------------------------

**TerraJourney --- Do dado ao conhecimento.**
