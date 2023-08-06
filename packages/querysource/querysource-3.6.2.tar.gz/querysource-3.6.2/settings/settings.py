# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
from navconfig import DEBUG, config

# Debug
LOCAL_DEVELOPMENT = (DEBUG is True and sys.argv[0] == 'run.py')

# PGP Credentials
PGP_KEY_PATH = config.get('pgp_key_path')
PGP_PASSPHRASE = config.get('pgp_passphrase')

# Timezone (For parsedate)
# https://dateparser.readthedocs.io/en/latest/#timezone-and-utc-offset
TIMEZONE = config.get('TIMEZONE', fallback='America/New_York')

"""
Databases
"""
# DB Default
# POSTGRESQL Default
DBHOST = config.get('DBHOST', fallback='localhost')
DBUSER = config.get('DBUSER')
DBPWD = config.get('DBPWD')
DBNAME = config.get('DBNAME', fallback='navigator')
DBPORT = config.get('DBPORT', fallback=5432)
if not DBUSER:
    raise RuntimeError('Missing PostgreSQL Default Settings.')

# RETHINKDB
rt_driver = config.get('RT_DRIVER', fallback='rethink')
rt_host = config.get('RT_HOST', fallback='localhost')
rt_port = config.get('RT_PORT', fallback=28015)
rt_database = config.get('RT_DATABASE', fallback='navigator')
rt_user = config.get('RT_USER')
rt_password = config.get('RT_PWD')

# POSTGRESQL
PG_DRIVER = config.get('PG_DRIVER', fallback='pg')
PG_HOST = config.get('PG_HOST', fallback='localhost')
PG_USER = config.get('PG_USER')
PG_PWD = config.get('PG_PWD')
PG_DATABASE = config.get('PG_DATABASE', fallback='navigator')
PG_PORT = config.get('PG_PORT', fallback=5432)
if not PG_USER:
    raise RuntimeError('Missing PostgreSQL Settings.')

POSTGRES_TIMEOUT = config.get('POSTGRES_TIMEOUT', fallback=3600000)
POSTGRES_MIN_CONNECTIONS = config.getint('POSTGRES_MIN_CONNECTIONS', fallback=4)
POSTGRES_MAX_CONNECTIONS = config.getint('POSTGRES_MAX_CONNECTIONS', fallback=300)

database_url = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
    user=PG_USER,
    password=PG_PWD,
    host=PG_HOST,
    port=PG_PORT,
    db=PG_DATABASE
)
SQLALCHEMY_DATABASE_URI = database_url

# database for changes (admin)
asyncpg_url = 'postgres://{user}:{password}@{host}:{port}/{db}'.format(
    user=DBUSER,
    password=DBPWD,
    host=DBHOST,
    port=DBPORT,
    db=DBNAME
)
default_dsn = asyncpg_url

### DWH Connectors
DWH_USER = config.get('DWHUSER', fallback=DBUSER)
DWH_HOST = config.get('DWHHOST', fallback=DBHOST)
DWH_PWD = config.get('DWHPWD', fallback=DBPWD)
DWH_DATABASE = config.get('DWHNAME', fallback=DBNAME)
DWH_PORT = config.get('DWHPORT', fallback=DBPORT)

# read-only access to pg
dwh_url = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
    user=PG_USER,
    password=PG_PWD,
    host=PG_HOST,
    port=PG_PORT,
    db=PG_DATABASE
)
# admin: write-access permission over pg
adwh_url = 'postgres://{user}:{password}@{host}:{port}/{db}'.format(
    user=DWH_USER,
    password=DWH_PWD,
    host=DWH_HOST,
    port=DWH_PORT,
    db=DWH_DATABASE
)

## MS SQL Server:
MSSQL_DRIVER = config.get('MSSQL_DRIVER', fallback='sqlserver')
MSSQL_HOST = config.get('MSSQL_HOST', fallback='localhost')
MSSQL_PORT = config.get('MSSQL_PORT', fallback='1433')
MSSQL_USER = config.get('MSSQL_USER')
MSSQL_PWD = config.get('MSSQL_PWD')
MSSQL_DATABASE = config.get('MSSQL_DATABASE')
if not MSSQL_USER:
    raise Exception('Missing Microsoft SQL Server Settings.')

## CASSANDRA
CASSANDRA_DRIVER = config.get('CASSANDRA_DRIVER', fallback='cassandra')
CASSANDRA_HOST = config.get('CASSANDRA_HOST', fallback='127.0.0.1')
CASSANDRA_PORT = config.get('CASSANDRA_PORT', fallback='9042')
CASSANDRA_USER = config.get('CASSANDRA_USER')
CASSANDRA_PWD = config.get('CASSANDRA_PWD')
CASSANDRA_DATABASE = config.get('CASSANDRA_DATABASE')
if not CASSANDRA_USER:
    raise Exception('Missing Cassandra Settings.')

## INFLUXDB
INFLUX_DRIVER = config.get('INFLUX_DRIVER', fallback='cassandra')
INFLUX_HOST = config.get('INFLUX_HOST', fallback='127.0.0.1')
INFLUX_PORT = config.get('INFLUX_PORT', fallback='8086')
INFLUX_USER = config.get('INFLUX_USER')
INFLUX_PWD = config.get('INFLUX_PWD')
INFLUX_DATABASE = config.get('INFLUX_DATABASE')
if not INFLUX_HOST:
    raise Exception('Missing InfluxDB Settings.')

