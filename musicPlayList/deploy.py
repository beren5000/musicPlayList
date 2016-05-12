from settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'musicplaylist',
       'USER': 'superuser',
       'PASSWORD': 'admin',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/beren5000/webapps/musicplaylist/musicPlayList/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/home/beren5000/webapps/musicplaylist_media'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = 'http://beren5000.webfactional.com/media/'
# END MEDIA CONFIGURATION

STATIC_ROOT = '/home/beren5000/webapps/musicplaylist_static'
STATIC_URL = 'http://beren5000.webfactional.com/static/'