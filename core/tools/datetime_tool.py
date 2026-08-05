from datetime import datetime


class DateTimeTool:

    def current_time(self):

        return datetime.now().strftime("%I:%M %p")

    def current_date(self):

        return datetime.now().strftime("%d %B %Y")

    def current_day(self):

        return datetime.now().strftime("%A")