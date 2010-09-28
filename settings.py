import os

PLATFORM = os.uname()[0]
if PLATFORM == 'Darwin':
    DEBUG = True

elif PLATFORM == 'Linux':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'voxi.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

PROJECT_DIR = 'voxinfinitus'

SITE_NAME = 'Vox Infinitus'
SITE_DESCRIPTION = 'A network dedicated to encouraging and solidfying equal and free access to information, defending freedom of expression, and promoting transparency.'
SITE_COPYRIGHT = u'Max Countryman, Alex Toney'
GOOGLE_ANALYTICS_ID = ''

SECRET_KEY = 'change this :)'

SITE_ID = 4096

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

if not DEBUG:
    MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',) + MIDDLEWARE_CLASSES

if not DEBUG:
	CACHE_BACKEND = 'memcached://127.0.0.1:11211/?timeout=120'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)

USE_I18N = False

GLOBAL_MEDIA_DIRS = (
    os.path.join(os.path.dirname(__file__), 'media'),
)

ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.syndication',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
)
