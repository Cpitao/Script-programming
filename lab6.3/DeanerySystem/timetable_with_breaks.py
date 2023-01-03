from typing import List

from .Break import Break
from .basic_timetable import BasicTimetable
from .lesson import Lesson, Day
from .term import Term


class TimetableWithBreaks(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """
    skipBreaks = False

    def __init__(self, breaks: List[Break]):
        self.lessons = {}
        self.breaks = breaks

    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transferred_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """
        if not TimetableWithBreaks.skipBreaks:
            for b in self.breaks:
                term_start = term.hour * 60 + term.minute
                term_end = term.hour * 60 + term.minute + term.duration
                break_start = b.hour * 60 + b.minute
                break_end = b.hour * 60 + b.minute + b.duration
                if (term_start <= break_start < term_end) or \
                        (break_start <= term_start < break_end):
                    return True

        if term in self.lessons:
            return True
        return False

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """

        if self.can_be_transferred_to(lesson.term, lesson.fullTime):
            for b in self.breaks:
                term_start = lesson.term.hour * 60 + lesson.term.minute
                term_end = lesson.term.hour * 60 + lesson.term.minute + lesson.term.duration
                break_start = b.hour * 60 + b.minute
                break_end = b.hour * 60 + b.minute + b.duration
                if (term_start <= break_start < term_end) or \
                        (break_start <= term_start < break_end):
                    raise ValueError("Given term is already occupied")
            self.lessons[lesson.term] = lesson
            return True
        raise ValueError("Given term is already occupied")

    def __str__(self):
        # this one looks like spaghetti but at least its flexible
        key_hours = [(l.term.hour, l.term.minute) for k, l in self.lessons.items()]
        key_hours += [(l.term.hour + (l.term.minute + l.term.duration) // 60 % 24,
                       l.term.minute + l.term.duration - (l.term.minute + l.term.duration) // 60 * 60)
                      for k, l in self.lessons.items()]
        key_hours += [(l.term.hour, l.term.minute) for l in self.breaks]
        key_hours += [(l.term.hour + (l.term.minute + l.term.duration) // 60 % 24,
                       l.term.minute + l.term.duration - (l.term.minute + l.term.duration) // 60 * 60)
                      for l in self.breaks]
        key_hours = sorted(list(set(key_hours)))
        cell_width = 20
        s = f"{'':{5}}|"
        for i in range(7):
            s += f"{Day(i):{cell_width}}|"
        s += '\n'

        for h in key_hours:
            s += f"{str(h[0]).zfill(2)}:{str(h[1]).zfill(2)}|"
            for i in range(7):
                for k, l in self.lessons.items():
                    if l.term.getDay() == Day(i) and l.term.hour == h[0] and l.term.minute == h[1]:
                        s += f"{l.name:20}|"
                        break
                else:
                    for b in self.breaks:
                        if b.term.hour == h[0] and b.term.minute == h[1]:
                            s += f"{str(b):{cell_width}}|"
                            break
                    else:
                        s += "*" * 20 + "|"
            s += '\n'
        return s

    def move(self, lesson: Lesson, term: Term):
        if self.can_be_transferred_to(term, lesson.fullTime):
            if TimetableWithBreaks.skipBreaks:
                for b in self.breaks:
                    term_start = term.hour * 60 + term.minute
                    break_start = b.hour * 60 + b.minute
                    if term_start == break_start:
                        self.move(lesson, term + b.duration)
                        break
                else:
                    lesson.term = term
            else:
                lesson.term = term
