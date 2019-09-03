from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Introduction)
        yield (pages.Trade, {
            'trade_attempted': False,
            'role_pre': 'Vendedor',
            'group_color': 'Rojo',
            'other_role_pre': 'Comprador',
            'other_group_color': 'Azul',
        })
        yield (pages.Results, {
            'trade_succeeded': False,
            'token_color': None,
            'round_payoff': 0,
        })

