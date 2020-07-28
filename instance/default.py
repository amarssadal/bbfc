import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://localhost:5432/bbcf"

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "ea77cb5c6f56e5402e9ed520674adcc9ade5bb9b77378982"

DEBUG = True
