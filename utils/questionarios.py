# =========================================================
# QUESTIONÁRIOS DOS INDICADORES
# =========================================================

# =========================================================
# IAA — Indicador de Autoavaliação
# =========================================================

PERGUNTAS_IAA = {
    'Q1': '1) Como você se sente consigo mesmo?',
    'Q2': '2) Como você se sente na hora de estudar?',
    'Q3': '3) Como você se sente quando está com sua família?',
    'Q4': '4) Como você se sente quando está com amigos?',
    'Q5': '5) Como você se sente quando está no Passos Mágicos?',
    'Q6': '6) Como você se sente sobre seus Professores na Passos Mágicos?'
}


OPCOES_IAA_INICIAL = {
    '😄 Animado': 1.667,
    '🙂 Bem': 1.167,
    '😔 Triste': 0.583
}


OPCOES_IAA_AVANCADO = {

    'Q1': {
        'Sinto-me feliz e confiante': 1.667,
        'Apesar de nem sempre tudo estar bem, eu me sinto feliz e esperançoso': 1.250,
        'Tem sido difícil me motivar, nem sempre me sinto bem comigo mesmo': 0.833,
        'Não tenho me sentido bem, preciso de ajuda': 0.417
    },

    'Q2': {
        'Tenho disposição e vontade de estudar': 1.667,
        'Dou importância aos estudos, mas nem sempre tenho vontade de estudar': 1.250,
        'Estudo apenas o necessário': 0.833,
        'Preferia não ter que estudar tanto, não sinto vontade': 0.417
    },

    'Q3': {
        'Muito satisfeito': 1.667,
        'A maior parte das vezes satisfeito': 1.250,
        'Muitas vezes insatisfeito': 0.833,
        'Não sei lidar com isso, preciso de ajuda': 0.417
    },

    'Q4': {
        'Muito satisfeito': 1.667,
        'A maior parte das vezes satisfeito': 1.250,
        'Muitas vezes insatisfeito': 0.833,
        'Não sei lidar com isso, preciso de ajuda': 0.417
    },

    'Q5': {
        'Sinto-me feliz e animado': 1.667,
        'Gosto muito do Passos Mágicos, mas nem sempre me sinto à vontade': 1.250,
        'Gosto do Passos Mágicos, mas não sinto que faço parte dele': 0.833,
        'Não me sinto um aluno Passos Mágicos': 0.417
    },

    'Q6': {
        'Sinto-me feliz e acolhido': 1.667,
        'Gosto dos Professores, mas nem sempre me sinto à vontade': 1.250,
        'Acho que os Professores não me valorizam': 0.833,
        'Não me sinto muito bem com os Professores': 0.417
    }
}


# =========================================================
# IPS — Indicador de Aspectos Psicossociais
# =========================================================

PERGUNTAS_IPS = {

    'Q1': {
        'pergunta': (
            '1) Como a equipe de Psicologia caracteriza o momento '
            'do estudante na sua dinâmica familiar?'
        ),
        'opcoes': {
            'A — Demonstra dinâmica familiar funcional e boa interação': 2.50,
            'B — Demonstra dinâmica geral funcional': 1.88,
            'C — Apresenta dificuldades na interação familiar': 1.25,
            'D — Encontra-se em fase de atendimento terapêutico regular e apoio': 0.63
        }
    },

    'Q2': {
        'pergunta': (
            '2) Como a equipe de Psicologia caracteriza o momento '
            'do estudante no seu desenvolvimento emocional?'
        ),
        'opcoes': {
            'A — Demonstra autonomia e adequação': 2.50,
            'B — Demonstra controle emocional adequado em geral': 1.88,
            'C — Demonstra alterações emocionais incompatíveis com a sua faixa etária': 1.25,
            'D — Encontra-se em fase de atendimento terapêutico regular e apoio': 0.63
        }
    },

    'Q3': {
        'pergunta': (
            '3) Como a equipe de Psicologia caracteriza '
            'o comportamento do estudante?'
        ),
        'opcoes': {
            'A — Interage de forma funcional': 2.50,
            'B — Interage em geral de forma adequada': 1.88,
            'C — Apresenta interações disfuncionais': 1.25,
            'D — Encontra-se em fase de atendimento terapêutico regular e apoio': 0.63
        }
    },

    'Q4': {
        'pergunta': (
            '4) Como a equipe de Psicologia caracteriza '
            'as interações sociais do estudante?'
        ),
        'opcoes': {
            'A — Demonstra interações sociais funcionais': 2.50,
            'B — Demonstra em geral adequação nas interações': 1.88,
            'C — Apresenta perfil excessivamente introspectivo': 1.25,
            'D — Encontra-se em fase de atendimento terapêutico regular e apoio': 0.63
        }
    }
}


# =========================================================
# IPP — Indicador de Aspectos Psicopedagógicos
# =========================================================

