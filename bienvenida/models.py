from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'bienvenida'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="Nombres y apellidos:", blank=False)
    acepto = models.BooleanField(label="Acepto participar",
                                 choices=[
                                     [True, "Sí"],
                                     [False, "No"]])

