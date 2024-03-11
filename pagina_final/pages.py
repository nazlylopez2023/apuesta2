from otree.api import *
from .models import *


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class total(Page):
    form_model = 'player'
    form_fields = ['tokens_totales']

    def vars_for_template(self):
        tokens_encription = 20
        tokens_total_ind = self.participant.vars.get('tokens_total_ind', 0)
        tokens_total_grupo = self.participant.vars.get('tokens_total_grupo', 0)
        tokens_total_firma = self.participant.vars.get('tokens_total_firma', 0)

        self.player.tokens_totales = 20 + tokens_total_ind + tokens_total_grupo + tokens_total_firma
        return {'tokens_encription': tokens_encription,
                'tokens_total_ind': tokens_total_ind,
                'tokens_total_grupo': tokens_total_grupo,
                'tokens_total_firma': tokens_total_firma,
                'tokens_totales': self.player.tokens_totales,
                'pago_monetario' : self.player.tokens_totales*1000

                }



page_sequence = [total]
