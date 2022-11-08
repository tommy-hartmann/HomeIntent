from .base_datetimeinfo import intents, BaseDateTimeInfo


class DateTimeInfo(BaseDateTimeInfo):

    @intents.beta
    @intents.sentences([
    "welches datum ist heute",
    "welcher (tag|wochentag) ist heute",
    ])
    def info_date(self):
        return f"Heute ist {self.date}"
    
    @intents.beta
    @intents.sentences([
        "wie spät ist es",
        "wie (ist|lautet) die [aktuelle] uhrzeit"
    ])
    def info_time(self):
        return f"Es ist {self.time}"