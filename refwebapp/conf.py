import distutils.util
import os

DB_URL = os.getenv("REFWEBAPP_DB_URL", "sqlite:///refwebapp.sqlite")
DEBUG = bool(
    distutils.util.strtobool(os.getenv("REFWEBAPP_DEBUG", "false").lower())
)
