from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_grupo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 3
    n_rounds_payoff = 4

    #Hojas de Vida = lista con diccionarios dentro
    ## Listas -> estructuras ordenadas, separados por comas
    ## Diccionarios -> estrictura no ordenada
    hvs = [
    # hoja de vida de la ronda # 0
        {
            'A':{
            'num_doc': '1A' ,
            'tipo_doc': 'CC',
            'gen': 'Masculino',
            'age': '28',
            'las_exp': ['Domiciliario - 1año',
                        'Mesero - 3 meses',
                        'Domiciliario - 6 meses'
                        ],
            'lvl_edu': 'Secundaria',
            'type': 'A',
        },

            'B':{
            'num_doc': '1B',
            'tipo_doc': 'PEP',
            'gen': 'Masculino',
            'age': '30',
            'las_exp': ['Mesero - 1año',
                        'Domiciliario - 3 meses',
                        'Mesero - 6 meses',
                        ],

            'lvl_edu': 'Secundaria',
            'type': 'B',

            },
        'text': "De estos candidatos ¿A quién recomendaría para un puesto de <b>mesero</b>?",
        'round': '1'
        },

    # hoja de vida # 1
        {
            'A': {
                'num_doc': '2A',
                'tipo_doc': 'CC',
                'gen': 'Masculino',
                'age': '28',
                'las_exp': ['Domiciliario - 1año',
                            'Mesero - 3 meses',
                            'Domiciliario - 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'num_doc': '2B',
                'tipo_doc': 'PEP',
                'gen': 'Masculino',
                'age': '30',
                'las_exp': ['Mesero - 1año',
                            'Domiciliario - 3 meses',
                            'Mesero - 6 meses',
                            ],

                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "De estos candidatos ¿A quién recomendaría para un puesta de mesero?",
            'round': '2'
        },
    # hoja de vida # 2
        {
            'A': {
                'num_doc': '3A',
                'tipo_doc': 'CC',
                'gen': 'Masculino',
                'age': '28',
                'las_exp': ['Domiciliario - 1año',
                            'Mesero - 3 meses',
                            'Domiciliario - 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'num_doc': '3B',
                'tipo_doc': 'PEP',
                'gen': 'Masculino',
                'age': '30',
                'las_exp': ['Mesero - 1año',
                            'Domiciliario - 3 meses',
                            'Mesero - 6 meses',
                            ],

                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "De estos candidatos ¿A quién recomendaría para un puesto de <b>mesero</b>?",
            'round': '3'
        },
    # hoja de vida # 3
    # hoja de vida # 4
    # hoja de vida # 5
    # hoja de vida # 6
    # hoja de vida # 7
    ]



class Subsession(BaseSubsession):
    winner_round_1 = models.StringField()
    winner_round_2 = models.StringField()
    winner_round_3 = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Introducción

    selected_round_1 = models.StringField(initial = "-")
    tokens_round_1 = models.IntegerField(initial = -1)
    selected_round_2 = models.StringField(initial = "-")
    tokens_round_2 = models.IntegerField(initial = -1)
    selected_round_3 = models.StringField(initial = "-")
    tokens_round_3 = models.IntegerField(initial = -1)
    selected_round_4 = models.StringField(initial = "-")
    tokens_round_4 = models.IntegerField(initial = -1)
    selected_round_5 = models.StringField(initial = "-")
    tokens_round_5 = models.IntegerField(initial = -1)
    selected_round_6 = models.StringField(initial = "-")
    tokens_round_6 = models.IntegerField(initial = -1)
    selected_round_7 = models.StringField(initial = "-")
    tokens_round_7 = models.IntegerField(initial = -1)
    selected_round_8 = models.StringField(initial = "-")
    tokens_round_8= models.IntegerField(initial = -1)

# Payoffs
    ## depende de la cantidad de rondas a pagar
    ### ronda 1 a pagar
    round_a_to_payoff_selected = models.StringField()
    round_a_to_payoff_tokens = models.IntegerField()
    ### ronda 2 a pagar
    round_b_to_payoff_selected = models.StringField()
    round_b_to_payoff_tokens = models.IntegerField()
    ### ronda 3 a pagar
    round_c_to_payoff_selected = models.StringField()
    round_c_to_payoff_tokens = models.IntegerField()
    ### ronda 4 a pagar
    round_d_to_payoff_selected = models.StringField()
    round_d_to_payoff_tokens = models.IntegerField()

    ## Cálculo de los tokens totales
    tokens_total = models.IntegerField()
