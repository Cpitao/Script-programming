from DeanerySystem.timetable_with_breaks import *

if __name__ == '__main__':
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
    try:
        Lesson(timetable, Term(Day.MON, 11, 10), "Shifted", "", 0, True)
    except ValueError:
        print("Given term is already occupied")
    print(timetable)
