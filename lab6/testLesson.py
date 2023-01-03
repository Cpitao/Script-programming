from DeanerySystem.lesson import *
from DeanerySystem.timetable_without_breaks import TimetableWithoutBreaks
import unittest


class Test_Lesson(unittest.TestCase):

    def test_earlierDay(self):
        timetable = TimetableWithoutBreaks()
        term = Term(Day.TUE, 9, 30)
        lesson = Lesson(timetable, term, "PE", "Kowalski", 2050, True)
        lesson.earlierDay()
        self.assertEqual(Day.MON, lesson.term.getDay())

    def test_laterDay(self):
        timetable = TimetableWithoutBreaks()
        term = Term(Day(2), 10, 30)
        lesson = Lesson(timetable, term, "PE", "Kowalski", 2050, True)
        self.assertTrue(lesson.laterDay())
        self.assertEqual(lesson._term.getDay(), Day(3))

    def test_laterDay_invalid(self):
        timetable = TimetableWithoutBreaks()
        term = Term(Day(6), 10, 30)
        lesson = Lesson(timetable, term, "PE", "Kowalski", 2050, False)
        self.assertFalse(lesson.laterDay())

    def test_laterTime(self):
        timetable = TimetableWithoutBreaks()
        term = Term(Day(3), 10, 30)
        lesson = Lesson(timetable, term, "PE", "Kowalski", 2050, True)
        self.assertTrue(lesson.laterTime(90))
        self.assertEqual(Term(Day(3), 12, 0), lesson._term)
    
    def test_earlierTime(self):
        timetable = TimetableWithoutBreaks()
        term = Term(Day(3), 10, 30)
        lesson = Lesson(timetable, term, "PE", "Kowalski", 2050, True)
        self.assertTrue(lesson.earlierTime(90))
        self.assertEqual(9, lesson._term._hour)
        self.assertEqual(0, lesson._term._minute)


if __name__ == "__main__":
    unittest.main()