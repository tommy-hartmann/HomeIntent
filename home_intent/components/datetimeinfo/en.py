from .base_datetimeinfo import intents, BaseDateTimeInfo


class DateTimeInfo(BaseDateTimeInfo):

    @intents.beta
    @intents.sentences([
    "what day is it"
    "what date is it"
    "what is the current date"
    ])
    def info_date(self):
        return f"Today is {self.date}"
        
    @intents.beta
    @intents.sentences([
        "what time is it", 
        "what' is the time [please]", 
        "what's the time [please]" 
        "could you [please] tell me the time?"
    ])
    def info_time(self):
        return f"It is {self.time}"