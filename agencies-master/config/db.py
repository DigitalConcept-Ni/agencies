import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apolo',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TENANT = {
    'default': {
    'ENGINE': 'django_tenants.postgresql_backend',
    'NAME': 'admin',
    'USER': 'postgres',
    'PASSWORD': '00Dascher',
    'HOST': 'localhost',
    'PORT': '5432',
}}

TENANT_SERVER = {
    'default': {
    'ENGINE': 'django_tenants.postgresql_backend',
    'NAME': 'bisb',
    'USER': 'postgres',
    'PASSWORD': 'M@te0urbin@',
    'HOST': 'localhost',
    'PORT': '5432',
}}

# mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
