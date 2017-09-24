import os
from os import environ

import dj_database_url
#from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = '0fz@15bw4hsx%rz$zl$lg+wccwpbov#v+ci@f7-v9t@ptjfa13'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otreechat']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
    {
        'name': 'survey',
        'display_name': 'my1stsurvey',
        'num_demo_participants': 1,
        'app_sequence': ['survey'],
        'participation_fee': 3.00,
    },
    {
        'name': 'fortune',
        'display_name': 'the fortune',
        'num_demo_participants': 1,
        'app_sequence': ['fortune'],
        'participation_fee': 3.00,
    },    
    {
        'name': 'prisoners_dilemma',
        'display_name': 'the prisoners dilemma',
        'num_demo_participants': 2,
        'app_sequence': ['prisoners_dilemma'],
        'participation_fee': 3.00,
    },
    # {
    #     'name': 'ultimatom_game',
    #     'display_name': 'the ultimatom game',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['ultimatom_game'],
    #     'participation_fee': 3.00,
    # },
    {
        'name': 'Treatment_demo',
        'display_name': 'the Treatment Demo',
        'num_demo_participants': 1,
        'app_sequence': ['Treatment_demo'],
        'participation_fee': 3.00,
    },
    {
        'name': 'new_treatmentdemo',
        'display_name': 'new_treatmentdemo',
        'num_demo_participants': 1,
        'app_sequence': ['new_treatmentdemo'],
        'participation_fee': 3.00,
        'treatment': 'high',
    },
    {
        'name': 'Quiz_Time',
        'display_name': 'Quiz Time',
        'num_demo_participants': 5,
        'app_sequence': ['quiz_time'],
        'participation_fee': 3.00,
    },
    {
        'name': 'chat',
        'display_name': 'chat',
        'num_demo_participants': 2,
        'app_sequence': ['chat'],
        'participation_fee': 3.00,
    },
    {
        'name': 'chat_in_ultimatom',
        'display_name': 'chat_in_ultimatom',
        'num_demo_participants': 2,
        'app_sequence': ['chat_in_ultimatom'],
        'participation_fee': 3.00,
    },
    
    {
        'name': 'assignment_full_info',
        'display_name': 'Assignment Full Information Treatment',
        'num_demo_participants': 8,
        'app_sequence': ['assignment'],
        'participation_fee': 3.00,
        'treatment': 'full_info',
        #'my_page_timeout_seconds': 120,
    }, 

    {
        'name': 'assignment_part_info',
        'display_name': 'Assignment Partial Information Treatment',
        'num_demo_participants': 8,
        'app_sequence': ['assignment'],
        'participation_fee': 3.00,
        'treatment': 'part_info',
        #'my_page_timeout_seconds': 120,
    },

    {
        'name': 'assignment_part_info_4p',
        'display_name': 'Assignment Partial Information Game With 4 Players',
        'num_demo_participants': 4,
        'app_sequence': ['assignment'],
        'participation_fee': 3.00,
        'treatment': 'part_info',
        #'my_page_timeout_seconds': 120,
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
