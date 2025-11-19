from datetime import datetime
from ..basemodel import GeneratedEvent
from ..fntool_def import DateFnDef

class DateFormatTool(DateFnDef):
    @classmethod
    def get_local_datetime(self, t: list[int]):
        local_t = []
        for timestamp in t:
            local_t.append(self.local_date_from_epoch(timestamp))
        return local_t

    @classmethod
    def local_date_from_epoch(self, timestamp):
        if len(str(timestamp)) == 13:
            return datetime.fromtimestamp(timestamp/1000, tz=GeneratedEvent.tz()).strftime('%c')
        else:
            return datetime.fromtimestamp(timestamp, tz=GeneratedEvent.tz()).strftime('%c')