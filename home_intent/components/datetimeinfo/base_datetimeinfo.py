import locale
import logging
from datetime import datetime
from dataclasses import dataclass

from babel.dates import format_date, format_time

from home_intent import HomeIntent, Intents


intents = Intents(__name__)


class BaseDateTimeInfo:

    def __init__(self, language: str = "en"):
        # TODO: keep track of timers and add ability to remove timers
        # self.timers = []
        self._lang = language
        self._logger = logging.getLogger("rhasspy.component.datetime")

    @property
    def date(self):
        return format_date(datetime.now(), format="full", locale=self._lang)

    @property
    def time(self):
        return format_time(datetime.now(), format="medium", locale=self._lang)
