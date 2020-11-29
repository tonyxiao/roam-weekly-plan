# -*- coding: utf-8 -*-
# https://github.com/kylestratis/roam-weekly-plan
import sys
import datetime


# https://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python
def week_from_date(date_object):
    date_ordinal = date_object.toordinal()
    year = date_object.year
    week = ((date_ordinal - _week1_start_ordinal(year)) // 7) + 1
    if week >= 52:
        if date_ordinal >= _week1_start_ordinal(year + 1):
            year += 1
            week = 1
    return year, week

def _week1_start_ordinal(year):
    jan1 = datetime.date(year, 1, 1)
    jan1_ordinal = jan1.toordinal()
    jan1_weekday = jan1.weekday()
    week1_start_ordinal = jan1_ordinal - ((jan1_weekday + 1) % 7)
    return week1_start_ordinal

def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def get_next_sunday():
    today = datetime.date.today()
    return today + datetime.timedelta(days=-today.weekday()-1, weeks=1)

def next_week():
    today = datetime.date.today()
    next_sunday = get_next_sunday()
    return [
        custom_strftime("%B {S}, %Y", next_sunday + datetime.timedelta(days=i))
        for i in range(0, 7)
    ]

def next_week_number():
  return week_from_date(get_next_sunday())

def generate_template():
    week = next_week()
    week_number = next_week_number()
    template = """
Week {weekno} of {year}
Sunday: [[{sunday}]]
Monday: [[{monday}]]
Tuesday: [[{tuesday}]]
Wednesday: [[{wednesday}]]
Thursday: [[{thursday}]]
Friday: [[{friday}]]
Saturday: [[{saturday}]]
    """.format(
        year=week_number[0],
        weekno=week_number[1],
        sunday=week[0],
        monday=week[1],
        tuesday=week[2],
        wednesday=week[3],
        thursday=week[4],
        friday=week[5],
        saturday=week[6],
    )
    return template


s = generate_template()
sys.stdout.write(s)