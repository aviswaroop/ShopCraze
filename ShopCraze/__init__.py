from otree.api import *
from random import randint, seed
from datetime import datetime

author = 'Abhinav Viswaroop'

doc = """Ecommerce website for experiment"""

# Tracking the occurrence of each round
r1_occur = False
r2_occur = False
r3_occur = False

r1_page = 0
r2_page = 0
r3_page = 0

class C(BaseConstants):
    NAME_IN_URL = 'ShopCraze'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: BaseSubsession):
    global r1_page, r2_page, r3_page
    seed(datetime.now().timestamp())
    if subsession.round_number == 1:
        for p in subsession.get_players():
            participant = p.participant
            participant.r1_page = randint(1, 4)
            participant.r2_page = randint(1, 4)
            participant.r3_page = randint(1, 4)
            participant.permutation = (participant.r1_page * 100) + (participant.r2_page * 10) + participant.r3_page
            print('permutation = ', participant.permutation)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="Your initials:")
    age = models.IntegerField(label="Your age:", min=17, max=85)
    gender = models.StringField(choices=['Female', 'Male', 'Other'])
    cash = models.IntegerField(initial=2600)
    product = models.StringField(widget=widgets.RadioSelect,
                                 label="Add to Cart",
                                 choices=['product1', 'product2', 'product3'],
                                 initial=0)
    permutation = models.IntegerField(initial=((r1_page * 100) + (r2_page * 10) + r3_page))
    r1_page = models.IntegerField()
    r2_page = models.IntegerField()
    r3_page = models.IntegerField()


# List of Pages

class InstructionPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class HomePage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class LoginPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'gender']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass


# CartPages for Round 1
class CartPage11(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r1_occur is False:
            if (player.product == 'product1') and (player.round_number == 1):
                return player.round_number == 1
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r1_occur
        r1_occur = True

class CartPage121(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r1_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 1):
                if participant.r1_page == 1:
                    return player.round_number == 1
            elif (player.product == 'product3') and (player.round_number == 1):
                if participant.r1_page == 4:
                    return player.round_number == 1
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r1_occur
        r1_occur = True

class CartPage122(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r1_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 1):
                if participant.r1_page == 3:
                    return player.round_number == 1
            elif (player.product == 'product3') and (player.round_number == 1):
                if participant.r1_page == 2:
                    return player.round_number == 1
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r1_occur
        r1_occur = True

class CartPage131(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r1_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 1):
                if participant.r1_page == 1:
                    return player.round_number == 1
            elif (player.product == 'product2') and (player.round_number == 1):
                if participant.r1_page == 4:
                    return player.round_number == 1
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r1_occur
        r1_occur = True

class CartPage132(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r1_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 1):
                if participant.r1_page == 3:
                    return player.round_number == 1
            elif (player.product == 'product2') and (player.round_number == 1):
                if participant.r1_page == 2:
                    return player.round_number == 1
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r1_occur
        r1_occur = True

# CartPages for Round 2
class CartPage21(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r2_occur is False:
            if (player.product == 'product1') and (player.round_number == 2):
                return player.round_number == 2
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r2_occur
        r2_occur = True

class CartPage221(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r2_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 2):
                if participant.r2_page == 1:
                    return player.round_number == 2
            elif (player.product == 'product3') and (player.round_number == 2):
                if participant.r2_page == 4:
                    return player.round_number == 2
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r2_occur
        r2_occur = True

class CartPage222(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r2_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 2):
                if (participant.r2_page == 1) or (participant.r2_page == 3):
                    return player.round_number == 2
            elif (player.product == 'product3') and (player.round_number == 2):
                if participant.r2_page == 2:
                    return player.round_number == 2
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r2_occur
        r2_occur = True

class CartPage231(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r2_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 2):
                if participant.r2_page == 1:
                    return player.round_number == 2
            elif (player.product == 'product2') and (player.round_number == 2):
                if participant.r2_page == 4:
                    return player.round_number == 2
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r2_occur
        r2_occur = True

class CartPage232(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r2_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 2):
                if participant.r2_page == 3:
                    return player.round_number == 2
            elif (player.product == 'product2') and (player.round_number == 2):
                if participant.r2_page == 2:
                    return player.round_number == 2
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r2_occur
        r2_occur = True

# CartPages for Round 3
class CartPage31(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r3_occur is False:
            if (player.product == 'product1') and (player.round_number == 3):
                return player.round_number == 3
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r3_occur
        r3_occur = True

class CartPage321(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r3_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 3):
                if participant.r3_page == 1:
                    return player.round_number == 3
            elif (player.product == 'product3') and (player.round_number == 3):
                if participant.r3_page == 4:
                    return player.round_number == 3
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r3_occur
        r3_occur = True

class CartPage322(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r3_occur is False:
            participant = player.participant
            if (player.product == 'product2') and (player.round_number == 3):
                if (participant.r3_page == 1) or (participant.r3_page == 3):
                    return player.round_number == 3
            elif (player.product == 'product3') and (player.round_number == 3):
                if (participant.r3_page == 2) or (participant.r3_page == 4):
                    return player.round_number == 3
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r3_occur
        r3_occur = True

class CartPage331(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r3_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 3):
                if participant.r3_page == 3:
                    return player.round_number == 3
            elif (player.product == 'product2') and (player.round_number == 3):
                if participant.r3_page == 4:
                    return player.round_number == 3
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r3_occur
        r3_occur = True

class CartPage332(Page):
    @staticmethod
    def is_displayed(player: Player):
        if r3_occur is False:
            participant = player.participant
            if (player.product == 'product3') and (player.round_number == 3):
                if participant.r3_page == 3:
                    return player.round_number == 3
            elif (player.product == 'product2') and (player.round_number == 3):
                if participant.r3_page == 2:
                    return player.round_number == 3
            else:
                return 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        global r3_occur
        r3_occur = True

# PurchasePages for Round 1
class PurchasePage11(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 if ((player.round_number == 1) and (participant.r1_page == 1)) else 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 1579
        elif player.product == 'product2':
            player.cash -= 1162
        else:
            player.cash -= 1500
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.participant.r1_page = participant.r1_page

class PurchasePage12(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 if ((player.round_number == 1) and (participant.r1_page == 2)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 1579
        elif player.product == 'product2':
            player.cash -= 1162
        else:
            player.cash -= 1500
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.participant.r1_page = participant.r1_page

class PurchasePage13(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 if ((player.round_number == 1) and (participant.r1_page == 3)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 1579
        elif player.product == 'product2':
            player.cash -= 1500
        else:
            player.cash -= 1162
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.participant.r1_page = participant.r1_page


class PurchasePage14(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 if ((player.round_number == 1) and (participant.r1_page == 4)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 1579
        elif player.product == 'product2':
            player.cash -= 1500
        else:
            player.cash -= 1162
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.participant.r1_page = participant.r1_page

# PurchasePages for Round 2
class PurchasePage21(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 2  if ((player.round_number == 2) and (participant.r2_page == 1)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 289
        elif player.product == 'product2':
            player.cash -= 188
        else:
            player.cash -= 211
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']


class PurchasePage22(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 2  if ((player.round_number == 2) and (participant.r2_page == 2)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 289
        elif player.product == 'product2':
            player.cash -= 188
        else:
            player.cash -= 211
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']

class PurchasePage23(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 2  if ((player.round_number == 2) and (participant.r2_page == 3)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 289
        elif player.product == 'product2':
            player.cash -= 211
        else:
            player.cash -= 188
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']

class PurchasePage24(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 2  if ((player.round_number == 2) and (participant.r2_page == 4)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 289
        elif player.product == 'product2':
            player.cash -= 211
        else:
            player.cash -= 188
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']

# PurchasePages for Round 3
class PurchasePage31(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 3  if ((player.round_number == 3) and (participant.r3_page == 1)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 680
        elif player.product == 'product2':
            player.cash -= 528
        else:
            player.cash -= 625
        participant.cash = player.cash
        player.permutation = player.participant.vars['permutation']

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']

class PurchasePage32(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 3  if ((player.round_number == 3) and (participant.r3_page == 2)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 680
        elif player.product == 'product2':
            player.cash -= 528
        else:
            player.cash -= 625
        participant.cash = player.cash

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']
        player.permutation = player.participant.vars['permutation']

class PurchasePage33(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 3  if ((player.round_number == 3) and (participant.r3_page == 3)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 680
        elif player.product == 'product2':
            player.cash -= 625
        else:
            player.cash -= 528
        participant.cash = player.cash

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']
        player.permutation = player.participant.vars['permutation']

class PurchasePage34(Page):
    form_model = 'player'
    form_fields = ['product']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 3  if ((player.round_number == 3) and (participant.r3_page == 4)) else 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.name = player.name
        participant.age = player.age
        participant.gender = player.gender
        if player.product == 'product1':
            player.cash -= 680
        elif player.product == 'product2':
            player.cash -= 625
        else:
            player.cash -= 528
        participant.cash = player.cash

    @staticmethod
    def vars_for_template(player: Player):
        player.name = player.participant.vars['name']
        player.gender = player.participant.vars['gender']
        player.age = player.participant.vars['age']
        player.cash = player.participant.vars['cash']

# Final Segment of the Experiment
class ResultsPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    def to_human_readable(self, x):
        return '{:,}'.format(int(x))

    @staticmethod
    def to_human_readable_text(x):
        return '{:}'.format(str(x))

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        n = ''
        a = 0
        g = ''
        c = 0
        player_in_all_rounds = player.in_all_rounds()
        for p in player_in_all_rounds:
            n = p.name
            a = p.age
            g = p.gender
            c = p.cash
            break
        return dict(
            name = ResultsPage.to_human_readable_text(n),
            age = a,
            gender =ResultsPage.to_human_readable_text(g),
            cash = c
        )

class DebriefPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

page_sequence = [InstructionPage, HomePage, LoginPage,
                 PurchasePage11, PurchasePage12, PurchasePage13, PurchasePage14,
                 CartPage11, CartPage121, CartPage122, CartPage131, CartPage132,
                 PurchasePage21, PurchasePage22, PurchasePage23,PurchasePage24,
                 CartPage21, CartPage221, CartPage222, CartPage231, CartPage232,
                 PurchasePage31, PurchasePage32, PurchasePage33, PurchasePage34,
                 CartPage31, CartPage321, CartPage322, CartPage331, CartPage332,
                 ResultsPage, DebriefPage]

