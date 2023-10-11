import configparser
import os

__config = configparser.ConfigParser()
__config.read("conf/application.conf")

SERVER_CONFIG_SECTION = "SERVER"
SERVICE_CONFIG_SECTION = "SERVICE"
LOG_CONFIG_SECTION = "LOG"
POSTGRES_CONFIG_SECTION = "POSTGRES"
COOKIE_CONFIG_SECTION = "COOKIE"
REDIS_CONFIG_SECTION = "REDIS"


# Server Details
BASE_URL = os.environ.get("BASE_URL", __config.get(SERVER_CONFIG_SECTION, 'base_url'))
PORT = os.environ.get("SERVICE_PORT", __config.get(SERVER_CONFIG_SECTION, 'port'))
HOST = __config.get(SERVER_CONFIG_SECTION, 'host')

# service
ALLOW_ORIGINS = __config.get(SERVICE_CONFIG_SECTION, 'allow_origins').split(",")
SERVER_CAT = __config.get(SERVICE_CONFIG_SECTION, "server_cat")
SESSION_TIMEOUT = os.environ.get('session_timeout', __config.get(SERVICE_CONFIG_SECTION, 'session_timeout'))

# LOG HANDLERS
LOG_BASE_PATH = __config.get(LOG_CONFIG_SECTION, 'base_path')
LOG_LEVEL = __config.get(LOG_CONFIG_SECTION, 'level')
FILE_BACKUP_COUNT = __config.get(LOG_CONFIG_SECTION, 'file_backup_count')
FILE_BACKUP_SIZE = __config.get(LOG_CONFIG_SECTION, 'file_size_mb')
FILE_NAME = LOG_BASE_PATH + __config.get(LOG_CONFIG_SECTION, 'file_name')
LOG_HANDLERS = __config.get(LOG_CONFIG_SECTION, 'handlers')

# Postgres conf
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", __config.get(POSTGRES_CONFIG_SECTION, "postgres_host"))
POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", __config.get(POSTGRES_CONFIG_SECTION, "postgres_port")))
POSTGRES_USER = os.environ.get("POSTGRES_USER", __config.get(POSTGRES_CONFIG_SECTION, "postgres_user"))
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", __config.get(POSTGRES_CONFIG_SECTION, "postgres_password"))
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", __config.get(POSTGRES_CONFIG_SECTION, "postgres_database"))

# cookie
COOKIE_STR = __config.get(COOKIE_CONFIG_SECTION, "cookie_str")
COOKIE_KEY = os.environ.get("COOKIE_KEY", __config.get(COOKIE_CONFIG_SECTION, "cookie_key"))
COOKIE_EXPIRATION_IN_SECONDS = os.environ.get("COOKIE_EXPIRATION_IN_SECONDS",
                                              __config.get(COOKIE_CONFIG_SECTION, "cookie_expire_time_seconds"))

# Redis Details
REDIS_HOST = os.environ.get("REDIS_HOST", __config.get(REDIS_CONFIG_SECTION, "host"))
REDIS_PORT = os.environ.get("REDIS_PORT", __config.get(REDIS_CONFIG_SECTION, "port"))
