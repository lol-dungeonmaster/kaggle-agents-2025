from datetime import datetime
from ..basemodel import GeneratedEvent

class DateFormatTool:
    @classmethod
    def get_local_datetime(cls, t: list[int]) -> list[str]:
        """Converts an array of timestamps from epoch time to the local timezone format.

        The result is an array of date and time in locale appropriate format.
        Suitable for use in a locale appropriate response.
        Treat this function as a vector function. Always prefer to batch timestamps for conversion.
        Use this function to format date and time in your responses.

        Args:
            t: An array of timestamps in seconds since epoch to be converted.
            The order of timestamps matches the order of conversion.

        Returns:
            A list of strings, where each string is a date and time in locale-appropriate format.
            Example:
            [
            "March 15, 2023 12:00:00 PM",
            "March 16, 2023 09:30:00 AM"
            ]
        """
        local_t = []
        for timestamp in t:
            local_t.append(cls.local_date_from_epoch(timestamp))
        return local_t

    @classmethod
    def local_date_from_epoch(cls, timestamp):
        if len(str(timestamp)) == 13:
            return datetime.fromtimestamp(timestamp/1000, tz=GeneratedEvent.tz()).strftime('%c')
        else:
            return datetime.fromtimestamp(timestamp, tz=GeneratedEvent.tz()).strftime('%c')