## MYSQL
MYSQL_DRIVER = config.get('MYSQL_DRIVER', fallback='mysql')
MYSQL_HOST = config.get('MYSQL_HOST', fallback='127.0.0.1')
MYSQL_PORT = config.get('MYSQL_PORT', fallback='3306')
MYSQL_USER = config.get('MYSQL_USER')
MYSQL_PWD = config.get('MYSQL_PWD')
MYSQL_DATABASE = config.get('MYSQL_DATABASE')
if not MYSQL_DATABASE:
    raise Exception('Missing mySQL Settings.')

"""
QuerySet (for QuerySource)
"""

CACHE_HOST = config.get('CACHEHOST', fallback='localhost')
CACHE_PORT = config.get('CACHEPORT', fallback=6379)
CACHE_DB = config.get('CACHEDB', fallback=2)
CACHE_URL = f"redis://{CACHE_HOST}:{CACHE_PORT}/{CACHE_DB}"

REDIS_HOST = config.get('REDIS_HOST', fallback='localhost')
REDIS_PORT = config.get('REDIS_PORT', fallback=6379)
REDIS_DB = config.get('REDIS_DB', fallback=1)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"



"""
REDIS Session
"""
REDIS_SESSION_DB = config.get('REDIS_SESSION_DB', fallback=0)
SESSION_STORAGE = config.get('SESSION_STORAGE', fallback='redis')
SESSION_URL = f"redis://{CACHE_HOST}:{CACHE_PORT}/{REDIS_SESSION_DB}"
CACHE_PREFIX = config.get('CACHE_PREFIX', fallback='navigator')
SESSION_PREFIX = f'{CACHE_PREFIX}_session'

# QuerySet
QUERYSET_DB = config.get('QUERYSET_DB', fallback=3)
QUERYSET_REDIS = f"redis://{REDIS_HOST}:{REDIS_PORT}/{QUERYSET_DB}"

"""
 Memcache
"""
MEMCACHE_HOST = config.get('MEMCACHE_HOST', 'localhost')
MEMCACHE_PORT = config.get('MEMCACHE_PORT', 11211)

"""
 Redash System
"""
REDASH_HOST = config.get('REDASH_HOST', fallback='https://widgets.trocglobal.com')
REDASH_API_KEY = config.get('REDASH_API_KEY')

## AMAZON
aws_region = config.get('REGION', section='AWS', fallback='us-east-1')
aws_bucket = config.get('BUCKET', section='AWS', fallback='navigator-static-files-2')
aws_key = config.get('AWS_KEY')
aws_secret = config.get('AWS_SECRET')

"""
Resource Usage
"""
QUERY_API = config.getboolean('QUERY_API', fallback=True)
SCHEDULER = config.getboolean('SCHEDULER', fallback=True)
SERVICES = config.getboolean('SERVICES', fallback=True)
WEBSOCKETS = config.getboolean('WEBSOCKETS', fallback=True)
API_TIMEOUT = 36000  # 10 minutes
SEMAPHORE_LIMIT = config.get('SEMAPHORE_LIMIT', fallback=4096)

"""
Authentication and Authorization Backend
"""
# Partner Key (for TrocToken)
PARTNER_KEY = config.get('PARTNER_KEY')
PARTNER_SESSION_TIMEOUT = 200000  # in seconds
CYPHER_TYPE = 'RNC'

AUTH_CREDENTIALS_REQUIRED = config.getboolean(
    'AUTH_CREDENTIALS_REQUIRED', fallback=False
)

AUTH_USER_MODEL = config.get(
    'AUTH_USER_MODEL',
    fallback='navigator_auth.models.User'
)

AUTHENTICATION_BACKENDS = (
 'navigator_auth.backends.NoAuth',
 'navigator_auth.backends.DjangoAuth',
 'navigator_auth.backends.BasicAuth',
)

AUTHORIZATION_MIDDLEWARES = (
    # 'navigator.auth.middlewares.django_middleware',
    # 'navigator.auth.middlewares.troctoken_middleware',
)

SESSION_URL = "redis://{}:{}/{}".format(CACHE_HOST, CACHE_PORT, REDIS_SESSION_DB)
CACHE_PREFIX = config.get('CACHE_PREFIX', fallback='navigator')
SESSION_PREFIX = '{}_session'.format(CACHE_PREFIX)
SESSION_TIMEOUT = config.getint('SESSION_TIMEOUT', fallback=360000)
SESSION_KEY = config.get('SESSION_KEY', fallback='id')
SECRET_KEY = 'CAMISA'  # avoid using fixed secret keys for JWT
SESSION_STORAGE = 'NAVIGATOR_SESSION_STORAGE'
SESSION_OBJECT = 'NAV_SESSION'

# Google Analytics
# GA_VIEW_ID=123
# GA_PROPERTY_ID=310649319
# GA_SERVICE_ACCOUNT_NAME="ga-api-a78f7d886a47.json"
# GA_SERVICE_PATH="env/"
GA_SERVICE_ACCOUNT_NAME = "google.json"
GA_SERVICE_PATH = "google/"

### QuerySource variables and Extensions
# Variables: replacement on field values.
QUERYSOURCE_VARIABLES = {
    "current_example": "resources.functions.current_example",
    "first_day": "querysource.libs.functions.first_day",
    "last_day": "querysource.libs.functions.last_day",
}

# FILTERS: functions called on "filter" process.
QUERYSOURCE_FILTERS = {
    "qry_options": "querysource.libs.functions.query_options",
    "grouping_set": "querysource.libs.functions.grouping_set",
    "group_by_child": "querysource.libs.functions.group_by_child",
}
