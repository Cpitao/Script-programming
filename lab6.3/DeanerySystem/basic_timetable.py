from abc import ABC, abstractmethod
from math import ceil
from typing import List
from .action import Action
from .lesson import Lesson
from .term import Term


class BasicTimetable(ABC):

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

        try:
            return list(map(lambda x: mappings[x], actions))
        except KeyError:
            raise ValueError("Invalid mapping string")

    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass

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

        if term in self.lessons:
            return self.lessons[term]
        raise ValueError("No lesson at given term")

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions.
N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        l_list = list(self.lessons.values())
        for i, action in enumerate(actions):
            if action == Action.DAY_LATER:
                l_list[i % len(self.lessons.values())].laterDay()
            elif action == Action.DAY_EARLIER:
                l_list[i % len(self.lessons.values())].earlierDay()
            elif action == Action.TIME_LATER:
                l_list[i % len(self.lessons.values())].laterTime(90)
            elif action == Action.TIME_EARLIER:
                l_list[i % len(self.lessons.values())].earlierTime(90)

    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass