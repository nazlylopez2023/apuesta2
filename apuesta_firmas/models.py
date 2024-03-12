from otree.api import *
import random





doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_firmas'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 8
    n_rounds_payoff = 4
    fee = 350
    pag = ['Ronda_1_fir','Ronda_2_fir', 'Ronda_3_fir', 'Ronda_4_fir', 'Ronda_5_fir','Ronda_6_fir','Ronda_7_fir','Ronda_8_fir' ]
    num_rondas =len(pag)

    LAB = {
        'LAB1': 1,
        'LAB2': 2,
        'LAB3': 3,
        'LAB4': 4,
        'LAB5': 5,
        'LAB6': 6,
        'LAB7': 7,
        'LAB8': 8,
        'LAB9': 9,
        'LAB10': 10,
        'LAB11': 11,
        'LAB12': 12,
        'LAB13': 13,
        'LAB14': 14,
        'LAB15': 15,
        'LAB16': 16,
        'LAB17': 17,
        'LAB18': 18,
        'LAB19': 19,
        'LAB20': 20,
        'LAB21': 21,
        'LAB22': 22,
        'LAB23': 23,
        'LAB24': 24,
        'LAB25': 25,
        'LAB26': 26,
        'LAB27': 27,
        'LAB28': 28,
        'LAB29': 29,
    }

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
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>cuidador de adulto mayor</b>?",
            'round': '1'
        },

    # hoja de vida # 1
        {
            'A': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '14.931.329',
                'lug_nac': 'Maracay (Venezuela)',
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
            'round': '2'
        },
    # hoja de vida # 2
        {
            'A': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '1.401.613',
                'lug_nac': 'Maracay (Venezuela)',
                'age': '28',
                'las_exp': ['Domiciliario de restaurante - Entre 10 y 12 meses',
                            'Domiciliario aplicación - Entre 7 y 9 meses',
                            'Domiciliario independiente - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '824.120',
                'lug_nac': 'Barquisimento (Venezuela)',
                'age': '30',
                'las_exp': ['Domiciliario aplicación - Más de 12 meses',
                            'Mensajero motorizado - Entre 10 y 12 meses',
                            'Domiciliario aplicación - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor despacho de domicilios</b>?",
            'round': '3'
        },
    # hoja de vida # 3

        {
            'A': {

                'type': 'A',
                'tipo_doc': 'Cédula de ciudadanía',
                'num_doc': '1.022.965.450',
                'lug_nac': 'Bogotá D.C.',
                'age': '33',
                'las_exp': ['Vigilante seguridad privada - Más de 12 meses',
                            'Supervisor seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.143.362.956',
                'lug_nac': 'El Bagre (Antioquia)',
                'age': '30',
                'las_exp': ['Operador de medios de seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses',
                            'Pintor de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>maestro de obra</b>?",
            'round': '4'
        },
    # hoja de vida # 4

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
                'lug_nac': 'Zulia (Venezuela)',
                'age': '33',
                'las_exp': ['Administrador negocio familiar - Más de 12 meses',
                            'Encargado de tienda de farmacia - 3 meses',
                            'Asistente administrativo - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>supervisor de tienda</b>?",
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
                'num_doc': '80.746.909',
                'lug_nac': 'Bogotá D.C.',
                'age': '40',
                'las_exp': ['Jardinero de zonas verdes - Más de 12 meses ',
                            'Guarnecedor de calzado - Entre 7 y 9 meses',
                            'Bodeguero - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '700.4016',
                'lug_nac': 'Los Puertos (Venezuela)',
                'age': '35',
                'las_exp': ['Oficios Varios - Más de 12 meses',
                            'Maquinista - 3 meses',
                            'Trabajador fábrica de escritorios - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "Entre el Candidato A y el Candidato B ¿A quién recomendaría para un puesto de <b>Operario de máquina de empaquetado</b>?",
            'round': '7'
        },
    # hoja de vida # 7

        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '21.030.623',
                'lug_nac': 'San Antonio de Táchira (Venezuela)',
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
            'round': '8'
        },
    ]



class Subsession(BaseSubsession):
    pass
    #def creating_session(subsession):
        #import random
        #for p in subsession.get_players():
            #round_numbers = list(range(1, C.num_rondas + 1))
            #random.shuffle(round_numbers)
            #print(round_numbers)
            #p.participant.vars['rondas'] = dict(zip(C.pag, round_numbers))
            #print(p.participant.vars['rondas'])

            #for i in range(1, C.num_rondas + 1):
                #setattr(p, f'winner_{i}', '')




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_round_information(self):
        round_numbers = list(range(1, C.num_rondas + 1))
        random.shuffle(round_numbers)
        print(round_numbers)
        self.participant.vars['rondas'] = dict(zip(C.pag, round_numbers))
        print(self.participant.vars['rondas'])

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



    winner_1 = models.StringField()
    winner_2 = models.StringField()
    winner_3 = models.StringField()
    winner_4 = models.StringField()
    winner_5 = models.StringField()
    winner_6 = models.StringField()
    winner_7 = models.StringField()
    winner_8 = models.StringField()

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

 ## tokens acumulados menos el fee
    tokens_acum = models.IntegerField()

# tokens acumulados que me traje de la etapa 1 y 2
    tokens_rondas = models.IntegerField()

# tokens acumulados en todas las rondas
    tokens_finales = models.IntegerField()

# tokens que traje de la tarea de decodificación
    tokens_encription = models.IntegerField()

# tokens que traje de la prueba individual
    tokens_total_ind = models.IntegerField()

# tokens que traje de la predicción de grupo
    tokens_total_grupo = models.IntegerField()

# tokens en plata
    pago_monetario = models.CurrencyField()



