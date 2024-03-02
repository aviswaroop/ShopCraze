from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    session_name='test_session',
    initial_cash='[2600, 2600]',
    random_round_payoff=True,
    training_round=False,
    real_world_currency_per_point=1,
    participation_fee=1.00,
    doc='',
)

SESSION_CONFIGS = [
    dict(
        name='Experiment',
        num_demo_participants=1,
        app_sequence=['ShopCraze']
    ),
]
DEBUG = False
SESSION_FIELDS = ['num_rounds']
PARTICIPANT_FIELDS = ['name', 'age', 'gender', 'cash', 'product', 'permutation']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='ALexperiment',
        display_name='AL Research Study',
        participant_label_file='_rooms/ALexperiment_test.txt',
        use_secure_urls=True
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
<b>E-Commerce Website</b>
<p>Welcome to this experiment conducted by Ananya Limaye.<br>
The experiment takes the shape of an e-commerce website.</p>
"""

# Change this default secret key to a fully random one after forking.
SECRET_KEY = '1sjjosef4a7#)%cb3_us8%aa*l_d476lp&*hatrb6al*u*dude^'