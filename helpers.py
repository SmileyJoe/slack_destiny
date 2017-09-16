from datetime import datetime, timedelta


class Time:

    @staticmethod
    def elapsed(seconds):
        formatted = ""
        time = datetime(1, 1, 1) + timedelta(seconds=seconds)
        day = time.day-1
        hour = time.hour
        minute = time.minute

        if day > 0:
            formatted = Time.plural("day", day)

        if hour > 0 or formatted:
            if formatted:
                formatted += ", "
            formatted += Time.plural("hour", hour)

        if minute > 0 or formatted:
            if formatted:
                formatted += ", "
            formatted += Time.plural("minute", minute)

        return formatted

    @staticmethod
    def plural(title, value):
        plural = ""
        if value > 1 or value == 0:
            plural = "s"

        return "{} {}{}".format(value, title, plural)
