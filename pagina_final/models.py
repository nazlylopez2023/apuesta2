from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
        NAME_IN_URL = 'pagina_final'
        PLAYERS_PER_GROUP = None
        NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    tokens_encription = models.IntegerField()
    tokens_total_ind = models.IntegerField()
    tokens_total_grupo = models.IntegerField()
    tokens_total_firma = models.IntegerField()
    tokens_totales = models.IntegerField()
    pago_monetario =  models.IntegerField()

