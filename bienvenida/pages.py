from otree.api import Page
from otree.models import player

from .models import C


class Inst_grales(Page):
    form_model = 'player'


class Consentimiento(Page):
    form_model = "player"
    form_fields = ['name', 'acepto']

    # def before_next_page(self):
    #     if self.player.acepto:
    #         # Redireccionar al participante a la siguiente página
    #         pass
    #     else:
    #         # Indicar al participante que ha elegido no participar
    #         pass


class NoAcepta(Page):
    player = 'models.Player'

    # Display only to participants who pass all three mandatory conditions

    def is_displayed(self):
        return self.player.acepto == False


class Out(Page):
    player = 'models.Player'

    def vars_for_template(self):
        self.player.set_id()
        return {
            'lab_id': self.player.lab_id,
        }

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [Inst_grales, Consentimiento, NoAcepta]
