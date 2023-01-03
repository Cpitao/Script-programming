from enum import Enum


class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        for i in range(-3, 4):
            if nthDayFrom(i, self).name == day.name:
                return i
    
    def __str__(self):
        strs = ["Poniedziałek",
                "Wtorek",
                "Środa",
                "Czwartek",
                "Piątek",
                "Sobota",
                "Niedziela"]
        return strs[self.value]

def nthDayFrom(n, day):
    return Day((day.value + n) % 7)