PERGUNTAS_IPP = {

    'Q1': {
        'pergunta': (
            '1) Como o avaliador descreveria o desempenho '
            'cognitivo do estudante?'
        ),
        'opcoes': {
            'Demonstra desempenho cognitivo acima do esperado.': 2.500,
            'Demonstra desempenho cognitivo adequado.': 1.875,
            'Demonstra déficit em algum aspecto de seu desempenho cognitivo.': 1.250,
            'Encontra-se em fase de atendimento e apoio.': 0.625
        }
    },

    'Q2': {
        'pergunta': (
            '2) Como o avaliador descreveria o estado '
            'emocional do estudante?'
        ),
        'opcoes': {
            'Demonstra autonomia e adequação': 2.500,
            'Demonstra adequação em geral': 1.875,
            'Demonstra carências emocionais incompatíveis com a sua faixa etária': 1.250,
            'Encontra-se em fase de atendimento e apoio': 0.625
        }
    },

    'Q3': {
        'pergunta': (
            '3) Como o avaliador descreveria o '
            'comportamento do estudante?'
        ),
        'opcoes': {
            'Interage de forma positiva': 2.500,
            'Interage em geral de forma adequada': 1.875,
            'Apresenta algumas interações inadequadas': 1.250,
            'Encontra-se em fase de atendimento e apoio': 0.625
        }
    },

    'Q4': {
        'pergunta': (
            '4) Como o avaliador descreveria as '
            'interações sociais do estudante?'
        ),
        'opcoes': {
            'Demonstra interações sociais positivas': 2.500,
            'Demonstra em geral adequação nas interações sociais': 1.875,
            'Apresenta perfil excessivamente introspectivo': 1.250,
            'Encontra-se em fase de atendimento e apoio': 0.625
        }
    }
}


RECOMENDACOES_IPP = [
    (
        'O estudante deveria ser promovido de Fase '
        'e indicado para Bolsa de Estudos.'
    ),
    (
        'O estudante deveria ser mantido na Fase atual '
        'e indicado para Bolsa de Estudos.'
    ),
    'O estudante deveria ser promovido de Fase.',
    'O estudante deveria ser mantido na Fase atual.',
    'O estudante deveria ser alocado em uma Fase anterior.'
]


# =========================================================
# IPV — Indicador de Ponto de Virada
# =========================================================

