from .term import Term
from .day import *
from math import ceil


class Lesson:

    def __init__(self, timetable,
                 term: Term, name: str, teacherName: str,
                 year: int, fullTime: bool):
        self._term = term
        self._name = name
        self._teacherName = teacherName
        self._year = year
        self._fullTime = fullTime
        timetable.put(self)
        self.timetable = timetable

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term):
        if self.isTermGood(term):
            self._term = term

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self._year = year

    @property
    def fullTime(self):
        return self._fullTime

    @fullTime.setter
    def fullTime(self, val):
        if isinstance(val, bool):
            self._fullTime = val

    def earlierDay(self):
        new_term = Term(nthDayFrom(-1, self._term._Term__day), self._term._hour, self._term._minute,
                        self._term._duration)
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self._term = new_term
            return True
        else:
            return False

    def laterDay(self):
        new_term = Term(nthDayFrom(1, self._term._Term__day), self._term._hour, self._term._minute,
                        self._term._duration)
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self._term = new_term
            return True
        else:
            return False

    def earlierTime(self, duration):
        duration_days = duration // (60 * 24)
        duration -= duration_days * (60 * 24)
        duration_hours = duration // 60
        duration -= duration_hours * 60
        new_term = Term(self._term._Term__day, self._term._hour,
                        self._term._minute, self._term._duration)
        if duration <= new_term._minute:
            new_term._minute -= duration
        else:
            new_term._minute = new_term._minute - duration + 60
            new_term._hour -= 1 # if current term is correct, this shift can't go back a day
        if duration_hours <= new_term._hour:
            new_term._hour -= duration_hours
        else:
            new_term._hour = new_term._hour - duration_hours + 24
            new_term._Term__day = nthDayFrom(-1, new_term._Term__day)
        new_term._Term__day = nthDayFrom(-duration_days, new_term._Term__day)
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self._term = new_term
            return True
        return False

    def laterTime(self, duration):
        duration_days = duration // (60 * 24)
        duration -= duration_days * (60 * 24)
        duration_hours = duration // 60
        duration -= duration_hours * 60
        new_term = Term(self._term._Term__day, self._term._hour,
                        self._term._minute, self._term._duration)
        if new_term._minute + duration >= 60:
            new_term._minute = new_term._minute + duration - 60
            new_term._hour += 1 # if previous term was correct this is too
        else:
            new_term._minute += duration
        if new_term._hour + duration_hours > 23:
            new_term._hour = new_term._hour + duration_hours - 24
            new_term._Term__day = nthDayFrom(1, new_term.getDay())
        else:
            new_term._hour += duration_hours
        new_term._Term__day = nthDayFrom(duration_days, new_term._Term__day)
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self._term = new_term
            return True
        else:
            return False

    def isTermGood(self, term):
        if self._fullTime:
            if (0 <= term._Term__day.value <= 3 and 8 <= term._hour <= 19 \
                and 8 <= term._hour + ceil((term._minute + term._duration) / 60) <= 20) or \
                (term._Term__day.value == 4 and 8 <= term._hour <= 16 \
                 and 8 <= term._hour + ceil((term._minute + term._duration) / 60) <= 20):
                # also checks if it finished before 8p.m.
                return True
            else:
                return False
        else:
            if (term._Term__day.value == 4 and 17 <= term._hour <= 19 \
                and 17 <= term._hour + ceil((term._minute + term._duration) / 60) <= 20) or \
               (5 <= term._Term__day.value <= 6 and 8 <= term._hour <= 19 \
                and 8 <= term._hour + ceil((term._minute + term._duration)) / 60):
                return True
            else:
                return False

    def __str__(self):
        duration = 90
        duration_days = duration // (60 * 24)
        duration -= duration_days * (60 * 24)
        duration_hours = duration // 60
        duration -= duration_hours * 60
        new_term = Term(self._term._Term__day, self._term._hour,
                        self._term._minute, self._term._duration)
        if new_term._minute + duration >= 60:
            new_term._minute = new_term._minute + duration - 60
            new_term._hour += 1 # if previous term was correct this is too
        else:
            new_term._minute += duration
        if new_term._hour + duration_hours > 23:
            new_term._hour = new_term._hour + duration_hours - 24
            new_term._Term__day = nthDayFrom(1, new_term.getDay())
        else:
            new_term._hour += duration_hours
        new_term._Term__day = nthDayFrom(duration_days, new_term._Term__day)
        ifFull = "full time" if self._fullTime else "weekend"
        return f"{self._name} ({self._term.getDay()} {self._term._hour}:{str(self._term._minute).zfill(2)}" \
               f"-{new_term._hour}:{str(new_term._minute).zfill(2)})\n{self._year} year of {ifFull.zfill(2)} studies\n" \
               f"Teacher: {self._teacherName}"