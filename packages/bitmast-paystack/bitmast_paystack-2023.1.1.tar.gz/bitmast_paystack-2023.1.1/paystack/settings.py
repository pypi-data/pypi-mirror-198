import os
from dotenv import load_dotenv

load_dotenv()
env = os.environ.get

DEBUG = True # Set to false in production.

# SECURITY WARNING: keep the secret key used in production secret!

# Payment Gateway configuration
TEST_SECRET_KEY = env('TEST_SECRET_KEY')
LIVE_SECRET_KEY = env('LIVE_SECRET_KEY')
CONTENT_TYPE = env('CONTENT_TYPE')
CACHE = env('CACHE')
