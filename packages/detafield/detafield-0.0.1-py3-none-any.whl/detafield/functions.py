__all__ = ['age']

import datetime
import calendar



def age(start: datetime.date, end: datetime.date = None):
	end = end or datetime.date.today()
	return (((end - start).days - calendar.leapdays(start.year, end.year)) / 365).__round__(2)
