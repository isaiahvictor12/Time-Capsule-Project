class Time:
    def __init__(self, month, day, year) -> None:
        self.month = month
        self.day = day
        self.year = year
        self.total_time = str(self.year) + str(self.month) + str(self.day)
        pass

    