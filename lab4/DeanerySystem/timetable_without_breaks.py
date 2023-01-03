from typing import List
from .term import Term
from .lesson import Lesson, Day
from .action import Action
from math import ceil


class TimetableWithoutBreaks:
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lessons = []

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
            if (0 <= term.getDay().value <= 3 and 8 <= term.hour <= 19 \
                and 8 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20) or \
                    (term.getDay().value == 4 and 8 <= term.hour <= 16 \
                     and 8 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20):
                # also checks if it finished before 8p.m.
                return True
            else:
                return False
        else:
            if (term.getDay().value == 4 and 17 <= term.hour <= 19 \
                and 17 <= term.hour + ceil((term.minute + term.duration) / 60) <= 20) or \
                    (5 <= term.getDay().value <= 6 and 8 <= term.hour <= 19 \
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
        s = ""
        # this will be a lot of spaghetti code
        day_lessons = [list(filter(lambda x: x.term.getDay() == Day(i), self.lessons))
                       for i in range(7)]
        row_labels = ["8:00-9:30",
                      "9:30-11:00",
                      "11:00-12:30",
                      "12:30-14:00",
                      "14:00-15:30",
                      "15:30-17:00",
                      "17:00-18:30",
                      "18:30-20:00"]
        # max lengths will indicate necessary padding
        max_lengths = [max(len(lab) for lab in row_labels)] + \
                      [max([0] + [len(x.name) for x in lessons]) for lessons in day_lessons]
        for i in range(7):
            max_lengths[i + 1] = max(max_lengths[i + 1], len(str(Day(i))))

        # header row
        s += f'|{"":{max_lengths[0]}}|'
        for i in range(7):
            s += f"{Day(i):{max_lengths[i+1]}}|"
        s += '\n'
        for i in range(len(row_labels)):
            s += f"|{row_labels[i]:{max_lengths[0]}}|"
            for j in range(7):
                for l in self.lessons:
                    if l.term.hour * 60 + l.term.minute == 8 * 60 + 90 * i and \
                            l.term.getDay() == Day(j):
                        s += f"{l.name:{max_lengths[j + 1]}}|"
                        break
                else:
                    s += f"{'':{max_lengths[j + 1]}}|"
            s += '\n'
        return s