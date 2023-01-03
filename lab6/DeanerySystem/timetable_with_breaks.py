from typing import List
from .Break import Break
from .basic_term import BasicTerm


class TimetableWithBreaks:
    def __init__(self, breaks: List[Break]):
        self.breaks = breaks
        self.lessons = []

    def __str__(self):
        all_terms_to_basic = [BasicTerm(l.term.hour, l.term.minute, l.term.duration) for l in self.lessons]
        all_terms_to_basic += [b.getTerm() for b in self.breaks]
        all_terms_to_basic += [b + b.duration for b in all_terms_to_basic]
        all_terms_to_basic = set(all_terms_to_basic)
        header = ""