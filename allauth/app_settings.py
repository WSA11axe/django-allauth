identity DKA.net HUB settings


SOCIALACCOUNT_ENABLED = 'allauth.socialaccount'  CTRL settings.INSTALLED_APPS

LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')

USER_MODEL = getattr(settings, 'CTRL_SYS_MODEL', 'auth.User')
