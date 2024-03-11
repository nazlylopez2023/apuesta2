from os import environ

SESSION_CONFIGS = [
    dict(
        name = 'Apuesta_ind',
        app_sequence = ['bienvenida','encription','apuesta_ind','apuesta_grupo','apuesta_firmas'],   #'encription','apuesta_ind','apuesta_grupo','apuesta_firmas','pagina_final'
        num_demo_participants = 3,
        display_name = 'Apuesta individual'
    ),
    #dict(
         #name='Apuesta_grupo',
         #app_sequence=['apuesta_grupo'],
         #num_demo_participants=3,
         #display_name = 'Apuesta grupo'
     #),

    #dict(
        #name = 'Apuesta_firmas',
        #app_sequence = ['apuesta_firmas'],
        #num_demo_participants = 3,
        #display_name = 'Apuesta creencias de las firmas',
    #),
    #dict(
        #name = 'pagina_final',
        #app_sequence = ['pagina_final'],
        #num_demo_participants = 3,
        #display_name = 'Pagos totales'
    #),
]

INSTALLED_APPS = ['bienvenida','encription','apuesta_ind','apuesta_grupo','apuesta_firmas']      #'encription','apuesta_ind','apuesta_grupo','apuesta_firmas','pagina_final'

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['total_tokens','payout','tokens_total_ind','tokens_acum','tokens_rondas','tokens_total_grupo','tokens_total_firma']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
USE_POINTS = True
POINTS_CUSTOM_NAME = 'Tokens'
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2242569844807'
