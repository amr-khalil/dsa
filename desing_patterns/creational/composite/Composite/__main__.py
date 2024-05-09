from datetime import date
from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from collections.abc import Iterable
from functools import reduce


class AbsComposite(ABC):
    @abstractmethod
    def get_oldest(self):
        pass

class Person(AbsComposite):
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def get_oldest(self):
        return self

class Tree(Iterable, AbsComposite):
    def __init__(self, members):
        self._members = members

    def __iter__(self):
        return iter(self._members)

    def get_oldest(self):
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1_.birthdate < t2_.birthdate else t2_
        return reduce(f, self, NullPerson())


class NullPerson(AbsComposite):
    name = None
    birthdate = date.max

    def get_oldest(self):
        return self


def main():
    hitchhikers = Tree(
        [
            Person("Trillian", date(1970, 3, 14)),
            Person("Arthur", date(1965, 7, 4)),
            Person("Ford", date(1995, 2, 2)),
            Person("Zaphod", date(1997, 5, 1)),
            Person("Douglas", date(1999, 4, 2)),
        ]
    )

    singles = Tree(
        [Person("Marvin", date(1991, 1, 1)), Person("Slarti", date(1993, 9, 9))]
    )

    loner = Person("Dirk", date(1990, 6, 6))

    tree1 = Tree([hitchhikers])
    tree2 = Tree([singles, loner])
    tree3 = Tree([tree1, tree2])
    for tree in tree1, tree2, tree3:
        oldest = tree.get_oldest()
        age = relativedelta(date.today(), oldest.birthdate)
        print(
            f"Oldest person: {oldest.name}; Age: {age.years} years, {age.months} months"
        )


if __name__ == "__main__":
    main()
