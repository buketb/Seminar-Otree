from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class RoleAnnouncement(Page):
    pass

class ProposerSplit(Page):
    form_model = models.Group
    form_fields = ['proposed_share']
    
    timeout_seconds = 20
    timeout_submission = {'proposed_share': 0}

    def is_displayed(self):
        return self.player.role() == 'proposer'

    def before_next_page(self):
    #    if self.timeout_happened:
    #        self.player.proposed_share = 0
        pass
    




class ResponderWaitPage(WaitPage):
    pass

class ResponderPage(Page):
    form_model = models.Group
    form_fields = ['accepted']

    def is_displayed(self):
        return self.player.role() == 'responder'

class ProposerWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass


page_sequence = [
    RoleAnnouncement,
    ProposerSplit,
    ResponderWaitPage,
    ResponderPage,
    ProposerWaitPage,
    Results
]
