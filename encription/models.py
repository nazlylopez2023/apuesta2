from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency
)
import random, string, json, time

doc = """
a.k.a. Keynesian beauty contest.

Players all guess a number; whoever guesses closest to
2/3 of the average wins.

See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'encription'

    letters_per_word = 3
    fee = 350

    use_timeout = True
    seconds_per_period = 180
    seconds_trial=30

    LAB_MATRIX = {
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

class Subsession(BaseSubsession):
    dictionary = models.StringField()

    def creating_session(self):
        # Create dictionary
        letters = list(string.ascii_uppercase)
        random.shuffle(letters)
        numbers = []
        N = list(range(100, 1000))
        for i in range(27):
            choice = random.choice(N)
            N.remove(choice)
            numbers.append(choice)
        d = [letters, numbers]
        dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
        self.dictionary = json.dumps(dictionary)



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    performance = models.IntegerField(initial=0, blank=True)
    mistakes = models.IntegerField(initial=0, blank=True)
    payout = models.IntegerField(initial=0)

    def calculate_payoff(self):

        if self.performance > 0:
            self.payout = Constants.fee
        else:
            self.payout = 0

    lab_id = models.IntegerField(initial=0)

    name = models.StringField(label="Nombres y apellidos:", blank=False)
    acepto = models.BooleanField(label="Acepto participar",
                                 choices=[
                                     [True, "Sí"],
                                     [False, "No"]])

    def set_id(self):
        participant_label = self.participant.label
        self.lab_id = Constants.LAB_MATRIX.get(participant_label, 0)

