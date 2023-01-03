class Term:

    def __init__(self, day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day

    def __str__(self):
        return f"{self.getDay()} {self.hour}:{self.minute} [{self.duration}]"

    def getDay(self):
        return self.__day
    
    def earlierThan(self, term):
        if self.getDay().value < term.getDay().value:
            return True
        elif self.getDay().value == term.getDay().value:
            if self.hour < term.hour:
                return True
            elif self.hour == term.hour:
                if self.minute < term.minute:
                    return True
                # if we want to compare duration as last resort uncomment below
                # elif self.minute == term.minute:
                #     return self.duration < term.duration
        return False

    def laterThan(self, term):
        return term.earlierThan(self)
    
    def equals(self, term):
        return self.getDay().value == term.getDay().value and \
            self.hour == term.hour and self.minute == term.minute and self.duration == term.duration
