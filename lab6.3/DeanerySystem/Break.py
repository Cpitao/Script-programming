from .basic_term import BasicTerm


class Break:
    def __init__(self, term: BasicTerm):
        self._term = term
        self.hour = term.hour
        self.minute = term.minute
        self.duration = term.duration

    def getTerm(self):
        return self._term

    @property
    def term(self):
        return self._term

    def __str__(self):
        return "---"
