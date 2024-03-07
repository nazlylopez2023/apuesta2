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

    #Hojas de Vida = lista con diccionarios dentro
    ## Listas -> estructuras ordenadas, separados por comas
    ## Diccionarios -> estrictura no ordenada
    hvs = [
    # hoja de vida de la ronda # 0
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.151.947.578',
                'lug_nac': 'Cali (Valle del Cauca)',
                'age': '30',
                'las_exp': ['Conductor - Más de 12 meses',
                            'Preparador físico - Entre 3 y 6 meses',
                            'Enfermero de clínica - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '20.610.722',
                'lug_nac': 'Maracaibo (Venezuela)',
                'age': '32',
                'las_exp': ['Enfermero independiente - Más de 12 meses',
                            'Enfermero de clínica - Entre 7 y 9 meses',
                            'Enfermero de Clínica - Entre 7 y 9 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>cuidador de adulto mayor</b>?",
            'round': '1'
        },

    # hoja de vida # 1
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.026.290.858',
                'lug_nac': 'Bogotá D.C.',
                'age': '28',
                'las_exp': ['Mensajero - 3 meses',
                            'Auxiliar de bodega - Más de 12 meses',
                            'Supernumerario de restaurante - 3 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.022.413.634',
                'lug_nac': 'Bogotá D.C.',
                'age': '27',
                'las_exp': ['Domiciliario - Entre 7 y 9 meses',
                            'Auxiliar de Bodega - Más de 12 meses',
                            'Camillero de clínica - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>asistente de inventario de bodega</b>?",
            'round': '2'
        },
    # hoja de vida # 2
        {
            'A': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '14.931.329',
                'lug_nac': 'Venezuela',
                'age': '35',
                'las_exp': ['Supernumerario de restaurante- Entre 10 y 12 meses',
                            'Depositario de bodega - Más de 12 meses',
                            'Domiciliario - Más de 12 meses'
                            ],
                'lvl_edu': 'Primaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.015.452.938',
                'lug_nac': 'Bogotá D.C.',
                'age': '28',
                'las_exp': ['Domiciliario de restaurante - Entre 7 y 9 meses',
                            'Auxiliar de bodega - Entre 3 y 6 meses',
                            'Pintor de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Primaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>asistente de inventario de bodega</b>?",
            'round': '3'
        },
    # hoja de vida # 3

        {
            'A': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '749.965',
                'lug_nac': 'Valencia (Venezuela)',
                'age': '32',
                'las_exp': ['Auxiliar de tienda de cadena - 3 meses',
                            'Mesero - Más de 12 meses',
                            'Cajero de Movistar Arena - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '22.283.194',
                'lug_nac': 'Venezuela',
                'age': '28',
                'las_exp': ['Cajero de supermercado - Más de 12 meses',
                            'Domiciliario - Más de 12 meses',
                            'Domiciliario - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>auxiliar de minimercado</b>?",
            'round': '4'
        },
    # hoja de vida # 4

        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.143.362.956',
                'lug_nac': 'El Bagre (Antioquia)',
                'age': '30',
                'las_exp': ['Operador de medios de seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses',
                            'Pintor de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de ciudadanía',
                'num_doc': '1.022.965.450',
                'lug_nac': 'Bogotá D.C.',
                'age': '33',
                'las_exp': ['Vigilante seguridad privada - Más de 12 meses',
                            'Supervisor seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>maestro de obra</b>?",
            'round': '5'
        },
    # hoja de vida # 5

        {
            'A': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '1.401.613',
                'lug_nac': 'Venezuela',
                'age': '28',
                'las_exp': ['Domiciliario - Más de 12 meses',
                            'Domiciliario aplicación - Más de 12 meses',
                            'Domiciliario aplicación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '824.120',
                'lug_nac': 'Venezuela',
                'age': '30',
                'las_exp': ['Domiciliario aplicación - Más de 12 meses',
                            'Domiciiario restaurante - Más de 12 meses',
                            'Domiciliario aplicación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor despachos de domicilios por aplicación</b>?",
            'round': '6'
        },
    # hoja de vida # 6
        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '21.030.623',
                'lug_nac': 'Venezuela',
                'age': '33',
                'las_exp': ['Músico de agrupación - Más de 12 meses',
                            'Domiciliario de restaurante - Entre 3 y 6 meses',
                            'Músico de agrupación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de ciudadanía',
                'num_doc': '1.023.970.577',
                'lug_nac': 'Bogotá D.C.',
                'age': '24',
                'las_exp': ['Profesor de música independiente - Más de 12 meses',
                            'Profesor de música en instituto - Más de 12 meses',
                            'Trombonista de agrupación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>músico de agrupación para eventos</b>?",
            'round': '7'
        },
    # hoja de vida # 7

        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.022.400.837',
                'lug_nac': 'Bogotá D.C.',
                'age': '28',
                'las_exp': ['Agente de operaciones terrestres - Más de 12 meses',
                            'Vendedor independiente - 3 meses',
                            'Operario de producción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '1.249.585',
                'lug_nac': 'Venezuela',
                'age': '33',
                'las_exp': ['Administrador negocio familiar - Más de 12 meses',
                            'Encargado de tienda de farmacia - 3 meses',
                            'Asistente administrativo - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor de tienda</b>?",
            'round': '8'
        },
    ]



class Subsession(BaseSubsession):
    winner_round_1 = models.StringField()
    winner_round_2 = models.StringField()
    winner_round_3 = models.StringField()
    winner_round_4 = models.StringField()
    winner_round_5 = models.StringField()
    winner_round_6 = models.StringField()
    winner_round_7 = models.StringField()
    winner_round_8 = models.StringField()


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
