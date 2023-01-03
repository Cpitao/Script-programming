import unittest
from DeanerySystem.timetable_without_breaks import TimetableWithoutBreaks
from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.day import Day
from DeanerySystem.action import Action


class Test_Timetable(unittest.TestCase):

    def test_shifting(self):
        timetable = TimetableWithoutBreaks()
        term1 = Term(Day.TUE, 9, 30)
        term2 = Term(Day.MON, 11, 00)
        lesson1 = Lesson(timetable, term1, "Podstawy eksploatacji złóż gazu", "Janusz", 2, True)
        lesson2 = Lesson(timetable, term2, "Podstawy gazownictwa ziemnego", "Janusz", 2, True)
        with self.assertRaises(ValueError):
            timetable.perform(timetable.parse(["t-", "d-", "t+", "d-"]))

    def test_parsing(self):
        action_string_list = ["t-", "d-", "t+", "d+"]
        actions = [Action.TIME_EARLIER, Action.DAY_EARLIER, Action.TIME_LATER, Action.DAY_LATER]
        self.assertListEqual(actions, TimetableWithoutBreaks().parse(action_string_list))

    def test_get(self):
        timetable = TimetableWithoutBreaks()
        term1 = Term(Day.TUE, 9, 30)
        lesson1 = Lesson(timetable, term1, "Podstawy eksploatacji złóż gazu", "Janusz", 2, True)
        self.assertEqual(timetable.get(Term(Day.TUE, 9, 30)), lesson1)

    def test_put_invalid(self):
        timetable = TimetableWithoutBreaks()
        term1 = Term(Day.TUE, 9, 30)
        lesson1 = Lesson(timetable, term1, "Podstawy eksploatacji złóż gazu", "Janusz", 2, True)
        lesson2 = Lesson(timetable, term1, "Podstawy eksploatacji złóż gazu", "Janusz", 2, True)
        self.assertEqual(len(timetable.lessons), 1)
