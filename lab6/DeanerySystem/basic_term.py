class BasicTerm:

    def __init__(self, hour: int, minute: int, duration=90):
        self._hour = hour
        self._minute = minute
        self._duration = duration

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if type(value) is int and 0 <= value <= 23:
            self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if type(value) is int and 0 <= value <= 59:
            self._minute = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if type(value) is int:
            self._duration = value

    def __lt__(self, other):
        return self._hour < other.hour or \
                (self._hour == other.hour and self._minute < other.minute)

    def __eq__(self, other):
        return self._hour == other.hour and self._minute == other.minute

    def __le__(self, other):
        return self < other or self == other

    def __sub__(self, other):
        def sub_minutes(self, value):
            self_mins = self.hour * 60 + self.minute
            if self_mins >= value:
                return BasicTerm((self_mins - value) // 60, self_mins - (self_mins - value) // 60 * 60,
                                 self.duration)
            else:
                self_mins = 24 * 60 - value - self_mins
                return BasicTerm(self_mins // 60, self_mins - self_mins // 60 * 60, self.duration)

        def sub_terms(self, other):
            raise ValueError("BasicTerm subtraction not supported")

        if type(other) is int:
            return sub_minutes(self, other)
        elif type(other) is BasicTerm:
            return sub_terms(self, other)

    def __add__(self, other):
        if type(other) is not int:
            raise ValueError("BasicTerm addition only with integer")
        self_mins = self.hour * 60 + self.minute
        return BasicTerm((self_mins + other) // 60 % 24,
                         (self_mins + other) - (self_mins + other) // 60 * 60, self.duration)

    def __hash__(self):
        return hash((self.hour, self.minute))

