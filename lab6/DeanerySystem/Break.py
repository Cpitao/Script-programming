from .basic_term import BasicTerm
from .term import Term


class Break:
    def __init__(self, brk: BasicTerm):
        self.__brk = brk

    def __str__(self):
        return "---"

    def getTerm(self):
        return self.__brk

