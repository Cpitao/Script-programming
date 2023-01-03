from .term import Term


class Break:
    def __init__(self, term: Term):
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
