from typing import List
from .term import Term
from .lesson import Lesson, Day
from .action import Action
from math import ceil
from .Break import Break


class TimetableWithBreaks:
    """ Class containing a set of operations to manage the timetable """
    skipBreaks = False

    def __init__(self, breaks: List[Break]):
        self.lessons = []
        self.breaks = breaks

    ##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""

        if self.busy(term):
            return False

        if fullTime:
            if (0 <= term.getDay().value <= 3 and 8 <= term.hour <= 19
                and 8 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20) or \
                    (term.getDay().value == 4 and 8 <= term.hour <= 16
                     and 8 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20):
                # also checks if it finished before 8p.m.
                return True
            else:
                return False
        else:
            if (term.getDay().value == 4 and 17 <= term.hour <= 19
                and 17 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20) or \
                    (5 <= term.getDay().value <= 6 and 8 <= term.hour <= 19
                     and 8 <= term.hour + ceil((term.minute + term.duration)) / 60):
                return True
            else:
                return False

    ##########################################################

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

        for l in self.lessons:
            if (term > l.term and (term - l.term).duration < term.duration + l.term.duration) or \
                    (l.term > term and (l.term - term).duration < term.duration + l.term.duration) or \
                    (term.hour == l.term.hour and term.minute == l.term.minute and term.getDay() == l.term.getDay()):
                return True
        return False

    ##########################################################

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
                    return False
            self.lessons.append(lesson)
            return True
        return False

    ##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """
        mappings = {"d-": Action.DAY_EARLIER,
                    "d+": Action.DAY_LATER,
                    "t-": Action.TIME_EARLIER,
                    "t+": Action.TIME_LATER}

        return list(map(lambda x: mappings[x],
                        filter(lambda x: x in mappings, actions)))

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions.
N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        for i, action in enumerate(actions):
            if action == Action.DAY_LATER:
                self.lessons[i % len(self.lessons)].laterDay()
            elif action == Action.DAY_EARLIER:
                self.lessons[i % len(self.lessons)].earlierDay()
            elif action == Action.TIME_LATER:
                self.lessons[i % len(self.lessons)].laterTime(90)
            elif action == Action.TIME_EARLIER:
                self.lessons[i % len(self.lessons)].earlierTime(90)

    ##########################################################

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """

        for l in self.lessons:
            if l.term == term:
                return l
        return None

    def __str__(self):
        # this one looks like spaghetti but at least its flexible
        key_hours = [(l.term.hour, l.term.minute) for l in self.lessons]
        key_hours += [(l.term.hour + (l.term.minute + l.term.duration) // 60 % 24,
                       l.term.minute + l.term.duration - (l.term.minute + l.term.duration) // 60 * 60)
                      for l in self.lessons]
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
                for l in self.lessons:
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
