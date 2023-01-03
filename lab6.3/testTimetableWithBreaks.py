import unittest
from DeanerySystem.timetable_with_breaks import TimetableWithBreaks
from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.day import Day
from DeanerySystem.action import Action
from DeanerySystem.Break import Break


class Test_TimetableWithBreaks(unittest.TestCase):

    def test_shifts_no_skip_breaks(self):
        TimetableWithBreaks.skipBreaks = False
        breaks = [
            Break(Term(Day.MON, 9, 30, 10)),
            Break(Term(Day.MON, 11, 10, 10)),
            Break(Term(Day.MON, 12, 50, 10)),
            Break(Term(Day.MON, 14, 30, 30))
        ]
        timetable = TimetableWithBreaks(breaks)
        lessons = [
            Lesson(timetable, Term(Day.WED, 8, 0), "Alg. macierzowe", "Teacher1", 3, True),
            Lesson(timetable, Term(Day.WED, 9, 40), "Kryptografia", "Teacher2", 2, True),
            Lesson(timetable, Term(Day.WED, 11, 20), "Skryptowe", "Teacher3", 2, True),
        ]
        with self.assertRaises(ValueError):
            Lesson(timetable, Term(Day.MON, 11, 10), "This should not appear", "", 0, True)

        self.assertEqual(len(timetable.lessons), 3)
        with self.assertRaises(ValueError):
            lessons[1].laterTime(90) # should not move - collision
        with self.assertRaises(ValueError):
            lessons[2].laterTime(90) # should not move because skipBreaks = False
        self.assertTrue(lessons[2].laterTime(100)) # OK

    def test_shifts_skip_breaks(self):
        TimetableWithBreaks.skipBreaks = True
        breaks = [
            Break(Term(Day.MON, 9, 30, 10)),
            Break(Term(Day.MON, 11, 10, 10)),
            Break(Term(Day.MON, 12, 50, 10)),
            Break(Term(Day.MON, 14, 30, 30))
        ]
        timetable = TimetableWithBreaks(breaks)
        lessons = [
            Lesson(timetable, Term(Day.WED, 8, 0), "Alg. macierzowe", "Teacher1", 3, True),
            Lesson(timetable, Term(Day.WED, 9, 40), "Kryptografia", "Teacher2", 2, True),
            Lesson(timetable, Term(Day.WED, 11, 20), "Skryptowe", "Teacher3", 2, True),
        ]
        self.assertEqual(len(timetable.lessons), 3)
        self.assertTrue(lessons[2].laterTime(90))
        self.assertTrue(lessons[2].laterTime(90))

    def test_shifting(self):
        TimetableWithBreaks.skipBreaks = True
        timetable = TimetableWithBreaks([Break(Term(Day.MON, 9, 30, 10))])
        term1 = Term(Day.TUE, 8, 0)
        term2 = Term(Day.MON, 11, 00)
        lesson1 = Lesson(timetable, term1, "Podstawy eksploatacji złóż gazu", "Janusz", 2, True)
        lesson2 = Lesson(timetable, term2, "Podstawy gazownictwa ziemnego", "Janusz", 2, True)
        with self.assertRaises(ValueError):
            timetable.perform(timetable.parse(["t-", "d-", "t+", "d-"]))
