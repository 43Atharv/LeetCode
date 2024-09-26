class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        pos = bisect.bisect_right(self.bookings, (start, end))

        if pos > 0 and start < self.bookings[pos - 1][1]:
            return False
        if pos < len(self.bookings) and end > self.bookings[pos][0]:
            return False

        self.bookings.insert(pos, (start, end))
        return True


