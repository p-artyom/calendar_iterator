class CalendarIterator:
    def __init__(self):
        self.MONTH = [
            'января',
            'февраля',
            'марта',
            'апреля',
            'мая',
            'июня',
            'июля',
            'августа',
            'сентября',
            'октября',
            'ноября',
            'декабря',
        ]
        self.DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.LAST_MONTH = 11
        self.num_days = 1
        self.num_month = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (
            self.num_days <= self.DAYS[-1]
            and self.num_month != self.LAST_MONTH
        ):
            if self.num_days > self.DAYS[self.num_month]:
                self.num_days = 1
                self.num_month += 1
            day = self.num_days
            month = self.MONTH[self.num_month]
            self.num_days += 1
            return f'{day} {month}'
        raise StopIteration


if __name__ == '__main__':
    calendar_iterator = CalendarIterator()
    while True:
        print(next(calendar_iterator))
