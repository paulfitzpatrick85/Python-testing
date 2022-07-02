from datetime import date, timedelta


class Student:
    """A student class as base for method testing"""
    def __init__(self, first_name, last_name):
        self._first_name = first_name   # prepend '_' so other dev's know it is for read only
        self._last_name = last_name
        self._start_date = date.today()  # when instance of 'student' is created, start date is set using of instance of creation
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property  # method to get data only
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):    # green for alert_santa funct
        self.naughty_list = True

    @property  # method to get data only
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)



