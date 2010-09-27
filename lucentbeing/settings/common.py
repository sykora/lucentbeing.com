'''Common settings for lucentbeing.com.'''

import os

# Paths and URLs.
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

ADMINS = (
    ('P.C. Shyamshankar', 'sykora@lucentbeing.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Asia/Calcutta'

LANGUAGE_CODE = 'en-us'

USE_I18N = False
USE_L10N = False

SITE_ID = 1
