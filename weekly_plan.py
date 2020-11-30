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


def get_start_date():
    today = datetime.date.today()
    return today
    # return today + datetime.timedelta(days=-today.weekday()-1, weeks=1)

def generate_week():
    start_date = get_start_date()
    return [start_date + datetime.timedelta(days=i) for i in range(0, 14)] # Extra for all the iOS craziness...

def get_week_number():
  return week_from_date(get_start_date())

def generate_template():
    week = generate_week()
    week_number = get_week_number()
    template = """Week {weekno} of {year}
""".format(
        year=week_number[0],
        weekno=week_number[1],
    ) + "\n".join(["""{weekday}: [[{date}]]""".format(weekday=day.strftime("%A"), date=custom_strftime("%B {S}, %Y", day)) for day in week])
    return template


s = generate_template()
sys.stdout.write(s)