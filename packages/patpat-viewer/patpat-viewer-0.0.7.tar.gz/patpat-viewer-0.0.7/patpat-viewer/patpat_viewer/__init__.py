"""Patpat-viewer APP
    This APP Power by Flask
"""

import os
import re

from flask import Flask
from flask_bootstrap import Bootstrap5


def create_app(name=__name__):
    flask = Flask(name)
    Bootstrap5(flask)

    return flask


app = create_app()

PATPAT_ENV = os.getenv('PATPAT_ENV')
if PATPAT_ENV is None:
    PATPAT_ENV = f'{re.match(".*(?=__init__)" ,os.path.abspath(__file__)).group()}patpat_env'

app.config['PATPAT_ENV'] = PATPAT_ENV

from patpat_viewer import viewer

