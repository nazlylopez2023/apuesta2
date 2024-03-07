from ._builtin import Page, WaitPage
from .models import Constants


class Inst_grales(Page):
    form_model = "player"

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

class Instrucciones(Page):
    form_model = "player"


class Trial(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_trial

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                'task_list': task_list,
                'task_width': task_width}


class Paso(Page):
    pass


class Task(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                'task_list': task_list,
                'task_width': task_width}

    def before_next_page(self):
        self.player.calculate_payoff()


class Results(Page):
    def vars_for_template(self):
        player = self.player
        return {'payout': player.payout}


class Out(Page):
    def vars_for_template(self):
        self.player.set_id()
        return {
            'lab_id': self.player.lab_id,
        }

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
                 Instrucciones,
                 Trial,
                 Paso,
                 Task,
                 Results,]
