from datetime import date, timedelta


class student:
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

