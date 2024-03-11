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
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

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
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

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
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_4(Page):
    n_round=3
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_5(Page):
    n_round=4
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }
class Ronda_6(Page):
    n_round=5
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }
class Ronda_7(Page):
    n_round=6
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_8(Page):
    n_round=7
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
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
        n_rounds_payoff = 4
        lst_rounds = list(range(1, C.n_rounds+1)) ## Ya aparece 1,2,3 no 0,1,2
        print("lista desordenada: ", lst_rounds)
        random.shuffle(lst_rounds)
        lst_rounds = lst_rounds[:n_rounds_payoff]
        print("lista de rondas escogidas", lst_rounds)
        winner_round_1 = self.participant.vars.get('winner_round_1', 0)
        winner_round_2 = self.participant.vars.get('winner_round_2', 0)
        winner_round_3 = self.participant.vars.get('winner_round_3', 0)
        winner_round_4 = self.participant.vars.get('winner_round_4', 0)
        winner_round_5 = self.participant.vars.get('winner_round_5', 0)
        winner_round_6 = self.participant.vars.get('winner_round_6', 0)
        winner_round_7 = self.participant.vars.get('winner_round_7', 0)
        winner_round_8 = self.participant.vars.get('winner_round_8', 0)
        tokens_total_ind = self.participant.vars.get('tokens_total_ind', 0)



##rondas para pagar serían a, b, c y d
        ##Diccionario de ganadores        Acá llamo el ganador que defino en models.
        winners = {
            1: {'winner': winner_round_1, 'my_choose': self.player.selected_round_1,
                'tokens': self.player.tokens_round_1},
            2: {'winner': winner_round_2, 'my_choose': self.player.selected_round_2,
                'tokens': self.player.tokens_round_2},
            3: {'winner': winner_round_3, 'my_choose': self.player.selected_round_3,
                'tokens': self.player.tokens_round_3},
            4: {'winner': winner_round_4, 'my_choose': self.player.selected_round_4,
                'tokens': self.player.tokens_round_4},
            5: {'winner': winner_round_5, 'my_choose': self.player.selected_round_5,
                'tokens': self.player.tokens_round_5},
            6: {'winner': winner_round_6, 'my_choose': self.player.selected_round_6,
                'tokens': self.player.tokens_round_6},
            7: {'winner': winner_round_7, 'my_choose': self.player.selected_round_7,
                'tokens': self.player.tokens_round_7},
            8: {'winner': winner_round_8, 'my_choose': self.player.selected_round_8,
                'tokens': self.player.tokens_round_8},
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

        ## guardar el número de la segunda ronda a pagar -> c
        self.player.round_c_to_payoff_selected = str(lst_rounds[2])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[2]]['winner'] == winners[lst_rounds[2]]['my_choose']):
            self.player.round_c_to_payoff_tokens = winners[lst_rounds[2]]['tokens'] * 1
        else:
            self.player.round_c_to_payoff_tokens = winners[lst_rounds[2]]['tokens'] * -1

        ## guardar el número de la segunda ronda a pagar -> b
        self.player.round_d_to_payoff_selected = str(lst_rounds[1])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[3]]['winner'] == winners[lst_rounds[3]]['my_choose']):
            self.player.round_d_to_payoff_tokens = winners[lst_rounds[3]]['tokens'] * 1
        else:
            self.player.round_d_to_payoff_tokens = winners[lst_rounds[3]]['tokens'] * -1

## Total de tokens por jugador

        self.player.tokens_total = self.player.round_a_to_payoff_tokens + self.player.round_b_to_payoff_tokens + self.player.round_c_to_payoff_tokens + self.player.round_d_to_payoff_tokens
        self.player.tokens_acum =  tokens_total_ind + self.player.tokens_total + C.fee
        self.player.tokens_rondas = tokens_total_ind + self.player.tokens_total
        return {
            'rounds_to_payoff': lst_rounds, ## las rondas que vamos a pagar
            'winners': winners,
            'total_tokens': self.player.tokens_total,
            'tokens_acum': self.player.tokens_acum,
            'tokens_total_ind': tokens_total_ind,
            'tokens_rondas': self.player.tokens_rondas
        }

    def before_next_page(self):
        self.participant.vars['tokens_total_grupo'] = self.player.tokens_total
        self.participant.vars['tokens_rondas'] = self.player.tokens_rondas



        


rondas = [Ronda_1, Ronda_2, Ronda_3, Ronda_4, Ronda_5, Ronda_6, Ronda_7, Ronda_8 ] #, Ronda_2, Ronda_3, Ronda_4, Ronda_5, Ronda_6, Ronda_7, Ronda_8
random.shuffle(rondas)



page_sequence = [Instrucciones] + rondas + [Pagos]
print("order pages", page_sequence)
