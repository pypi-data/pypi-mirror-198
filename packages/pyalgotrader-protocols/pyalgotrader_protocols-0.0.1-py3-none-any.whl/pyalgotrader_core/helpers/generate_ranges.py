from datetime import datetime, timedelta
from typing import Dict, List


def generate_ranges(
    tz, start_timestamp: int, end_timestamp: int, days: int = 100
) -> List[Dict[str, int]]:
    ranges = []
    current_start = datetime.fromtimestamp(start_timestamp, tz=tz)
    end = datetime.fromtimestamp(end_timestamp, tz=tz)

    while current_start < end:
        current_end = min(current_start + timedelta(days=days), end)
        range = {
            "fetch_from_epoch": int(current_start.timestamp()),
            "fetch_to_epoch": int(current_end.timestamp()),
        }
        ranges.append(range)
        current_start = current_end

    return ranges
