from .basic_timetable import BasicTimetable
from .lesson import Lesson, Day
from .term import Term


class TimetableWithoutBreaks(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lessons = {}

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

        if term in self.lessons:
            return self.lessons[term]
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
            self.lessons[lesson.term] = lesson
            return True
        return False

    def __str__(self):
        s = ""
        # this will be a lot of spaghetti code
        day_lessons = [list(filter(lambda x: x.term.getDay() == Day(i), self.lessons.values()))
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
                for l in self.lessons.values():
                    if l.term.hour * 60 + l.term.minute == 8 * 60 + 90 * i and \
                            l.term.getDay() == Day(j):
                        s += f"{l.name:{max_lengths[j + 1]}}|"
                        break
                else:
                    s += f"{'':{max_lengths[j + 1]}}|"
            s += '\n'
        return s

    def move(self, lesson: Lesson, term: Term):
        lesson.term = term