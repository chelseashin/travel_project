"""
Django settings for travel project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ze0!(hchui0!89bzok@fs*)xw7&bbz=4t9)10zggby$vm97d#$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites', # 추가 for 소셜 로그인
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'myaccounts',
    'maps',


    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'travel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'travel', 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # `allauth` needs this from django
                'django.template.context_processors.request',

            ],
        },
    },
]

WSGI_APPLICATION = 'travel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',  #mysql
        'USER': 'root', #root
        'PASSWORD': 'ssafydif', #1234
        'HOST': '192.168.31.83', #공백으로 냅두면 default localhost
        'PORT': '' #공백으로 냅두면 default 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'travel', 'static'),
]

AUTH_USER_MODEL = 'myaccounts.MyUser'

# LOGIN_URL='/accounts/login'


SITE_ID = 1
LOGIN_REDIRECT_URL='/'



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',

)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'kakao': {
        'SCOPE': [
            'profile',
            
        ]
    }
}

#     # 'facebook': {
#     #     'METHOD': 'oauth2',
#     #     'SCOPE': ['email', 'public_profile', 'user_friends'],
#     #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#     #     'INIT_PARAMS': {'cookie': True},
#     #     'FIELDS': [
#     #         'id',
#     #         'email',
#     #         'name',
#     #         'first_name',
#     #         'last_name',
#     #         'verified',
#     #         'locale',
#     #         'timezone',
#     #         'link',
#     #         'gender',
#     #         'updated_time',
#     #     ],
#     #     'EXCHANGE_TOKEN': True,
#     #     'LOCALE_FUNC': 'path.to.callable',
#     #     'VERIFIED_EMAIL': False,
#     #     'VERSION': 'v2.12',
#     # },
# }


# SOCIAL_AUTH_FACEBOOK_KEY = '2112059258920786'
# SOCIAL_AUTH_FACEBOOK_SECRET = '7dc2529524c24e6ba12b5bf21b03de18'
# test id/key
# SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_KEY
# SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_SECRET
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
 
# # Google
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = GOOGLE_KEY
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = GOOGLE_SECRET
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
 
# # Twitter
# # SOCIAL_AUTH_TWITTER_KEY = ''
# # SOCIAL_AUTH_TWITTER_SECRET = ''

# # Kakao
# SOCIAL_AUTH_KAKAO_KEY = KAKAO_KEY
# SOCIAL_AUTH_KAKAO_SECRET = KAKAO_SECRET

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.user.get_username',
#     'social.pipeline.user.create_user',
#     # 'accounts.social.create_user', # 덮어씀
#     # 'accounts.social.update_avatar', # 추가함
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details'
# )