from datetime import date
from dateutil.relativedelta import relativedelta
from collections.abc import Iterable

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


class Family(Iterable):
    def __init__(self, members:list[Person]):
        self.members = members
        
    def __str__(self):
        return ', '.join([member.name for member in self.members])

    def __iter__(self):
        return iter(self.members)
    

    

def main():
    family = Family([
        Person('Trillian', date(1970, 3, 14)),
        Person('Arthur', date(1965, 7, 4)),
        Person('Ford', date(1995, 2, 2)),
        Person('Zaphod', date(1997, 5, 1)),
        Person('Douglas', date(1999, 4, 2))
    ])

    singles = [
        Person('Marvin', date(1991, 1, 1)),
        Person('Slarti', date(1993, 9, 9))
    ]

    oldest = None
    earliest_date = date.max
    for m in family:
        if m.birthdate < earliest_date:
            oldest = m
            earliest_date = m.birthdate

    for s in singles:
        if s.birthdate < earliest_date:
            oldest = s
            earliest_date = s.birthdate

    age = relativedelta(date.today(),oldest.birthdate)
    print(f'Oldest person: {oldest.name}; Age: {age.years} years, {age.months} months')

if __name__ == '__main__':
    main()
