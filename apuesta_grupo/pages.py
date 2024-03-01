from otree.api import *
from .models import *
import random
class MyPage(Page):
    pass

class Espera(WaitPage):
    print("Espere mientras los demás jugadores terminen")

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


class Instrucciones(Page):
    pass


class Ronda_1(Page):
    n_round=0
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        random.shuffle(lst_order) #aleatorizar entre A y B
        print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_2(Page):
    n_round=1
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        random.shuffle(lst_order) #aleatorizar entre A y B
        print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }


class Ronda_3(Page):
    n_round=2
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        random.shuffle(lst_order) #aleatorizar entre A y B
        print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Pagos(Page):
    def vars_for_template(self):
        #n_rounds_payoff = C.n_rounds_payoff
        n_rounds_payoff = 2
        lst_rounds = list(range(1, C.n_rounds+1)) ## Ya aparece 1,2,3 no 0,1,2
        print("lista desordenada: ", lst_rounds)
        random.shuffle(lst_rounds)
        lst_rounds = lst_rounds[:n_rounds_payoff]
        print("lista de rondas escogidas", lst_rounds)

        #Escoger el ganador de cada ronda
        ## Primero obtener todos los jugadores en la subsesión
        players_per_subse = self.subsession.get_players()
        print(players_per_subse)
        round_1 = []
        round_2 = []
        round_3 = []
        round_4 = []
        round_5 = []
        round_6 = []
        round_7 = []
        round_8 = []
        for p in players_per_subse:
            round_1.append(p.selected_round_1)
            round_2.append(p.selected_round_2)
            round_3.append(p.selected_round_3)
        #Escoger el más elegido de cada ronda
        ## Ronda_1
        if round_1.count('A') > round_1.count('B'):
            self.subsession.winner_round_1 = 'A'
        elif round_1.count('B') > round_1.count('A'):
            self.subsession.winner_round_1 = 'B'
        else:
            self.subsession.winner_round_1 = 'Empate'

        ## Ronda_2
        if round_2.count('A') > round_2.count('B'):
            self.subsession.winner_round_2 = 'A'
        elif round_2.count('B') > round_2.count('A'):
            self.subsession.winner_round_2 = 'B'
        else:
            self.subsession.winner_round_2 = 'Empate'

        ## Ronda_3
        if round_3.count('A') > round_3.count('B'):
            self.subsession.winner_round_3 = 'A'
        elif round_3.count('B') > round_3.count('A'):
            self.subsession.winner_round_3 = 'B'
        else:
            self.subsession.winner_round_3 = 'Empate'
##rondas para pagar serían a, b, c y d
        ##Diccionario de ganadores        Acá llamo el ganador que defino en models.
        winners = {
            1: {'winner': self.subsession.winner_round_1, 'my_choose': self.player.selected_round_1,
                'tokens': self.player.tokens_round_1},
            2: {'winner': self.subsession.winner_round_2, 'my_choose': self.player.selected_round_2,
                'tokens': self.player.tokens_round_2},
            3: {'winner': self.subsession.winner_round_3, 'my_choose': self.player.selected_round_3,
                'tokens': self.player.tokens_round_3},
        }

        ## rondas a pagar son 4 y serían a, b, c y d

        ## guardar el número de la primera ronda a pagar -> a
        self.player.round_a_to_payoff_selected = str(lst_rounds[0])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[0]]['winner'] == winners[lst_rounds[0]]['my_choose']):
            self.player.round_a_to_payoff_tokens = winners[lst_rounds[0]]['tokens'] * 1
        elif (winners[lst_rounds[0]]['winner'] == 'Empate'):
            self.player.round_a_to_payoff_tokens = 0
        else:
            self.player.round_a_to_payoff_tokens = winners[lst_rounds[0]]['tokens'] * -1

        ## guardar el número de la segunda ronda a pagar -> b
        self.player.round_b_to_payoff_selected = str(lst_rounds[1])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[1]]['winner'] == winners[lst_rounds[1]]['my_choose']):
            self.player.round_b_to_payoff_tokens = winners[lst_rounds[1]]['tokens'] * 1
        else:
            self.player.round_b_to_payoff_tokens = winners[lst_rounds[1]]['tokens'] * -1

    # Mientras defino c y d
        self.player.round_c_to_payoff_tokens = 0
        self.player.round_d_to_payoff_tokens = 0

## Total de tokens por jugador
        self.player.tokens_total = self.player.round_a_to_payoff_tokens + self.player.round_b_to_payoff_tokens + self.player.round_c_to_payoff_tokens + self.player.round_d_to_payoff_tokens
        return {
            'rounds_to_payoff': lst_rounds, ## las rondas que vamos a pagar
            'winners': winners,
            'total_tokens': self.player.tokens_total
        }

    def before_next_page(self):
        self.participant.vars['tokens_total_grupo'] = self.player.tokens_total


rondas = [Ronda_1, Ronda_2, Ronda_3]
random.shuffle(rondas)



page_sequence = [Instrucciones] + rondas + [Espera, Pagos]
print("order pages", page_sequence)