PERGUNTAS_IPV = {

    'Q1': {
        'peso': 3,
        'pergunta': (
            '1) Como o avaliador descreveria a integração do estudante à Associação, '
            'no tocante à sua dinâmica de aprendizado e sua contribuição para '
            'o aprendizado dos colegas?'
        ),
        'opcoes': {
            (
                'É estudioso e troca os conhecimentos que adquire com os colegas, '
                'é atencioso com o aprendizado deles.'
            ): 2.00,

            (
                'É dedicado a aprender. Quando lhe é solicitado compartilha '
                'e ajuda os colegas.'
            ): 1.50,

            (
                'Se dedica a aprender, mas é indiferente aos colegas, '
                'com pouco envolvimento.'
            ): 1.00,

            (
                'Tem dificuldades em se comprometer com o aprendizado, '
                'ou dispersa a atenção dos colegas.'
            ): 0.50
        }
    },

    'Q2': {
        'peso': 2,
        'pergunta': (
            '2) Como o avaliador descreveria a integração do estudante à Associação, '
            'sobre seu interesse pelas rotinas e a conservação dos ambientes '
            'e materiais compartilhados?'
        ),
        'opcoes': {
            (
                'Se interessa pela Associação e pela organização da sua rotina, '
                'se envolve e colabora com a conservação e o cuidado dos '
                'ambientes compartilhados.'
            ): 1.33,

            (
                'Colabora, sempre que solicitado, nas tarefas de conservação, '
                'cuidado e organização dos ambientes.'
            ): 1.00,

            (
                'Colabora, mas sem entusiasmo, nas tarefas de conservação, '
                'cuidado e organização dos ambientes.'
            ): 0.67,

            (
                'Evita, sempre que pode, as tarefas de conservação, '
                'cuidado e organização dos ambientes.'
            ): 0.33
        }
    },

    'Q3': {
        'peso': 3,
        'pergunta': (
            '3) Como o avaliador descreveria a integração do estudante à Associação, '
            'no tocante ao seu interesse pelas oportunidades oferecidas?'
        ),
        'opcoes': {
            (
                'Tem interesse em todas as oportunidades oferecidas pela Associação. '
                'É curioso sobre os processos, dedicado nos estudos e participa '
                'das oportunidades, cursos, treinamentos e atividades extras.'
            ): 2.00,

            (
                'Tem interesse nas oportunidades oferecidas pela Associação, '
                'mas nem sempre expressa isso por meio da dedicação aos estudos '
                'e participação nas atividades.'
            ): 1.50,

            (
                'Tem interesse nas oportunidades oferecidas pela Associação, '
                'mas assume uma atitude passiva em relação a elas.'
            ): 1.00,

            'É indiferente às oportunidades oferecidas pela Associação.': 0.50
        }
    },

    'Q4': {
        'peso': 1,
        'pergunta': (
            '4) Como o avaliador descreveria o desenvolvimento emocional do estudante, '
            'no tocante à capacidade de manter uma postura positiva?'
        ),
        'opcoes': {
            (
                'O estudante tem uma postura positiva, é confiante em si mesmo '
                'e lida bem com suas emoções.'
            ): 0.67,

            (
                'O estudante tem uma postura positiva, mas passa por momentos '
                'de insegurança quanto ao seu potencial.'
            ): 0.50,

            (
                'O estudante tem dificuldades em manter uma postura positiva '
                'e demonstra pouca confiança em si mesmo.'
            ): 0.33,

            (
                'O estudante não consegue assumir uma postura positiva '
                'e apresenta muitas dificuldades para lidar com suas emoções.'
            ): 0.17
        }
    },

    'Q5': {
        'peso': 2,
        'pergunta': (
            '5) Como o avaliador descreveria o desenvolvimento emocional do estudante, '
            'quanto à sua curiosidade e interesse em aprender?'
        ),
        'opcoes': {
            (
                'O estudante é curioso, determinado, interessado e se sente '
                'desafiado positivamente pelo processo de aprendizagem.'
            ): 1.33,

            (
                'O estudante é interessado, mas se contenta com os conteúdos '
                'e atividades que lhe são apresentados.'
            ): 1.00,

            (
                'O estudante é indiferente ao conhecimento, apresentando '
                'dificuldades na realização de algumas atividades.'
            ): 0.67,

            (
                'O estudante não demonstra interesse pelo conhecimento '
                'e tem muita dificuldade em realizar as atividades propostas.'
            ): 0.33
        }
    },

    'Q6': {
        'peso': 1,
        'pergunta': (
            '6) Como o avaliador descreveria o desenvolvimento emocional do estudante, '
            'quanto ao apoio familiar que recebe?'
        ),
        'opcoes': {
            (
                'O estudante demonstra ter apoio familiar, com responsáveis '
                'presentes e interessados no seu desenvolvimento.'
            ): 0.67,

            (
                'O estudante demonstra ter apoio familiar e recebe acompanhamento '
                'na realização das atividades.'
            ): 0.50,

            (
                'O estudante demonstra receber pouco apoio familiar e seus '
                'responsáveis não acompanham de perto seu desenvolvimento.'
            ): 0.33,

            (
                'O estudante demonstra não receber apoio familiar efetivo '
                'no desenvolvimento da sua educação.'
            ): 0.17
        }
    },

    'Q7': {
        'peso': 1,
        'pergunta': (
            '7) Como o avaliador descreveria o potencial acadêmico do estudante, '
            'no tocante à interpretação e produção de textos?'
        ),
        'opcoes': {
            (
                'Demonstra bom domínio da leitura, interpreta adequadamente '
                'os textos e utiliza isso na produção escrita.'
            ): 0.67,

            (
                'Consegue ler adequadamente e demonstra bom entendimento '
                'do texto, mas ainda não expressa isso plenamente na escrita.'
            ): 0.50,

            (
                'Consegue ler, mas apresenta dificuldades de interpretação '
                'que prejudicam sua produção escrita.'
            ): 0.33,

            'Tem dificuldades de leitura, interpretação e redação.': 0.17
        }
    },

    'Q8': {
        'peso': 1,
        'pergunta': (
            '8) Como o avaliador descreveria o potencial acadêmico do estudante, '
            'quanto ao interesse pelas atividades de leitura?'
        ),
        'opcoes': {
            (
                'Demonstra ser um leitor engajado, especialmente '
                'na leitura de livros.'
            ): 0.67,

            (
                'Demonstra ser um leitor engajado em outros gêneros '
                'e expressa sua curiosidade por meio da leitura.'
            ): 0.50,

            'Participa das atividades de leitura, mas sem entusiasmo.': 0.33,

            'Evita, sempre que pode, as tarefas de leitura.': 0.17
        }
    },

    'Q9': {
        'peso': 1,
        'pergunta': (
            '9) Como o avaliador descreveria o potencial acadêmico do estudante, '
            'no tocante ao seu raciocínio lógico?'
        ),
        'opcoes': {
            (
                'Demonstra bom raciocínio lógico, compreende as questões propostas, '
                'estabelece relações e identifica padrões.'
            ): 0.67,

            (
                'Tem bom raciocínio lógico, mas apresenta alguma dificuldade '
                'de compreensão e requer pouca ajuda.'
            ): 0.50,

            (
                'Tem bom raciocínio lógico, mas precisa de ajuda na interpretação '
                'e resolução das questões.'
            ): 0.33,

            (
                'Tem dificuldades em atividades baseadas no raciocínio lógico '
                'e necessita de apoio para superar as defasagens.'
            ): 0.17
        }
    }
}


# =========================================================
# PESOS DO IPV — Tabela 59
# =========================================================

PESOS_IPV = {
    'Q1': 3,
    'Q2': 2,
    'Q3': 3,
    'Q4': 1,
    'Q5': 2,
    'Q6': 1,
    'Q7': 1,
    'Q8': 1,
    'Q9': 1
}