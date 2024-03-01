from otree.api import *
from .models import *


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class total(Page):

    def vars_for_template(self):
        tokens_total_ind = self.participant.vars.get('tokens_total_ind', 0)
        tokens_total_grupo = self.participant.vars.get('tokens_total_grupo', 0)
        tokens_total_firma = self.participant.vars.get('tokens_total_firma', 0)
        tokens_totales = tokens_total_ind + tokens_total_grupo + tokens_total_firma
        return {'tokens_total_ind': tokens_total_ind,
                'tokens_total_grupo': tokens_total_grupo,
                'tokens_total_firma': tokens_total_firma,
                'tokens_totales': tokens_totales,
                }
        



page_sequence = [total]
