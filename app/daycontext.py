from dataclasses import dataclass
from datetime import date
from . import config


@dataclass(frozen=True)
class DayContext:
    day_type: str   # "weekday" | "saturday" | "sunday"
    cap_min: int    # total task minutes allowed that day
    jog_rule: str   # plain-English rule that goes into the prompt


def day_context(d: date) -> DayContext:
    if d.weekday() == 0:
        return DayContext(day_type="weekday", cap_min=config.CAP_WEEKDAY_MIN, jog_rule="No jogging today. Movement must be quiet indoor strength/mobility.")
    elif d.weekday() == 5:
        return DayContext(day_type="saturday", cap_min=config.CAP_SATURDAY_MIN, jog_rule="Outdoor jog (run-walk intervals) IS allowed today")
    elif d.weekday() == 6:
        return DayContext(day_type="sunday", cap_min=config.CAP_SUNDAY_MIN, jog_rule="Jog only as a BACKUP if Saturday's jog was missed; otherwise no jog.")
    