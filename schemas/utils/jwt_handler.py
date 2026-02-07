from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, JWTError
import os

SECRET_KEY = os.getenv("JWT_SECRET")