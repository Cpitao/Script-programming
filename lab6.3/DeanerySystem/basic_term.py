class BasicTerm:
    def __init__(self, hour, minute, duration):
        self._hour = hour
        self._minute = minute
        self._duration = duration

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
        self._duration = value

