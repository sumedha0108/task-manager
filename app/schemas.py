from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field


class Category(str, Enum):
    movement = "movement"    # jog, run-walk, home strength
    growth = "growth"        # LeetCode, coding, painting
    nutrition = "nutrition"  # healthier eating
    social = "social"        # calling family/friends
    skincare = "skincare"


class Task(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    category: Category
    duration_min: int = Field(ge=1, le=60)


class CoachResponse(BaseModel):
    """What we demand back from the AI. Anything that doesn't fit is rejected."""
    coach_message: str = Field(min_length=1, max_length=400)
    tasks: list[Task] = Field(min_length=3, max_length=6)


class TaskResult(BaseModel):
    title: str
    category: Category
    status: Literal["done", "missed"]


class CheckinRequest(BaseModel):
    log_text: str = Field(min_length=1, max_length=2000)
    mood: int | None = Field(default=None, ge=1, le=5)
    energy: int | None = Field(default=None, ge=1, le=5)
    today_results: list[TaskResult] = []   # temporary: from the DB later
    week_summary: str = Field(default="", max_length=1500)  # same


class CheckinResponse(BaseModel):
    for_date: str
    day_type: str
    coach_message: str
    tasks: list[Task]