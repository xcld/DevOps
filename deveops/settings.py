# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 09 13:49
# Author Yo
# Email YoLoveLife@outlook.com
"""
Django settings for devEops project.

Generated by 'django-admin startproject' using Django 2.0+.
"""
from __future__ import absolute_import
import os
import sys
import django.db.backends.mysql
from deveops.variable import *
from deveops import conf as DEVEOPS_CONF
ENVIRONMENT=DEVEOPS_CONF.ENVIRONMENT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = BASE_DIR+'/apps'
import sys
sys.path.append(APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1x$!#dwp2_6^tdgs1nv8pwgutbc#4m%#qaz!m!0h_f*%6fp+vt'

#ASGI
ASGI_APPLICATION = 'deveops.routing.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'utils.apps.UtilsConfig',
    'authority.apps.AuthorityConfig',
    'manager.apps.ManagerConfig',
    'ops.apps.OpsConfig',
    'work.apps.WorkConfig',
    'timeline.apps.TimelineConfig',
    'variable.apps.VariableConfig',
    'dashboard.apps.DashboardConfig',
    'yodns.apps.YoDnsConfig',
    'db.apps.DBConfig',
    'monitor.apps.MonitorConfig',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'channels',
    # 'django.contrib.messages',
    # 'bootstrap3',
    # 'djcelery', #celery
    # 'kombu.transport.django', #celery
]

#JWF
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_SECRET_KEY': SECRET_KEY,
}


REST_FRAMEWORK = {
    # 'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'deveops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deveops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':DEVEOPS_CONF.DB_NAME,
        'USER':DEVEOPS_CONF.DB_USER,
        'PASSWORD':DEVEOPS_CONF.DB_PASSWD,
        'HOST':DEVEOPS_CONF.DB_HOST,
        'PORT':DEVEOPS_CONF.DB_PORT,
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

# FILE_CHARSET='gb18030'
#
DEFAULT_CHARSET='utf-8'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18N translation
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = BASE_DIR + DEVEOPS_CONF.MEDIA_ROOT
MEDIA_URL = '/media/'

#Ops dir
OPS_ROOT = MEDIA_ROOT + DEVEOPS_CONF.OPS_ROOT

#Work dir
WORK_ROOT = MEDIA_ROOT + DEVEOPS_CONF.WORK_ROOT

#Dashboard dir
DASHBOARD_ROOT = MEDIA_ROOT + DEVEOPS_CONF.DASHBOARD_ROOT

#QCode dir
QCODE_ROOT = MEDIA_ROOT + DEVEOPS_CONF.QCODE_ROOT

#Tool dir
TOOL_ROOT = BASE_DIR + DEVEOPS_CONF.TOOL_ROOT

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "DevOps/ops"),
    os.path.join(BASE_DIR, "DevOps/static"),
    os.path.join(BASE_DIR, "DevOps/media"),
)

#LOGIN
LOGIN_URL='/validate/login'
AUTH_USER_MODEL='authority.ExtendUser'

#SESSION
SESSION_SAVE_EVERY_REQUEST=True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=DEVEOPS_CONF.SESSION_COOKIE_AGE

#SSH
SSH_TIMEOUT=DEVEOPS_CONF.SSH_TIMEOUT

# LDAP
if ENVIRONMENT != 'TRAVIS':
    from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
    import ldap
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    AUTH_LDAP_SERVER_URI = DEVEOPS_CONF.LDAP_SERVER
    AUTH_LDAP_BIND_DN = "cn=tools,ou=Zabbix,ou=TEST,dc=zbjt,dc=com"
    AUTH_LDAP_BIND_PASSWORD = DEVEOPS_CONF.LDAP_PASSWD

    OU = DEVEOPS_CONF.LDAP_OU
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(objectClass=groupOfNames)")
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
    AUTH_LDAP_USER_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE,"(&(objectClass=*)(sAMAccountName=%(user)s))")
    AUTH_LDAP_USER_ATTR_MAP = {
        "full_name": "cn",
        "description": "description",
        "first_name":"sn",
        "phone":"mobile",
        "groups": "",
    }
    AUTH_LDAP_ALWAYS_UPDATE_USER = True
    # AUTH_LDAP_MIRROR_GROUPS = True
else:
    pass

#VMARE
VMWARE_USERNAME = DEVEOPS_CONF.VMWARE_USERNAME
VMWARE_PASSWD = DEVEOPS_CONF.VMWARE_PASSWD
VMWARE_SERVER = DEVEOPS_CONF.VMWARE_SERVER

#ALIYUN
ALIYUN_ACCESSKEY = DEVEOPS_CONF.ALIYUN_ACCESSKEY
ALIYUN_ACCESSSECRET = DEVEOPS_CONF.ALIYUN_ACCESSSECRET
ALIYUN_PAGESIZE = DEVEOPS_CONF.ALIYUN_PAGESIZE
ALIYUN_EXPIREDTIME = DEVEOPS_CONF.ALIYUN_EXPIREDTIME
ALIYUN_OVERDUETIME = DEVEOPS_CONF.ALIYUN_OVERDUETIME

# DNS
INNER_DNS = DEVEOPS_CONF.INNER_DNS
OUTER_DNS = DEVEOPS_CONF.OUTER_DNS


#CRONTAB
DASHBOARD_TIME = DEVEOPS_CONF.DASHBOARD_TIME
EXPIRED_TIME = DEVEOPS_CONF.EXPIRED_TIME
MANAGER_TIME = DEVEOPS_CONF.MANAGER_TIME
DNS_TIME = DEVEOPS_CONF.DNS_TIME

#REDIS
REDIS_HOST = DEVEOPS_CONF.REDIS_HOST
REDIS_PORT = DEVEOPS_CONF.REDIS_PORT
REDIS_SPACE = DEVEOPS_CONF.REDIS_SPACE
REDIS_PASSWD = DEVEOPS_CONF.REDIS_PASSWD


#CHANNEL
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(
                "redis://:{PASSWORD}@{HOST}:{PORT}/{SPACE}".format(
                    PASSWORD=REDIS_PASSWD,
                    HOST=REDIS_HOST,
                    PORT=REDIS_PORT,
                    SPACE=REDIS_SPACE)
            )],
        },
        # "ROUTING": "deveops.routing.routing",
    },
}

#FileUpload
# FILE_UPLOAD_HANDLERS=(
#     "django.core.files.uploadhandler.MemoryFileUploadHandler",
#     "django.core.files.uploadhandler.TemporaryFileUploadHandler"
# )
# import django.core.files.uploadhandler


#DJANGO LOG
# if DEBUG == True:
#     LOGGING_LEVEL = 'DEBUG'
# else:
#     LOGGING_LEVEL = 'WARNING'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#        'standard': {
#            # 'format': '%(levelname)s-%(asctime)s-'
#            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'  #日志格式
#        }
#     },
#     'filters': {
#     },
#     'handlers': {
#         'default': {
#             'level':LOGGING_LEVEL,
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/django.log',     #日志输出文件
#             'maxBytes': 1024*1024*5,                  #文件大小
#             'backupCount': 5,                         #备份份数
#             'formatter':'standard',                   #使用哪种formatters日志格式
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default'],
#             'level': LOGGING_LEVEL,
#             'propagate': False
#         }
#     }
# }
#
# #PERSON LOG
# import logging
# import logging.config
# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# #                     datefmt='%a, %d %b %Y %H:%M:%S',
# #                     filename='logs/myapp.log',
# #                     filemode='w')
#
# logging.config.fileConfig('logging.ini')
# logger = logging.getLogger("deveops.api")
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')