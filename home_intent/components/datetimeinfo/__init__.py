import logging
from typing import Union

from home_intent import HomeIntent, Intents
from pydantic import BaseModel, Field


def setup(home_intent: HomeIntent):
    dt = home_intent.import_module(__name__)
    home_intent.register(dt.DateTimeInfo(home_intent.language), dt.intents)
   