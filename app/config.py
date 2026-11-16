import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")

TIMEZONE = "Asia/Kolkata"   # your day boundary, not the server's (servers usually run UTC)

CAP_WEEKDAY_MIN = 40
CAP_SATURDAY_MIN = 90   # my guess, change freely
CAP_SUNDAY_MIN = 75     # my guess, change freely

MAX_ATTEMPTS = 3        # LLM calls per check-in