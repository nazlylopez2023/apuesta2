from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_grupo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 8
    n_rounds_payoff = 4
    fee = 350

    #Hojas de Vida = lista con diccionarios dentro
    ## Listas -> estructuras ordenadas, separados por comas
    ## Diccionarios -> estrictura no ordenada
    hvs = [
    # hoja de vida de la ronda # 0
        {
            'A':{
            'tipo_doc': 'Cédula de Extranjería' ,
            'num_doc': '21.479.372',
            'lug_nac': 'Maracay (Venezuela)',
            'age': '37',
            'las_exp': ['Orientador trámites de tránsito - Entre 3 y 6 meses',
                        'Lavador de carro - Entre 3 y 6 meses',
                        'Lavador de carro - Entre 10 y 12 meses'
                        ],
            'lvl_edu': 'Secundaria',
            'type': 'A',
        },

            'B':{
            'tipo_doc': 'Cédula de Ciudadanía' ,
            'num_doc': '1.023.874.978',
            'lug_nac': 'Bogotá D.C.',
            'age': '29',
            'las_exp': ['Operario de aseo - Más de 12 meses',
                        'Ayudante de pastelería - Entre 3 y 6 meses',
                        'Operario de aseo - Entre 3 y 6 meses'
                        ],
            'lvl_edu': 'Secundaria',
            'type': 'B',

            },
        'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>asistente de supervisor de aseo</b>?",
        'round': '1'
        },

    # hoja de vida # 1
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.016.060.489',
                'lug_nac': 'Puerto Leguízamo (Putumayo)',
                'age': '29',
                'las_exp': ['Mesero - Entre  7 y 9 meses',
                            'Domiciliario - Entre 3 y 6 meses',
                            'Mesero - Entre 10 y 12 meses meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '26.631.888',
                'lug_nac': 'Barquisimento (Venezuela)',
                'age': '26',
                'las_exp': ['Mesero - Entre 7 y 9 meses',
                            'Mesero - Más de 12 meses',
                            'Vendedor negocio familiar - Entre 10 y 12 meses',
                            ],

                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesta de <b>despachador de domicilios en restaurante</b>?",
            'round': '2'
        },
    # hoja de vida # 2
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.010.203.108',
                'lug_nac': 'Bogotá D.C.',
                'age': '31',
                'las_exp': ['Asistente administrativo - Más de 12 meses',
                            'Gerente comercial - Más de 12 meses',
                            'Desarrollador de software - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '80.772.995',
                'lug_nac': 'Bogotá D.C.',
                'age': '38',
                'las_exp': ['Auxiliar de Bodega - Más de 12 meses',
                            'Auxiliar postal - Más de 12 meses',
                            'Codificador se sistemas - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>secretario multitasking</b>?",
            'round': '3'
        },
    # hoja de vida # 3
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.065.613.805',
                'lug_nac': 'Valledupar (Cesar)',
                'age': '33',
                'las_exp': ['Vendedor restaurante de cadena - Más de 12 meses ',
                            'Vigilante - Entre 7 y 9 meses',
                            'Auxiliar restaurante de cadena - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '749.965',
                'lug_nac': 'Valencia (Venezuela)',
                'age': '32',
                'las_exp': ['Auxiliar tienda de cadena - Entre 3 y 6 meses',
                            'Mesero - Más de 12 meses',
                            'Cajero de Movistar Arena - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor de tienda</b>?",
            'round': '4'
        },

    # hoja de vida # 4
        {
            'A': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '4.668.040',
                'lug_nac': 'San Cristobal (Venezuela)',
                'age': '33',
                'las_exp': ['Vendedor de fruver - Entre 7 y 9 meses',
                            'Vendedor de tienda - Entre 3 y 6 meses',
                            'Vendedor de fruver - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '1.252.250',
                'lug_nac': 'Villa de Cura (Venezuela)',
                'age': '26',
                'las_exp': ['Vendedor independiente - Más de 12 meses',
                            'Vendedor de fruver - Entre 7 y 9 meses',
                            'Vendedor de fruver - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor de mini mercado</b>?",
            'round': '5'
        },
    # hoja de vida # 5
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.071.579.575',
                'lug_nac': 'Carrapí (Cundinamarca)',
                'age': '33',
                'las_exp': ['Operario de corrugados - Más de 12 meses',
                            'Operario máquina de inyección de suelas - Más de 12 meses',
                            'Operario de perforación - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '5.112.719',
                'lug_nac': 'San Felipe (Venezuela)',
                'age': '33',
                'las_exp': ['Operario de producción - Más de 12 meses',
                            'Supervisor de producción - Más de 12 meses',
                            'Ayudante en plaza de mercados - Entre 7 y 9 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor de operaciones</b>?",
            'round': '6'
        },
    # hoja de vida # 6
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.233.503.273',
                'lug_nac': 'Bogotá D.C.',
                'age': '24',
                'las_exp': ['Mensajero - Entre 7 y 8 meses',
                            'Vendedor - Entre 3 y 6 meses',
                            'Auxiliar logístico - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.022.428.304',
                'lug_nac': 'Bogotá D.C.',
                'age': '26',
                'las_exp': ['Mensajero - Más de 12 meses',
                            'Vendedor - Más de 12 meses',
                            'Asistente de ventas - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>asesor de ventas</b>?",
            'round': '7'
        },
    # hoja de vida # 7

        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '25.242.901',
                'lug_nac': 'Monagas (Venezuela)',
                'age': '27',
                'las_exp': ['Domiciliario - Entre 10 y 12 meses',
                            'Encargado de supermercado - Más de 12 meses',
                            'Vendedor - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '22.283.194',
                'lug_nac': 'Caracas (Venezuela)',
                'age': '28',
                'las_exp': ['Cajero de supermercado - Más de 12 meses',
                            'Domiciliario - Entre 7 y 9 meses',
                            'Domiciliario - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor despachos de domicilios</b>?",
            'round': '8'
        },
    ]

    



class Subsession(BaseSubsession):
    pass


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

    winner_round_1 = models.StringField()
    winner_round_2 = models.StringField()
    winner_round_3 = models.StringField()
    winner_round_4 = models.StringField()
    winner_round_5 = models.StringField()
    winner_round_6 = models.StringField()
    winner_round_7 = models.StringField()
    winner_round_8 = models.StringField()

# tokens que se acumulan entre rondas más el fee. Si la suma es <350 el participante sale
    tokens_acum = models.IntegerField()
# tokens que traje de la primera etapa
    total_tokens_ind = models.IntegerField()
# tokens que me voy a llevar a la tercera etapa
    tokens_rondas = models.IntegerField()
