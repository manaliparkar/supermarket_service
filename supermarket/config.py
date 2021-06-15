"""Application configuration."""
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_NAME = 'supermarket_service'

HEALTH_CHECK = '/hello'

POOL_SIZE = 15
POOL_MAX_OVERFLOW = -1
POOL_RECYCLE_MS = 3600  # Avoids connections going stale
POOL_PRE_PING  = True

DB_URL = os.environ.get('DB_URL')
