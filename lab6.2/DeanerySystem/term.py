from .day import Day


class Term:

    def __init__(self, day, hour, minute, duration=90):
        self._hour = hour
        self._minute = minute
        self._duration = duration
        self.__day = day

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if 0 <= value <= 23:
            self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if 0 <= value < 60:
            self._minute = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        pass

    def __str__(self):
        return f"{self.getDay()} {self._hour}:{self._minute} [{self._duration}]"

    def getDay(self):
        return self.__day
    
    def earlierThan(self, term):
        if self.getDay().value < term.getDay().value:
            return True
        elif self.getDay().value == term.getDay().value:
            if self._hour < term._hour:
                return True
            elif self._hour == term._hour:
                if self._minute < term._minute:
                    return True
                # if we want to compare duration as last resort uncomment below
                # elif self.minute == term.minute:
                #     return self.duration < term.duration
        return False

    def laterThan(self, term):
        return term.earlierThan(self)
    
    def equals(self, term):
        return self.getDay().value == term.getDay().value and \
               self._hour == term._hour and self._minute == term._minute and self._duration == term._duration

    def __lt__(self, other):
        return self.earlierThan(other)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __eq__(self, other):
        return self.equals(other)

    def __sub__(self, other):
        def term_to_mins(t):
            return t.getDay().value * 24 * 60 + t.hour * 60 + t.minute

        duration = term_to_mins(self) - term_to_mins(other) + other._duration
        return Term(other._Term__day, other._hour, other._minute, duration)

    def __add__(self, other):
        if type(other) is int:
            term_to_minutes = self.__day.value * 60 * 24 + \
                self.hour * 60 + self.minute + other
            minutes_to_day = Day(term_to_minutes // (24 * 60))
            minutes_to_hour = (term_to_minutes - minutes_to_day.value * 24 * 60) // 60
            minutes_to_minutes = term_to_minutes - minutes_to_day.value * 24 * 60 - minutes_to_hour * 60
            return Term(minutes_to_day, minutes_to_hour, minutes_to_minutes, self.duration)