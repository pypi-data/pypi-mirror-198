from enum import Enum
from typing import Dict, Any, Union


class Interval(Enum):
    OneMinute = "1m"
    ThreeMinute = "3m"
    FiveMinute = "5m"
    FifteenMinute = "15m"
    ThirtyMinute = "30m"
    OneHour = "1h"
    TwoHour = "2h"
    FourHour = "4h"
    EightHour = "8h"
    TwelveHour = "12h"
    OneDay = "1d"
    ThreeDay = "3d"
    OneWeek = "1w"
    OneMonth = "1M"


Json = Union[Dict[str, Any], None]
