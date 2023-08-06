import ptvsd
import os
import logging
import logging_loki
import sys
import time

from flask import Flask

# Lendo variáveis de ambiente
APP_NAME = os.environ['APP_NAME']
DEBUG = bool(os.getenv('DEBUG', 'False'))
MOPE_CODE = os.environ['MOPE_CODE']

MULTI_DATABASE_HOST = os.environ['MULTI_DATABASE_HOST']
MULTI_DATABASE_PASS = os.environ['MULTI_DATABASE_PASS']
MULTI_DATABASE_PORT = os.environ['MULTI_DATABASE_PORT']
MULTI_DATABASE_NAME = os.environ['MULTI_DATABASE_NAME']
MULTI_DATABASE_USER = os.environ['MULTI_DATABASE_USER']
DEFAULT_EXTERNAL_DATABASE_USER = os.environ['DEFAULT_EXTERNAL_DATABASE_USER']
DEFAULT_EXTERNAL_DATABASE_PASSWORD = os.environ['DEFAULT_EXTERNAL_DATABASE_PASSWORD']
