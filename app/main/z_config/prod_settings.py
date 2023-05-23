import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DOMAIN = 'http://localhost'
#BASE_DOMAIN = 'https://black-financier.com'
#BASE_DOMAIN = 'http://black-financier.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [ '167.99.142.239', 'black-financier.com', 'django', 'localhost',  '0.0.0.0', 'django_gunicorn', 'telegram', 'django_gunicorn:8000', '*', '127.0.0.1', '167.99.142.239', 'black-financier.com']

# rest

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

# cors

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    BASE_DOMAIN,
    'http://django_gunicorn',
    'http://telegram'
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
'''STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]'''

# Smtp

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'blackfinancierdja@gmail.com'
EMAIL_HOST_PASSWORD = 'tyuwpblrrbuqxapx'
EMAIL_PORT = 587

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        "console": {
            "format": "{asctime} - {levelname} - {module} - {funcName} - {pathname} - {message}",
            "style": "{",
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file_django_main': {
            'class': 'logging.FileHandler',
            'formatter': 'console',
            'filename': "logs/main/z_err_django.log"
        },
        'file_my_log': {
            'class': 'logging.FileHandler',
            'formatter': 'console',
            'filename': "logs/main/z_err_my.log"
        }
    },

    'loggers': {
        # Might as well log any errors anywhere else in Django
        'django': {
            #'handlers': ['file_django_main', 'console'],
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },

        # My errors
        "main": {
            'handlers': ['file_my_log'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}



# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }



'''CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', '6379')],
        },
    },
}'''
